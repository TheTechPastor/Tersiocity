---
tag: Blog, Wifi Explorer
source: https://www.intuitibits.com/2017/08/11/understanding-scan-modes-wifiexplorerpro/
---

Wi-Fi scanning is one of the basic functions in a wireless network. It is the mechanism by which a client device (e.g. computer) or an application discovers the wireless networks that are in range of the Wi-Fi adapter. As part of this process, a scanning device or application gathers information about the signal strength, channel, security configuration and capabilities of nearby networks. Client devices use this information to determine which networks they can join or roam to. Meanwhile, applications such as WiFi Explorer Pro can use it to aid in the monitoring and troubleshooting of the wireless infrastructure.

In this blog post, I will briefly talk about how Wi-Fi scanning works, and then I will focus on how this process is accomplished in WiFi Explorer Pro, including the pros and cons of each scan mode. I believe it is important to understand the differences between each scan mode so that you know what to expect in terms of scan precision and performance. Just be aware that the technical details described here are specific to WiFi Explorer Pro and the macOS frameworks and libraries that it uses, so please do not assume the behavior and limitations of Wi-Fi scanning are the same for all platforms.

### **How Wi-Fi scanning works?**

There are two methods to perform Wi-Fi scanning: _active_ and _passive_. During an active scan, the client device searches for wireless networks by transmitting probes and listening for responses from the access points in range. These responses describe the configuration and capabilities of each of the wireless networks managed by the access point. On the other hand, during a passive scan, the client device listens for beacons, which are specific frames transmitted by the access points to announce their presence and, similarly to a probe response, also include the configuration and capabilities of the wireless networks they service. A client device must listen on a channel long enough to catch a beacon from a nearby access point. By default, beacons are transmitted at a rate of approximately 10 per second.

![](https://intuitibits.com/wp-content/uploads/2020/06/wifiexplorer-scan-modes.png)

#### **Active vs. passive scanning**

An active scan is the recommended mechanism to efficiently find nearby wireless networks. The method, and the probe request and response frames involved in this process, were designed specifically to carry out the scan as fast as possible. Active scanning is supported by basically all the Wi-Fi drivers, so your computer, smartphone, etc., and pretty much every Wi-Fi scanner program use this method. Existing libraries allow applications to easily perform active scans without worrying about low-level implementation details, such as hopping between channels, sending probes and processing the responses from the access points.

However, from a troubleshooting perspective, active scanning has a few disadvantages. First, this method cannot be used, in general, to find wireless networks that do not broadcast their SSID (also known as hidden networks), and second, it may result in shorter scan ranges because client devices usually transmit at lower power levels. As a consequence, access points that are located farther away cannot decode the probes and will not send a response to the client.

Alternatively, a passive scan allows you to find all networks, including those that are hidden and located at farther distances (contrary to client devices, access points usually transmit at higher power levels), but requires specific capabilities from the Wi-Fi driver and some extra coding. For example, the driver must have the ability to put the Wi-Fi interface in monitor mode and provide a mechanism to supply additional information about the frames, such as the signal strength at which the frames are being received from the access point. Wi-Fi scanners doing a passive scan would need to (somehow) iterate over the different supported channels, listen for beacons, and extract additional information from specialized frame headers that are used by the Wi-Fi driver to pass information to user-space applications.

As mentioned above, both beacon and probe response frames include configuration and capability information about the wireless network. Some information is included as part of the frame header, for example, whether or not the network is protected by an encryption mechanism. However, most of the information is provided as Information Elements, which are [TLV](https://en.wikipedia.org/wiki/Type-length-value) (type-value-length) encoded fields. Some information elements are mandatory depending on the type of frame that carries them, while others are optional. Also, manufacturers can insert proprietary information elements (known as vendor-specific elements). If the access point or client device does not know how to interpret a certain vendor-specific information element, it simply ignores it.

![](https://intuitibits.com/wp-content/uploads/2020/06/ie.png)

### **Scan modes in WiFi Explorer Pro**

WiFi Explorer Pro implements three main scan modes: active, passive and directed. As their name says, active and passive scan modes perform active and passive scanning using the built-in Wi-Fi adapter, respectively. Directed scan mode is a variation of active scanning on which the scan targets networks by name (SSID), as opposed to a normal active scan that targets all networks in range of the adapter. The details, pros and cons of each scan mode are described next.

![](https://intuitibits.com/wp-content/uploads/2020/06/scan_modes.png)

#### **Active scan mode**

When you choose active scan mode, WiFi Explorer Pro uses the [CoreWLAN](https://developer.apple.com/documentation/corewlan) system framework and API to perform an active scan. An active scan can be performed while associated to a network, however, it will still interrupt the normal transmission of data packets. That’s why doing throughput tests, for example, while running WiFi Explorer Pro (or any other Wi-Fi scanner) is a bad idea.

Active scan mode is the default mode in WiFi Explorer Pro and it is the only scan mode supported in the standard version of WiFi Explorer.

During an active scan, CoreWLAN broadcasts a series of _null probe requests_ on each supported channel for both the 2.4 and 5 GHz bands. A _null probe request_ does not target any network in particular. Thus, all access points that receive the probe request must send a probe response for each of the wireless networks they manage, with one caveat: if the network is configured as hidden, then the access point can choose not to send a response for that network. Response frames are sent directly to the transmitter of the probe request.

![](https://intuitibits.com/wp-content/uploads/2020/06/wifiexplorer-scan-mode-active.png)

After the probe request frames are transmitted, CoreWLAN listens for probe responses for a limited amount of time before switching to the next channel. Unfortunately, the specific timeout values used by CoreWLAN are unknown, but a full scan can take about 3 to 5 seconds. When running, WiFi Explorer Pro issues a new active scan every 3 seconds. Using shorter intervals has proven to produce errors in CoreWLAN.

When the scan finishes, CoreWLAN passes to WiFi Explorer Pro a dictionary for each network found. This dictionary contains the information elements from the probe response frame along with specific information like BSSID, SSID (network name), RSSI (signal strength), noise, beacon interval, type of network (managed or ad-hoc), channel, physical mode (e.g. 802.11b, 802.11n, etc.) and security type (e.g. WEP, WPA2, etc.). However, I’ve found that physical mode and security type values as provided by CoreWLAN are incorrect for certain network configurations, so WiFi Explorer Pro determines this information instead from the different information elements that CoreWLAN provides as part of the scan results. WiFi Explorer Pro takes all of this information and uses it to populate the network list and create the different views and charts.

One important aspect to note about active scanning is that because probe request frames are sent to the broadcast address, they do not contend for use of the channel and will not be retransmitted if they get corrupted due to a collision with another simultaneous Wi-Fi transmission or from interference caused by a non-802.11 energy source. As a consequence, it might be the case that a network with a strong signal previously detected by WiFi Explorer Pro may suddenly disappear from the scan results because the access point did not hear the probe request(s) during the current active scan. This situation is often misinterpreted as a temporary drop in the signal strength of the access point, but if the drop looks exactly as shown in the figure below (no signal), it is very likely that this is just a result of a probe request being _lost_ due to interference.

![](https://intuitibits.com/wp-content/uploads/2020/06/ap_drop.png)

#### **Passive scan mode**

When using passive scan mode, WiFi Explorer Pro uses a combination of frameworks and libraries to accomplish passive scanning. CoreWLAN by itself does not provide functions to perform passive scanning, so the first thing that WiFi Explorer Pro does is to put the built-in Wi-Fi adapter in monitor mode, which is nicely supported by all Mac models. Monitor mode allows us to capture all the 802.11 frames that can be “heard” by the adapter without having to associate to an access point. In fact, using monitor mode requires the adapter not to be associated to an access point, so if that is the case, WiFi Explorer Pro will disconnect from the wireless network before attempting to use monitor mode and reconnect when the scan is stopped or the user switches to active scan mode.

Once the adapter is in monitor mode, WiFi Explorer Pro uses a user-level packet capture library called [_libpcap_](http://www.tcpdump.org/) (the same library that [Wireshark](https://www.wireshark.org/) and [Airtool](https://www.intuitibits.com/products/airtool) use for packet capturing) to setup the adapter and start capturing only beacon and probe response frames received by the adapter. As part of this setup, the link-layer header type of the adapter is set to [Radiotap](http://www.radiotap.org/). Radiotap is the mechanism by which the driver can supply additional information that is not part of the data found in the beacon or probe response frames. You can learn more about link-layer header types in this [blog post](https://www.intuitibits.com/blog/link-layer-header-types).

![](https://intuitibits.com/wp-content/uploads/2020/06/wifiexplorer-scan-mode-passive-800x547.png)

Radiotap defines many fields, but not all of them are always included in the Radiotap header. However, when doing passive scanning, WiFi Explorer Pro expects to find these fields in particular:

-   **Channel:** frequency on which the frame was received.
-   **Antenna signal:** RF signal power at the antenna when the frame was received.
-   **Antenna noise:** RF noise power at the antenna when the frame was received.
-   **Flags:** whether the frame includes the FCS (Frame Check Sequence) or using a short preamble.

Simultaneous to the packet capture, WiFi Explorer Pro hops (in order) between all the supported channels in the 2.4 and 5 GHz bands using CoreWLAN. The time period WiFi Explorer Pro listens for beacons or probe responses (dwell time) on a given channel is 120 milliseconds but it is reduced to 60 milliseconds if WiFi Explorer Pro did not detect any 802.11 activity in the channel during the last scan. In the worst case scenario (where there is activity on every channel), a passive scan will take approximately 8 seconds. The elapsed time is the result of adding the time WiFi Explorer Pro listens on each channel plus the time that it takes to switch from one channel to the next one.

Since it is possible to receive multiple beacon frames from the same network during the dwell time, WiFi Explorer Pro will only include in the scan results the last frame received and the maximum value seen for signal strength and noise during the dwell time for that particular network. Also note that it is possible to find hidden networks using passive scan mode because these networks still have to transmit beacons the same way non-hidden networks do. The only difference is that the SSID Information Element in the beacon of a hidden network does not contain a value for the SSID. Hidden networks will appear in WiFi Explorer Pro with the name _<Hidden Network>_.

![](https://intuitibits.com/wp-content/uploads/2020/06/hidden_networks.png)

When the scan finishes, WiFi Explorer Pro parses each frame and builds the same dictionaries that CoreWLAN uses for returning the scan results so that they can be used in the same way by the code that populates the network list and creates the different views and charts.

#### **Directed scan mode**

Directed scan mode is just a type of active scanning where the probe request frame includes the name of the target network. This mode allows you to scan for a specific hidden network (or any network for that matter) while associated to an access point if you know the name of the network. The mechanism to perform the scan and to process the results is exactly the same as in the active scan mode. Directed scan mode also uses the CoreWLAN system framework.

![](https://intuitibits.com/wp-content/uploads/2020/06/wifiexplorer-scan-mode-directed.png)

### **Summary**

WiFi Explorer Pro offers three main scan modes: _active_, _passive_ and _directed_. Active scan mode is the default mode. It uses CoreWLAN to perform active scans by sending probe requests and listening for probe responses from the access point in range of the adapter. Active scan mode can be used while associated to a network but it will not provide any information about hidden networks (networks that do not broadcast their SSID). It also has a shorter scan range because client devices usually transmit at lower power levels so access points located farther away cannot decode the probe requests and will not send a probe response to the client.

Passive scan mode uses a combination of CoreWLAN and _libpcap_ to perform passive scanning by putting the built-in Wi-Fi adapter in monitor mode and listening for beacon and probe response frames from nearby access points while hopping between supported channels. Radiotap headers are used to supply additional information not found in the beacon or probe response frame such as signal strength and noise values. Passive scan mode cannot be used while associated to a network but it will find hidden networks. It also has a larger scan range because access points normally transmit using higher power levels so beacons can reach the client device even if the access point is located farther way.

Directed scan mode is just a variation of the active scan mode in which the scan targets a specific network. It can be used to find hidden networks while associated to an access point.