[[ReadItLater]] [[Article]]

# [New Obsidian Notes from Drafts](https://www.thoughtasylum.com/2022/12/29/new-obsidian-notes-from-drafts/)

29 Dec 2022

Yesterday I posted some details around [using Shortcuts to send a new note to Obsidian](https://www.thoughtasylum.com/2022/12/28/new-obsidian-notes-from-shortcuts/). Today, I’m going to look at a different and also popular capture option for [Obsidian](https://obsidian.md/); using one of my favourite applications, [Drafts](https://getdrafts.com/).

## The Approaches

In the post about Shortcuts, I utilised two different approaches. One using an x-callback-url, and one writing content direct to the file system. I am going to adopt the same approaches using Drafts.

While I could utilise a Shortcut to do these things on Drafts behalf, Drafts is more than capable of carrying out these actions natively, which speeds things up.

Because the approaches are the same, the pros and cons are very similar, so if you want to understand what the benefits and constraints are for each approach, I would recommend taking a look at [the previous post](https://www.thoughtasylum.com/2022/12/28/new-obsidian-notes-from-shortcuts/).

## Building a Drafts Action for Creating an Obsidian Note via URL Scheme

While I could have built a script step to more accurately reproduce all the options in the equivalent shortcut, I have opted to keep things simpler and use just a few of the other standard action steps to illustrate how it works. This makes both actions simpler in terms of having fewer steps, but a slightly deeper understanding of what is going on - particularly with adding parameters to the URL, but I do include an example of that.

The URL-based action ([download it here](https://directory.getdrafts.com/a/2F1)) consists of two action steps. While it could be simplified down to one, I thought I’d show a way you can typically make these sorts of actions a little easier to maintain.

The first step is the definition of a *Drafts Template Tag* that is used to define the name of the vault that has been registered in Obsidian. Here, the vault is called “obsidian vault”, and it is assigned to the template tag called `vault`.

![](New%20Obsidian%20Notes%20from%20Drafts-LITaXwqw3d.png)

The second action step is a callback URL step. This is what opens the URL and that is returned to when Obsidian executes the URL request.

![](New%20Obsidian%20Notes%20from%20Drafts-U3OF8xWeBp.png)

The URL includes several parameters. `vault` is the name of the Obsidian vault and is set to the template tag we defined in the previous step. `name` we set to the standard Drafts template tag, `safe_title`. This is equivalent to the first line of the draft, but with some text transformations carried out to make it a valid name for a file. `content` specifies the content of the new Obsidian note, and is specified as another standard Drafts template tag, `body`. This will set the note content to be the second line onwards of the draft. Finally, I also added the optional `silent` parameter. This parameter takes no value, and when included in the URL, it instructs Obsidian not to load the new note.

A key point to note about this step is the *URL encode tags* option is checked. This ensures that the content being passed to the URL via the tags is correctly encoded for inclusion in the URL.

I used the following Draft content as a simple test case for the action.

```
# New Note
The content of my note
```

When run, Obsidian is activated, and the new note is created (but not automatically loaded thanks to the `silent` parameter), and the following message is displayed.

![](New%20Obsidian%20Notes%20from%20Drafts-XaEoUqdkdD.png)

This is the same as for Shortcuts, and it just Obsidian doing a security check to confirm that you are happy for it to trigger the URL displayed. This is the callback URL to go back to Drafts. Just like for Shortcuts, it is passing back information about the new note (but we won’t do anything with that information, and since we haven’t specified to *Wait for response* in the callback-URL step, Drafts isn’t even going to wait on any data coming back), and you can check the box at the bottom to stop it prompting you in the future.

When the URL is opened, you are returned to Drafts, and the action completes. The new note has been created, and is accessible in the Obsidian vault.

## Building a Drafts Action for Creating an Obsidian Note by Directly Writing a File

The file-based action ([download it here](https://directory.getdrafts.com/a/2F2)) is once again very simple. In fact it has a strong parallel to the URL-based action. This time however, rather than specifying the vault name via a Drafts template tag, we are specifying the Drafts vault location (for new files) as a [Drafts folder bookmark](https://docs.getdrafts.com/docs/settings/bookmarks.html).

The action utilises a single *File* step that once again uses the `safe_title` template tag for the file name (with an explicit `.md` file extension this time), and the `body` template tag for the content of the draft.

![](New%20Obsidian%20Notes%20from%20Drafts-W7KhXJoYNR.png)

The action is set to reference a folder bookmark called `obsidian vault`. If this bookmark has not been created previously, then when run the action will display the following message.

![](New%20Obsidian%20Notes%20from%20Drafts-a3qMNppasu.png)

Selecting OK, you will be able to then select a folder to associate with the bookmark.

![](New%20Obsidian%20Notes%20from%20Drafts-f7ct5k2Ymg.png)

> Note, bookmarks are device specific, so you will be prompted on each device when this is run - the bookmarks cannot sync across devices.

When the action execution completes, the Markdown file will be created in the specified (bookmarked) folder.

## Summary

Once again, like for Shortcuts, I generally take the approach of writing directly to file. This avoids the switching out to Obsidian, and just feels seamless to me.

Because I use Drafts as my initial point of capture for bits and pieces of information, I do find myself utilising Drafts as a capture mechanism for Obsidian more often than Shortcuts. I actually use Shortcuts more often to capture into Drafts as Drafts is my central point of triage for information from which I can refine it and then route it out to other applications, such as Obsidian.

I hope the examples above will be useful to you in creating your own Obsidian capture solutions using Drafts, and do let me know if these have helped.