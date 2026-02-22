---
category: "[[Clippings]]"
author: "[[Econ Technologies, Inc.]]"
title: Network Connections | Econ Technologies, Inc.
source: https://www.econtechnologies.com/chronosync/guide-network-connections.html
clipped: 2024-04-08
published:
topics:
tags:
  - clippings
---

This guide explains the various methods used to connect a ChronoSync Mac to another Mac, a file server or a Network Attached Storage (NAS) device on a local area network (LAN). Once you have connected, you can access drives and folders on the remote device as long as they have been made accessible. You can then configure ChronoSync to automatically connect to and run a synchronization or backup when the remote device is available on the network.

If you are trying to synchronize or backup between two Macs, you only need to install ChronoSync on one of them. The other Mac can be accessed using built-in file sharing. If you want to realize the maximum potential of your connection, however, consider installing ChronoAgent on the other Mac. ChronoAgent synchronizes files faster, encrypts file transfers, and provides full administrative access to the Mac it is installed on.

If you are trying to synchronize or backup between a Mac and a file server, or NAS device, you still only need to install ChronoSync on the Mac. The other device will be accessed using using built-in file sharing.

In order for a Mac to communicate with another Mac, file server or NAS (collectively referred to as devices), a network connection is required to transfer data between the devices. While there are several forms of networking available, the two most likely candidates that you will be using are a wireless (Wi-Fi) or wired Ethernet network.

One of the most common networking methods for Macs utilizes wireless ethernet. This involves a simple connection to your AirPort base station or other Wi-Fi access point (commonly known as a hot spot) to join the network. You most likely have already joined a wireless network for the sake of accessing the internet, in which case no further steps are necessary and you may proceed to the PREPARING FOR SHARING section of this guide.

If you need to configure a Wi-Fi network connection, however, open the “System Preferences” app from the Apple Menu on your Mac. Click on the “Network” panel then click the padlock icon at the lower left. Enter your administrator credentials to allow you to make changes. You should then select “Wi-Fi” in the network connection services list and make sure that Wi-Fi is ON.

![network connection](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect1x2.png?fit=1268%2C1069&ssl=1)

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect2x2.png?fit=855%2C452&ssl=1)

Next you will need to click on the “Network Name” popup menu and choose the wireless network connection that you’d like to join. Multiple network names may appear if there are other wireless networks operating in the immediate vicinity. Make sure you choose the correct one. Unless the network you choose is open and unprotected, you will then have to supply a password to join it.

Hopefully you know the password to supply. If not, contact the person responsible for the wireless network and ask them — we can’t help you with this!

Once you have joined a wireless network, the wireless status indicator in your menubar should show one or more solid bars, indicating that you are connected and the signal strength of the connection.

Note that if you are configuring a Mac-to-Mac network connection, you need to follow these steps on both Macs to ensure they have connected to the same wireless network.

Now scroll down to the PREPARING FOR SHARING section of this guide to learn how to prepare to transfer files over this connection.

Most Macs have an Ethernet port available, or you can obtain a Thunderbolt-Ethernet adapter. Wired Ethernet provides much faster file transfers than Wi-Fi. Simply connect your Ethernet cable to the port on your Mac to an available port on a central router or switch device. The Mac should automatically recognize the connection.

To confirm that your Ethernet connection is working, open the “System Preferences” app from the Apple Menu on the Mac. Click on the “Network” panel and inspect the network connection services list. There should be one or more “Ethernet” services listed and one of them should have a green indicator along with a “Connected” status. You can select this entry to obtain more details about the Ethernet connection such as the assigned IP address and the router address.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect4x2.png?fit=1259%2C1057&ssl=1)

Note that if you are configuring a Mac-to-Mac network connection, you need to plug in your Ethernet cable and confirm connections on both Macs. Once this is done, go to the next section (PREPARING FOR SHARING) to learn how to prepare to transfer files over this connection.

Now that you have gotten your Mac(s) on the network, the next step is to actually share files. This, in turn, will allow you to configure a ChronoSync task to synchronize or backup files between the two computers, a file server or an NAS device. To do this you may need to perform some preparation on the computer or device that ChronoSync will be connecting to. The exact steps to take will vary depending on what file transfer protocol you wish to use and/or what type of device you will be transferring files with. This section will guide you through that process — or at least provide hints on what you may need to do to get things going.

If you will be transferring files between two Macs — even if the destination Mac is a file server — you should seriously consider using ChronoAgent. ChronoAgent is a background utility you install on the remote Mac (the one that is not running ChronoSync) that allows you to transfer files faster, more reliably and more securely than any other method. Yes, it is an extra purchase in addition to ChronoSync, but the benefits are well worth it.

Once ChronoAgent is installed on your destination Mac, open the “System Preferences” app from the Apple Menu on the ChronoAgent Mac. Click on the “ChronoAgent” panel and then click the padlock icon at the lower left. Enter your administrator credentials to allow you to make changes. Then click on ChronoAgent’s “General” panel.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect5x2.png?fit=1268%2C1088&ssl=1)

In the “Identify agent with name” field, enter a unique name for this agent. This will be broadcast on the network using the Bonjour service discovery protocol and will be used to identify this specific instance of ChronoAgent. Choose as descriptive of a name as necessary since there may be multiple agents on the network. Next, supply a user name and password. These are the credentials that will be necessary to connect to this agent.

While there certainly are many additional options that can be configured, this is all that is really necessary to get started. You can leave all other settings at their defaults. You can always come back and explore the additional options later. So, for now, go ahead and start ChronoAgent by turning it ON. That’s it! Your agent is now running and is ready to receive incoming connections from other ChronoSync Macs on your network. It may even receive incoming connections from iPads and iPhones running InterConneX!

You may now proceed to the MAKING THE CONNECTION section, later in this guide, to learn how.

If you will be transferring files between two Macs and decide not to use ChronoAgent, the built in file sharing service offered by macOS is your next logical choice. The following steps explain how to enable file sharing on one computer and then access that computer from another Mac. You will typically enable file sharing on a central computer that multiple Macs will be accessing.

You begin by enabling file sharing on a Mac that is not running ChronoSync. Open the “System Preferences” app from the Apple Menu. Click on the “Sharing” panel and then click the padlock icon at the lower left. Enter your administrator credentials to allow you to make changes.

While you have the “Sharing” panel open, take the time to make sure that your computer has a name. Most of the time, this has already been set for you. Sometimes, however, it is blank — and that can cause problems!

In the list of services on the left you should enable the “File Sharing” option. After doing so, this computer may now be reached by other Macs on the network. You can choose to setup specific folders that act as share points, but you really don’t need to do so as long as you use your administrator name and password when connecting from the other Mac. This will provide access to the root hard drive.

At this time you should make a note of the IP address presented near the center of the window. You typically will connect by computer name, but sometimes you’ll need to specify an IP address. After doing so, proceed to the MAKING THE CONNECTION section, later in this guide, to learn how to connect to this computer from other Macs.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect6x2.png?fit=1268%2C1008&ssl=1)

Preparing a file server to accept inbound connections is beyond the scope of this guide. There are simply too many different types of file servers to document (macOS Server, Windows Server, linux servers, etc.) Configuring a server can be quite complex and should be performed by someone with knowledge and experience in that area. Ultimately, however, a username and password will be created that are the credentials necessary to logon to that server. Once this information is obtained, you can proceed to the MAKING THE CONNECTION section, later in this guide, to learn how to connect to this server from Macs on your network. The process will be nearly identical to connecting with other Macs via built-in file sharing.

Preparing an NAS device to accept inbound connections is beyond the scope of this guide. Like file servers, there are simply too many different types of NAS devices to document here. Luckily, configuring an NAS is generally not as difficult as a full-blown file server. The various manufacturers do a good job of getting you up and running quickly. Like with file servers, ultimately, a username and password will be created that are the credentials necessary to logon to the NAS device. Once this information is obtained, you can proceed to the MAKING THE CONNECTION section, later in this guide, to learn how to connect to this NAS from Macs on your network. The process will be nearly identical to connecting with other Macs via built-in file sharing.

Now that you’ve joined the network and have prepped the service you will be communicating to (ChronoAgent, File Sharing, File Server or NAS Device), it’s time to complete the network connection. In all cases you need to log on to the service you are communicating with from a Mac running ChronoSync. The only factor that determines how you will do this depends on whether or not you are communicating with a ChronoAgent or one of the other services — logging on to another Mac via file sharing, a file server or an NAS device are virtually identical to each other.

### Connecting to a ChronoAgent

ChronoAgent is by far the most efficient, reliable and secure way to connect to a remote Mac. Once ChronoAgent is configured on the remote Mac, you connect to it within ChronoSync by creating a connection profile. With a synchronizer task open and the “Setup” panel selected, click on the “Connect to” popup menu and choose “Create connection…”.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect7x2.png?fit=663%2C526&ssl=1)

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect8x2.png?fit=1178%2C933&ssl=1)

After choosing this, the “Connections” preference pane will appear. Give the profile a meaningful name in the “Unique Profile Name” field. Then choose “ChronoAgent” as your “Connection Type.”

The rest of the panel will show. Choose the remote ChronoAgent in the “Connect to” popup. Supply your credentials and then click “Test…”. If all goes well, your connection profile will be confirmed. While there certainly are more configuration options you may choose, for this example just click “Next” until the profile is saved. For information on all the additional options available to you you when configuring a connection profile, see our Configuring Connection Profiles guide.

At this point, your newly created connection profile should appear in the “Connect to” popup button for your target. It will be available for all future tasks that you may create so you won’t have to go through the connection profile creation process again.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect9x2.png?fit=663%2C544&ssl=1)

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect10x2.png?fit=1268%2C880&ssl=1)

When you select the profile, a connection is made to your ChronoAgent. You are now ready to continue configuring a ChronoSync synchronization or backup operation. Selecting a target folder on the remote Mac is a simple as clicking “Choose…” and then navigating to the desired drive and folder.

Note that with ChronoAgent, you have full access to the remote machine — you don’t get that with built-in file sharing!

That’s it! You have now completed a network connection and data transfer between two Macs using ChronoSync + ChronoAgent!

### Connecting to Another Mac, File Server or NAS Device

The following steps show how you would connect to a macOS server or another Mac via file sharing. Non-Mac servers and NAS devices will be very similar, however.

On a Mac computer that is running ChronoSync, open a new Finder window and look in the sidebar on the left. You may have to scroll down a bit until you see the “SHARED” group. In that group you should see the name of the Mac computer, file server or NAS device you are trying to connect to, as long as the device is using a service discovery protocol to broadcast its availability. If you see the device name, click on it and then click the “Connect As…” button.

You will be asked to authenticate as a user. If you are connecting to another Mac, you may use the administrator credentials from that Mac, provided the owner of that computer allows it! Otherwise, you must use a username and password that the Mac’s owner provides you. The same goes for connecting to a file server — you must use a username and password provided by the server’s administrator. In the case of an NAS device, you still need a username and password but you are likely the one who configured the NAS, so this information should be readily accessible.

If you enable the “Remember this password in my keychain” option, your credentials will be saved and you won’t have to specify them again in order to connect to the remote device. This is generally what you want if you are the sole user of your Mac. It will allow you to access the remote device’s files from within ChronoSync and other apps (such as Finder), too, without having to frequently enter your password to connect. If you’re concerned about security, however, leave this option unchecked. You will be prompted for a password every time you try to gain access. See TIGHTER SECURITY, later in this guide, for some tips on how you can get ChronoSync to have automatic access by pre-specifying a username and password in your task.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect11x2.png?fit=1268%2C871&ssl=1)

If you did not see the device name you want to connect to in the SHARED group (or you didn’t see the SHARED group at all), you will have to connect by IP address. This will likely be the case if the device you are connecting to does not use a discovery protocol to broadcast its availability on the network. The IP address of the device should have been made available to you when you were configuring the device. If the device is a Mac, this was displayed when you were enabling file sharing (and that we suggested you make a note of).

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect12x2.png?fit=994%2C929&ssl=1)

Type in the IP address of the other computer that you are trying to connect to and then click “Connect”. If all goes well, you’ll be presented with the authentication dialog.

You will be asked to authenticate with a username and password. As in the case of connecting to a named device, above, you can choose to add your credentials to the keychain and avoid having to re-enter them in the future. Otherwise, leave “Remember this password in my keychain” unchecked and you will be required to authenticate each time you connect.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect13x2.png?fit=817%2C538&ssl=1)

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect14x2.png?fit=1072%2C1034&ssl=1)

At this point, whether you simply clicked on the device name in the SHARED group of the Finder sidebar, or you had to connect via COMMAND-K, a file sharing connection should have been established with the other device. A Finder window will open showing the file system hierarchy of the device you are connected to.

When you click on one of the drives being shared by the remote device, it becomes mounted on your Mac. You may now navigate through the folders as if they were stored on your own computer. You are now ready to configure a ChronoSync synchronization or backup operation. First, make sure your Target ‘Connect to:’ popup is set to ‘Mounted Volumes’. File sharing connections don’t allow ‘Mounted Volumes(Admin Access)’. Then, selecting the target folder on the remote Mac is a simple as clicking “Choose”, selecting the computer name from the sidebar, and then navigating to the desired folder. You can also Drag & Drop the desired folder from a Finder Window into the Target Pane.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect15x2.png?fit=1268%2C619&ssl=1)

When you are finished with the connection, click on the eject icon that appears next to the device’s name in the Finder sidebar.

That’s it! You have now completed a network connection and data transfer between a Mac and a remote device using ChronoSync!

As mentioned above when authenticating, you have the option of adding your username and password to your keychain to prevent having to re-specify them each time you want to connect to the remote device. You generally want to do this for convenience sake but sometimes you may not want to. For instance, you may not be the sole user of your computer and/or you may step away from your Mac from time to time. In such cases, you may not want just anyone to sit down at your machine and connect to another computer, file server or NAS that contains sensitive information. In these instances, you would normally leave your remote device unmounted and require a username and password each time you access them.

This is all well and good but what about ChronoSync? If you schedule a task, you probably don’t want to be prompted for the username and password just so the sync or backup can be completed. You might not even be sitting at the computer when the task runs!

To accommodate such scenarios, ChronoSync offers the ability to record your username and password within the synchronizer task. This allows ChronoSync to connect to your remote device automatically. To do this, specify your remote target just like you normally would and then click “Options.”

A drop-down sheet appears allowing you to configure custom options for the target, among which is the ability to specify a username and password. You may also want to enable the “Dismount server after synchronization” option so that disks on the remote device do not remain mounted after the task runs. Note: if you’re connecting via ChronoAgent, the username and password do not appear — those settings are specified in your connection profile.

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect17x2.png?fit=519%2C458&ssl=1)

![](https://i0.wp.com/www.econtechnologies.com/wp-content/uploads/2019/10/tip-network-connect18x2.png?fit=815%2C422&ssl=1)

For added security, you may want to password protect your task. These tasks will still run automatically when scheduled but will require a password if a user attempts to open them. To do this, choose “Access Restriction…” from the “File” menu when the task in question is open.

Adding password protection will close the loophole whereby a user simply needs to open a task in order to gain access to sensitive files on a remote device.

For most people, the above steps will work flawlessly for establishing a connection and transferring your data. However, we live in an imperfect world and sometimes things just don’t work out as expected. If you encounter any problems following this tutorial, here’s some tips that may help you get back on track:

From the “Help” menu in Finder, you can try some of the following search terms (minus the quotes):

-   “Connect two computers using Ethernet”
-   “Connect your Mac directly to a Windows computer”
-   “Set up a network connection service”
-   “Use a network hub, router, or switch”