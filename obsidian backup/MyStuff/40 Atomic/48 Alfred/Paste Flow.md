# PASTEFLOW

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#pasteflow)

**A Paste Stack & Paste Queue for Alfred | Pin & Reuse Text**

[![](https://github.com/ognistik/alfred-pasteflow/raw/main/Workflow/assets/images/pasteflow.png)](https://youtu.be/2TWJGcTVy3A)

_[~ Video Overview & Setup ~](https://youtu.be/2TWJGcTVy3A)_

## WHAT IS PASTEFLOW?

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#what-is-pasteflow)

PasteFlow is a handy paste stack (or paste queue) for [Alfred](https://alfredapp.com/). It lets you create a list of pinned text items that you can organize, edit, and use in different ways.

Ever needed to copy text from various places and put it all in one final spot? PasteFlow makes this easy. No more switching back and forth to copy and paste one item at a time. Save time and stay _in flow_ by doing all your copying first, then pasting later when you're ready. Since your items are saved in an actual list, you can even take a break, copy other things, and come back to your stack whenever you want.

Thanks to Alfred's triggers, clipboard features, and actions, PasteFlow is a flexible tool that can boost your productivity when working with text.

---

## REQUIREMENTS

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#requirements)

- This workflow uses Alfred’s Clipboard History. You do not need to use Alfred as your main clipboard manager, but you must have this feature activated.
    
- This workflow utilizes Python 3 to filter its menus. If you don't have it, it may prompt you to install Xcode Command Line Tools for this, or you can install it by running `xcode-select --install` in Terminal. Python is a widely used programming language recognized for its safety and reliability, commonly utilized in Alfred workflows, Homebrew, and more.
    

---

## HOW TO USE PASTEFLOW?

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#how-to-use-pasteflow)

If you're already familiar with paste stacks, you can start using PasteFlow right away with its default settings. Here's how to get started:

1. **Add items to your stack:**
    
    - Select text and use Pasteflow actions on them.
    - Set up your preferred hotkeys (green color-coded hotkeys are the most basic/essential).
    - Use PasteFlow's keyword to add items from your Clipboard to your stack.
2. **Process your saved items:** The easiest way to do this is to set up a hotkey (in green), but you can also use PasteFlow's keyword directly on Alfred's bar.
    
    - Paste items to your current window
    - Copy items back to your clipboard
3. **View & edit your stack:**
    
    - Set up hotkeys (red-coded hotkeys show your entire list)
    - Enter "Selective Mode" from Alfred's Bar using PasteFlow's keyword
    - Use Textview Mode (type `:View` with PasteFlow's keyword)

That's all you need to get started! But if you want to explore more, PasteFlow has lots of other useful and powerful features.

[![](https://github.com/ognistik/alfred-pasteflow/raw/main/Workflow/assets/images/001.jpg)](https://github.com/ognistik/alfred-pasteflow/blob/main/Workflow/assets/images/001.jpg)

---

## FEATURES

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#features)

### Configuration

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#configuration)

PasteFlow is flexible and adapts to your workflow. Here's how you can set it up:

- **Stack or Queue**: Choose how new items are added - at the top (stack) or bottom (queue). [_**Read more about the sorting logic.**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-sorting-logic)
- **Processing Order**: Pick where to start processing items - from the top or bottom. It's all about what feels right for you.
- **Selective Processing**: This setting allows for advanced workflows when inserting or processing individual list items. It works together with your chosen processing order. [_**Read more about the insertion & processing logic.**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-processing-logic)
- **Auto-Clear Options**: Decide if you want items cleared after processing. You can set this for individual items or the entire list when processed at once. [_**Read more about ways to clear your items.**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#clearing-items)
- **Restart or Stop**: Choose whether to restart processing when you reach the end of your list, or simply stop until you add more items.
- **Paste Actions**: Optionally, add a line break, comma, space, or press tab after each pasted item from your list.
- **Merge Formatting**: When processing your entire list at once, choose to merge items with line breaks, commas, or spaces.
- **List Lifespan**: Use PasteFlow as a temporary list with a timeout, or keep it indefinitely. For long-term lists, there's a custom save directory.

### In Action

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#in-action)

PasteFlow is packed with features to make your workflow smoother:

- **Large Text View**: In the main menu, press CMD L on any item to see your list in large text. You can also copy it (CMD C) or use Alfred's universal actions on it.
- **Selective Mode Viewing**: In Selective Mode, CMD L shows the full content of an item. Copy or use universal actions here too.
- **Hidden Menu**: Type `:` in Alfred's bar (with PasteFlow's keyword) to reveal extra options like inverting your list order, clearing it, or editing all its raw contents. Many of these are also directly available in Textview Mode (`:View`). [_**Read all about the main menu.**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-main-menu)
- **Powerful Selective Mode**: Edit individual items, move them around, remove them, or process them in any order. Some modifier combos let you tweak the whole list without entering Textview Mode. [_**Read all about Selective Mode.**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#selective-mode)
- **Multi-line Splitting**: Select a multi-line text and automatically split it into individual PasteFlow items. [_**Read all about Universal Actions**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#universal-actions)
- **Multiple Control Methods**: Use Alfred's bar directly, keyboard shortcuts ([color-coded for easy remembering](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#custom-hotkeys)), or send arguments to the external trigger. [_**Read all about the external trigger.**_](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-external-trigger)

PasteFlow is designed to be a flexible & powerful clipboard companion. Whether you're a pro or just getting started with paste stacks and clipboard managers, it's here to make your copy/paste tasks more efficient. Feel free to read below for more detailed information on all the features, and do not forget to [check out some tips and ideas that you may also find useful.](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#closing--tips)

[![](https://github.com/ognistik/alfred-pasteflow/raw/main/Workflow/assets/images/002.jpg)](https://github.com/ognistik/alfred-pasteflow/blob/main/Workflow/assets/images/002.jpg)

---

## CLEARING ITEMS

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#clearing-items)

You can use PasteFlow as a temporary text holder or a more permanent list. Here's how you can clear items from it:

**👇️ Auto-Clearing the List****👇️ Manually Clearing the List**

---

## THE MAIN MENU

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-main-menu)

The main menu is your control center for PasteFlow. Here's some things you can do without even actioning any menu option:

- See your list in large text with CMD L
- Copy your entire list at once with CMD C
- Use Alfred's Universal Actions on your full list

_Note: Pasteflow's menus are populated dynamically. For example, you won't see some processing options if your list is empty, the "Next Item" processing option won't be available if all items have been processed and the list isn't set to restart, or you will not have the "insert in next position" modifier [if it makes no difference](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#advanced-insertion-and-processing)..._

**👇️ Main Menu Options and Modifiers**

There's also a "secret" menu with extra options for your entire list. Just type `:` to access it. These actions are straightforward and don't have modifier combinations.

**👇️ The "Secret" Menu Options:**

PasteFlow's main menu is designed to give you quick access to all the tools you need. Whether you're adding items, processing them, or managing your list, everything is just a few keystrokes away!

---

## SELECTIVE MODE

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#selective-mode)

Selective mode gives you a hands-on experience with your PasteFlow list. It's like having a traditional paste stack/queue at your fingertips, where you can shuffle items around, make edits, or process them in any order you like.

If you've set PasteFlow to keep processed items, you'll have some visual cues on the icons that show which item is next in line (an icon with red) and which have already been processed (icons with transparency).

[![](https://github.com/ognistik/alfred-pasteflow/raw/main/Workflow/assets/images/004.jpg)](https://github.com/ognistik/alfred-pasteflow/blob/main/Workflow/assets/images/004.jpg)

Just like in the main menu, Selective Mode lets you do a few things with each item:

- See the item in large text with CMD L
- Copy the item with CMD C
- Use Alfred's Universal Actions on any item

**👇️ Modifier Keys for Item Management****👇️ Advanced Modifier Combos**

Selective Mode puts you in control. It's designed to be intuitive and powerful, giving you the flexibility to work with your list exactly the way you want.

---

## CUSTOM HOTKEYS

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#custom-hotkeys)

**👇️ The hotkeys have been color-coded to make setup easier for you.**

If you zoom out in Alfred's workflow editor (CMD + Hyphen), you'll notice the hotkeys are loosely grouped into:

- Insertion actions
- Processing actions
- Full-list actions
- Workflow actions

_Note: PasteFlow offers a lot of processing actions, and when combined with different settings, the preset hotkey list could grow huge. Some features, like inverting inserts or processing, are for more advanced users—so I didn't include those as hotkeys. If you're looking for customization beyond the available hotkeys, I recommend learning to use [the external trigger.](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-external-trigger)_

---

## UNIVERSAL ACTIONS

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#universal-actions)

PasteFlow comes with two powerful universal actions, each with additional modifier options to fine-tune your workflow:

[![](https://github.com/ognistik/alfred-pasteflow/raw/main/Workflow/assets/images/005.jpg)](https://github.com/ognistik/alfred-pasteflow/blob/main/Workflow/assets/images/005.jpg)

### Add to List

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#add-to-list)

This action adds your selected text to your PasteFlow list.

**👇️ Here's what you can do:**

### Split & Add to List

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#split--add-to-list)

This action splits your selected text into separate items and adds them to your list. It's super handy for multi-line text.

**👇️ Here are your options:**

These universal actions give you quick, flexible ways to add content to your PasteFlow list, right from any text you're working with.

---

## THE SORTING LOGIC

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-sorting-logic)

PasteFlow adapts to your preferred way of organizing information. Here's how it works:

- **Stack**: New items go to the top. Think of it like a pile of plates - the last one you add sits on top.
- **Queue**: New items go to the bottom. It's like people lining up - newcomers join at the end.

But what happens when you add multiple items at once? That's where it gets interesting:

- **Clipboard Items**: Most clipboard managers put recent items at the top. If your PasteFlow is set as a queue, it'll flip this order to match your preference.
- **Split Lists**: When you split a text into individual items, PasteFlow considers how we naturally write - top to bottom. For a stack setup, it'll invert this order.

**Want to change things up? You've got options:**

- While in stack, use the OPT modifier in Alfred's action or the main menu to add split list items with the most recent at the bottom. If you are in queue mode, you can use the same to insert your split items most recent at the top.
- The external trigger has a parameter for this too.

Remember, multiple clipboard items follow the stack or queue sorting logic when inserting. Unlike split items, there’s no extra setting to change this. Keep this in mind when choosing between stack and queue for your workflow.

---

## THE PROCESSING LOGIC

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-processing-logic)

Assuming you already have understood the sorting logic, now let me explain you what the processing order does. Here's a simple breakdown:

### Basic Processing

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#basic-processing)

- **Stack (Top-to-Bottom)**: Newest to oldest
- **Stack (Bottom-to-Top)**: Oldest to newest
- **Queue (Top-to-Bottom)**: Oldest to newest
- **Queue (Bottom-to-Top)**: Newest to oldest

For most users, this is all you need to know. However, if you enjoy using Selective Mode and are interested in processing or inserting items not only at the top or bottom but also in the middle of your list, there are ways to do that.

### Advanced Insertion and Processing

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#advanced-insertion-and-processing)

[![](https://github.com/ognistik/alfred-pasteflow/raw/main/Workflow/assets/images/nextItem.jpeg)](https://github.com/ognistik/alfred-pasteflow/blob/main/Workflow/assets/images/nextItem.jpeg)

PasteFlow's Selective Mode and the "Next Item Index" feature work together for more complex list management:

While in Selective Mode, use CMD + SHIFT when selecting an item to set it as the "next item". This item will not be processed and simply change it's icon into a red variation to indicate it is next in line. There's another way you can do this. Processing or clearing an item from anywhere your list will also automatically update the "next item" to be the one **after** the last processed position (you can choose a different setting for this in the configuration). What makes this a bit challenging, is that the "next item" can behave differently depending on your configuration.

**👇️ Let's break down how this works in different scenarios:**

Remember, PasteFlow uses visual cues with icon changes to help you understand the state of your list, even though you can't see it in real-time. Getting familiar with these concepts is not essential, but it allows you to leverage PasteFlow's full potential.

_Important. Note that the actions that modify the contents of your list (most of the options in the "secret" menu) will reset the "Next Item Index" regardless of the "Selective Processing" behavior set in the configuration._

---

## THE EXTERNAL TRIGGER

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#the-external-trigger)

The external trigger in PasteFlow allows you to use every feature without sacrificing a single keyboard shortcut. Whether you're using Keyboard Maestro, BetterTouchTool, or other 3rd party apps, you can trigger PasteFlow actions using AppleScript or Alfred's URL scheme by sending arguments.

The external trigger is `cmd` and can receive 4 arguments, comma-separated (without spaces):

```
theAction,clearList,invertOrder,insertNext
```

Only `theAction` is required.

**👇️ theAction Options**

### Additional Arguments

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#additional-arguments)

**👇️ These arguments need to be `0` for false, or `1` for true:**

Remember the `invertOrder` argument doesn't affect adding a range of clipboard items to your list. It's recommended to set your list behavior to match this and customize the rest as needed.

Here’s how some commands would look in action:

- `c!!addCurrentClip,0,0,1` will copy selected text and force insert it in the “next” position. It’s useful to have as an option if your list behaves as “queue” and you are processing it top-to-bottom.
- `pasteNext,0,1,0` will paste the previous item instead of the next one.
- `c!!addSplitClip,1` will copy selected text, split it by newlines, clear your current list, and insert it the split items in a new one.

---

## Closing & Tips

[](https://github.com/ognistik/alfred-pasteflow/blob/main/README.md#closing--tips)

Phew! Thank you for making it this far. After diving into this project, I've got a whole new respect for clipboard manager developers. Who knew the processing and sorting logic for a simple paste stack would turn into such a beast? But hey, that complexity opened up a world of cool options.

**👇️ Here are some tips/ideas you may find useful:**

Now, I know PasteFlow isn't perfect. You can't see your stack/queue in real-time while processing, and it doesn't keep rich text formatting (that's an Alfred's Clipboard Manager limitation). I know I am biased but I've got to say, I think PasteFlow is pretty good and should hit the spot for most users, whether you're just dipping your toes in or diving into the deep end.

If PasteFlow's making your life easier, how about [buying me a coffee](https://www.buymeacoffee.com/afadingthought)? I'd be over the moon grateful!