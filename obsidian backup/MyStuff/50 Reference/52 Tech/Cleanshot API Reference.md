# URL scheme API

Our macOS app exposes actions that lets pro users and developers of other apps send commands to CleanShot. This page explains how it works.

## Overview

URL scheme is a special type of link that works just like a normal https:// link you use every day. Instead of opening a webpage, it performs a specific action in the CleanShot macOS app.

Commands are sent to CleanShot by constructing a special URL:

`cleanshot://command-name?parameter1=value1&parameter2=value2`

Opening these links will launch the app and execute the command. For example, here's how you would tell CleanShot to take a fullscreen screenshot:

`cleanshot://capture-fullscreen`

## ✨  All-In-One mode

### /all-in-one

Launch the "All-In-One" mode.

Example:

`cleanshot://all-in-one`

Requires CleanShot 4.2 or later.

## 📸  Screenshots

### /capture-area

Opens the standard "Capture Area" mode. You can also provide the optional parameters and capture the screen instantly. Point (0,0) is located in the lower left corner of the screen.

Parameters:

-   x (optional)
-   y (optional)
-   width (optional)
-   height (optional)
-   display (optional) - Capture a specified display: 1 is the main display, 2 is the secondary, etc. If not specified, CleanShot will use the display which the cursor is on

Example:

`cleanshot://capture-area`

or

`cleanshot://capture-area?x=100&y=120&width=200&height=150&display=1`

Requires CleanShot 3.5.1 or later.

### /capture-previous-area

Repeats last taken screenshot.

Example:

`cleanshot://capture-previous-area`

Requires CleanShot 3.5.1 or later.

### /capture-fullscreen

Takes a fullscreen screenshot.

Example:

`cleanshot://capture-fullscreen`

Requires CleanShot 3.5.1 or later.

### /capture-window

Opens "Capture Window" mode.

Example:

`cleanshot://capture-window`

Requires CleanShot 3.5.1 or later.

### /self-timer

Opens "Capture Area" mode with self-timer.

Example:

`cleanshot://self-timer`

Requires CleanShot 3.5.1 or later.

### /scrolling-capture

Opens "Scrolling Capture" mode.

Example:

`cleanshot://scrolling-capture`

Requires CleanShot 3.5.1 or later.

### /pin

Opens the specified file as a pinned screenshot.

Parameters:

-   filepath (optional) - path to the file (PNG/JPEG) you want to pin. If you don’t pass this parameter, CleanShot will ask to select the file manually.

Example:

`cleanshot://pin`

or

`cleanshot://pin?filepath=/Users/john/Desktop/my%20screenshot.png`

Requires CleanShot 3.5.1 or later.

## 🎥  Screen Recording

### /record-screen

Opens "Record Screen" mode.

Example:

`cleanshot://record-screen`

Requires CleanShot 3.5.1 or later.

## 📖  Text Recognition

### /capture-text

Opens Text Recognition (OCR) tool or extracts text from the specified file. You can also provide the optional parameters (x, y, width, height, display) and capture the text from a specified area on screen. Point (0,0) is located in the lower left corner of the screen.

Parameters:

-   filepath (optional) - path to the image file (PNG/JPEG) that contains the text you want to extract.
-   x (optional)
-   y (optional)
-   width (optional)
-   height (optional)
-   display (optional) - Capture a specified display: 1 is the main display, 2 is the secondary, etc. If not specified, CleanShot will use the display which the cursor is on
-   linebreaks (optional) - Keep (true) or remove (false) line breaks from copied text

Example:

`cleanshot://capture-text`

or

`cleanshot://capture-text?filepath=/Users/john/Desktop/my%20screenshot.png`

or

`cleanshot://capture-text?x=100&y=120&width=200&height=150&display=1`

Requires CleanShot 3.8.1 and macOS 10.15 or later.

## ✏️  Annotate

### /open-annotate

Opens specified file in Annotate.

Parameters:

-   filepath (optional) - path to the image (PNG/JPEG) you want to open. If you don’t pass this parameter, CleanShot will ask to select the file manually.

Example:

`cleanshot://open-annotate`

or

`cleanshot://open-annotate?filepath=/Users/john/Desktop/my%20screenshot.png`

Requires CleanShot 3.8.1 or later.

### /open-from-clipboard

Opens the image from clipboard in Annotate.

Example:

`cleanshot://open-from-clipboard`

Requires CleanShot 3.5.1 or later.

## 🖥  Desktop icons

### /toggle-desktop-icons

Toggles Desktop icons visiblity.

Example:

`cleanshot://toggle-desktop-icons`

Requires CleanShot 3.5.1 or later.

### /hide-desktop-icons

Hides Desktop icons.

Example:

`cleanshot://hide-desktop-icons`

Requires CleanShot 3.8.1 or later.

### /show-desktop-icons

Shows Desktop icons.

Example:

`cleanshot://show-desktop-icons`

Requires CleanShot 3.8.1 or later.

## ⚡️  Quick Access Overlay

### /add-quick-access-overlay

Opens a new Quick Access Overlay with the specified image or video.

Parameters:

-   filepath (required) - path to the image or video (PNG/JPEG/MP4) you want to open.

Example:

`cleanshot://add-quick-access-overlay?filepath=/Users/john/Desktop/my%20screenshot.png`

Requires CleanShot 3.8.1 or later.

## ⏳  History management

### /open-history

Opens capture history.

Example:

`cleanshot://open-history`

Requires CleanShot 4.4 or later.

### /restore-recently-closed

Restores the most recently closed file from history.

Example:

`cleanshot://restore-recently-closed`

Requires CleanShot 3.5.1 or later.