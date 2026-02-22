[[ReadItLater]] [[Article]]

# [Symbolic link - Wikipedia](https://en.wikipedia.org/wiki/Symbolic_link)

In [computing](https://en.wikipedia.org/wiki/Computing "Computing"), a **symbolic link** (also **symlink** or **soft link**) is a file whose purpose is to point to a file or directory (called the "target") by specifying a [path](https://en.wikipedia.org/wiki/Path_\(computing\) "Path (computing)") thereto. [1](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-1)

Symbolic links are supported by [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX") and by most [Unix-like](https://en.wikipedia.org/wiki/Unix-like "Unix-like") [operating systems](https://en.wikipedia.org/wiki/Operating_system "Operating system"), such as [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD "FreeBSD"), [Linux](https://en.wikipedia.org/wiki/Linux "Linux"), and [macOS](https://en.wikipedia.org/wiki/MacOS "MacOS"). Limited support also exists in [Windows 7](https://en.wikipedia.org/wiki/Windows_7 "Windows 7") and [Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista "Windows Vista"), and to some degree in [Windows 2000](https://en.wikipedia.org/wiki/Windows_2000 "Windows 2000") and [Windows XP](https://en.wikipedia.org/wiki/Windows_XP "Windows XP") in the form of shortcut files. [CTSS](https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System#File_system "Compatible Time-Sharing System") on [IBM 7090](https://en.wikipedia.org/wiki/IBM_7090 "IBM 7090") had files linked by name in 1963. [2](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-50th-2) [3](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-ctsspg69-3) [4](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-ctsspg63-4) By 1978 minicomputer operating systems from [DEC](https://en.wikipedia.org/wiki/Digital_Equipment_Corporation "Digital Equipment Corporation"), and in Data General's [RDOS](https://en.wikipedia.org/wiki/Data_General_RDOS "Data General RDOS") included symbolic links.

A symbolic link contains a text string that is automatically interpreted and followed by the operating system as a path to another file or directory. This other file or directory is called the "target". The symbolic link is a second file that exists independently of its target. If a symbolic link is deleted, its target remains unaffected. If a symbolic link points to a target, and sometime later that target is moved, renamed or deleted, the symbolic link is not automatically updated or deleted, but continues to exist and still points to the old target, now a non-existing location or file. Symbolic links pointing to moved or non-existing targets are sometimes called *broken*, *orphaned*, *dead*, or *dangling*.

Symbolic links are different from [hard links](https://en.wikipedia.org/wiki/Hard_link "Hard link"). Hard links do not link paths on different [volumes](https://en.wikipedia.org/wiki/Volume_\(computing\) "Volume (computing)") or [file systems](https://en.wikipedia.org/wiki/File_system "File system"), whereas symbolic links may point to any file or directory irrespective of the volumes on which the link and target reside. Hard links always refer to an existing file, whereas symbolic links may contain an arbitrary path that does not point to anything.

Symbolic links operate transparently for many operations: programs that read or write to files named by a symbolic link will behave as if operating directly on the target file. However, they have the effect of changing an otherwise hierarchic filesystem from a [tree](https://en.wikipedia.org/wiki/Tree_\(graph_theory\) "Tree (graph theory)") into a directed graph, which can have consequences for such simple operations as determining the current directory of a process. Even the Unix standard for navigating to a directory's parent directory no longer works reliably in the face of symlinks. Some [shells](https://en.wikipedia.org/wiki/Unix_shell "Unix shell") [heuristically](https://en.wikipedia.org/wiki/Heuristic "Heuristic") try to uphold the illusion of a tree-shaped hierarchy, but when they do, this causes them to produce different results from other programs that manipulate pathnames without such heuristic, relying on the operating system instead. [5](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-:0-5) Programs that need to handle symbolic links specially (e.g., shells and backup utilities) thus need to identify and manipulate them directly.

Some Unix as well as Linux distributions use symbolic links extensively in an effort to reorder the file system hierarchy. This is accomplished with several mechanisms, such as variant, context-dependent symbolic links. This offers the opportunity to create a more intuitive or application-specific [directory tree](https://en.wikipedia.org/wiki/Directory_tree "Directory tree") and to reorganize the system without having to redesign the core set of system functions and utilities.

## POSIX and Unix-like operating systems

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=2 "Edit section: POSIX and Unix-like operating systems")\]

In [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX")\-compliant operating systems, symbolic links are created with the `symlink` [6](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-6) system call. The `[ln](https://en.wikipedia.org/wiki/Ln_\(Unix\) "Ln (Unix)")` shell command normally uses the `link` [7](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-7) system call, which creates a [hard link](https://en.wikipedia.org/wiki/Hard_link "Hard link"). When the `ln *-s*` flag is specified, the symlink() system call is used instead, creating a symbolic link. Symlinks were introduced in 1982 in [4.1a BSD Unix](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution "Berkeley Software Distribution") from [U.C. Berkeley](https://en.wikipedia.org/wiki/Computer_Systems_Research_Group "Computer Systems Research Group"). [8](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-8)

The following command creates a symbolic link at the [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface "Command-line interface") (shell):

```
 ln -s target_path link_path
```

target\_path is the relative or absolute path to which the symbolic link should point. Usually the target will exist, although symbolic links may be created to non-existent targets. link\_path is the path of the symbolic link.

After creating the symbolic link, some operations can be used to treat it as an alias for the target. However, the `lstat`, [9](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-9) `lchown` [10](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-10) and `readlink` [11](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-11) operations are unique to symbolic links and do not apply to the target; by using those system calls, programs that examine the file system (e.g., `[ls](https://en.wikipedia.org/wiki/Ls "Ls")`, `[find](https://en.wikipedia.org/wiki/Find_\(Unix\) "Find (Unix)")`) can report on symbolic links (instead of their targets, if any). Because the `rename` and `[unlink](https://en.wikipedia.org/wiki/Unlink_\(Unix\) "Unlink (Unix)")` system calls are coded to operate directly on symbolic links, file system management commands (e.g., `[rm](https://en.wikipedia.org/wiki/Rm_\(Unix\) "Rm (Unix)")`, `[mv](https://en.wikipedia.org/wiki/Mv_\(Unix\) "Mv (Unix)")`) affect the symbolic link itself (instead of being applied to the symbolic link target, if any). The `rm` (delete file) command removes the link itself, not the target file. Likewise, the `mv` command moves or renames the link, not the target. The `[cp](https://en.wikipedia.org/wiki/Cp_\(Unix\) "Cp (Unix)")` command has options that allow either the symbolic link or the target to be copied. Commands which read or write file contents will access the contents of the target file.

The POSIX directory listing application, `ls`, denotes symbolic links with an arrow after the name, pointing to the name of the target file (see following example), when the long directory list is requested (`-l` option). When a directory listing of a symbolic link that points to a directory is requested, only the link itself will be displayed. In order to obtain a listing of the linked directory, the path must include a trailing directory separator character ('/', slash).

Note: In the example below do not create "three" directory before creation of link in /tmp directory.

```
$ mkdir -p /tmp/one/two
$ echo "test_a" >/tmp/one/two/a
$ echo "test_b" >/tmp/one/two/b
$ cd /tmp/one/two
$ ls -l
-rw-r--r-- 1 user group 7 Jan 01 10:01 a
-rw-r--r-- 1 user group 7 Jan 01 10:01 b

$ cd /tmp
$ ln -s /tmp/one/two three
$ ls -l three
lrwxrwxrwx 1 user group 12 Jul 22 10:02 /tmp/three -> /tmp/one/two
$ ls -l three/
-rw-r--r-- 1 user group 7 Jan 01 10:01 a
-rw-r--r-- 1 user group 7 Jan 01 10:01 b

$ cd three
$ ls -l
-rw-r--r-- 1 user group 7 Jan 01 10:01 a
-rw-r--r-- 1 user group 7 Jan 01 10:01 b
$ cat a
test_a
$ cat /tmp/one/two/a
test_a
$ echo "test_c" >/tmp/one/two/a
$ cat /tmp/one/two/a
test_c
$ cat a
test_c
```

### Storage of symbolic links

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=3 "Edit section: Storage of symbolic links")\]

Early implementations of symbolic links stored the symbolic link information as data in regular files. The file contained the textual reference to the link's target, and the file mode bits indicated that the type of the file is a symbolic link.

This method was slow and an inefficient use of [disk-space](https://en.wikipedia.org/wiki/Disk_storage "Disk storage") on small systems. An improvement, called **fast symlinks**, allowed storage of the target path within the [data structures](https://en.wikipedia.org/wiki/Data_structure "Data structure") used for storing file information on disk ([inodes](https://en.wikipedia.org/wiki/Inode "Inode")). This space normally stores a list of disk [block](https://en.wikipedia.org/wiki/Block_\(data_storage\) "Block (data storage)") addresses allocated to a file. Thus, symlinks with short target paths are accessed quickly. Systems with fast symlinks often fall back to using the original method if the target path exceeds the available inode space. The original style is [retroactively termed](https://en.wikipedia.org/wiki/Retronym "Retronym") a **slow symlink**. It is also used for disk compatibility with other or older versions of operating systems.

Although storing the link value inside the inode saves a disk block and a disk read, the operating system still needs to parse the path name in the link, which always requires reading additional inodes and generally requires reading other, and potentially many, directories, processing both the list of files and the inodes of each of them until it finds a match with the link's path components. Only when a link points to a file in the same directory do "fast symlinks" provide significantly better performance than other symlinks.

The vast majority of POSIX-compliant implementations use fast symlinks. However, the [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX") standard does not require the entire set of file status information common to regular files to be implemented for symlinks. This allows implementations to use other solutions, such as storing symlink data in directory entries.

The [file system permissions](https://en.wikipedia.org/wiki/File_system_permissions "File system permissions") of a symbolic link are not used; the access modes of the target file are controlled by the target file's own permissions. Some operating systems, such as FreeBSD, offer the ability to modify file permissions and filesystem attributes of a symbolic link, through `lchmod` [12](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-12) and `lchflags` [13](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-13) system calls respectively.

The reported size of a symlink is the number of characters in the path it points to.

A traditional [Unix filesystem](https://en.wikipedia.org/wiki/Unix_filesystem "Unix filesystem") has a tree structure, [14](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-Ritchie-14) however symbolic links allow it to contain loops. [5](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-:0-5)

[NTFS](https://en.wikipedia.org/wiki/NTFS "NTFS") 3.1 introduced support for symbolic links for any type of file. It was included with [Windows XP](https://en.wikipedia.org/wiki/Windows_XP "Windows XP"), but was only enabled by default for kernel-mode apps. [Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista "Windows Vista") and later versions of Windows enabled support for symbolic links to user-mode applications. The `mklink` internal command of [Windows Command Prompt](https://en.wikipedia.org/wiki/Windows_command_prompt "Windows command prompt") can create symbolic links. Third-party drivers are required to enable support for NTFS symbolic links in Windows XP. [15](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-15) Unlike [junction points](https://en.wikipedia.org/wiki/NTFS_junction_point "NTFS junction point"), a symbolic link can also point to a file or remote [Server Message Block](https://en.wikipedia.org/wiki/Server_Message_Block "Server Message Block") (SMB) network path. Additionally, the NTFS symbolic link implementation provides full support for cross-filesystem links. However, the functionality enabling cross-host symbolic links requires that the remote system also support them.

Symbolic links are designed to aid in migration and application compatibility with [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX") operating systems. Microsoft aimed for Windows Vista's symbolic links to "function just like UNIX links". [16](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-16) However, the implementation differs from Unix symbolic links in several ways. For example, Windows Vista users must manually indicate when creating a symbolic link whether it is a file or a directory. [17](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-17) Windows 7 and Vista support a maximum of 31 [reparse points](https://en.wikipedia.org/wiki/Reparse_point "Reparse point") (and therefore symbolic links) for a given path (i.e. any given path can have at most 31 indirections before Windows gives up). [18](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-18) Only users with the new *Create Symbolic Link* privilege, which only administrators have by default, can create symbolic links. [19](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-19) If this is not the desired behavior, it must be changed in the Local Security Policy management console. Additionally, NTFS symbolic links to files are distinct from NTFS symbolic links to directories and therefore cannot be used interchangeably, unlike on POSIX where the same symbolic link can refer to either files or directories.

In Windows Vista and later, when the working directory path ends with a symbolic link, the current parent path reference, `..`, will refer to the parent directory of the symbolic link rather than that of its target. This behavior is also found at the shell level in at least some POSIX systems, including [Linux](https://en.wikipedia.org/wiki/Linux "Linux"), but never in accessing files and directories through operating system calls. For instance, bash builtin commands `pwd` and `cd` operate on the current logical directory. `pwd` is often used in scripts to determine the actual current working directory. When any path is used with a system call, any use of `..` will use the actual filesystem parent of the directory containing the `..` pseudo-directory entry. So, `cd ..; cat something` and `cat ../something` may return completely different results.

The following examples both create a symbolic link called "Downloads" at "E:\\" that points to the Downloads folder in the current user's profile.

-   The first example works in [Windows Command Prompt](https://en.wikipedia.org/wiki/Windows_command_prompt "Windows command prompt") only because `mklink` is an internal command.

`mklink /D E:\Downloads %UserProfile%\Downloads`

-   The second example works in [PowerShell](https://en.wikipedia.org/wiki/PowerShell "PowerShell") only because New-Item is an internal cmdlet.

`New-Item -Path 'E:\Downloads' -ItemType 'SymbolicLink' -Value "$Env:UserProfile\Downloads"`

### NTFS junction points

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=8 "Edit section: NTFS junction points")\]

The [Windows 2000](https://en.wikipedia.org/wiki/Windows_2000 "Windows 2000") version of [NTFS](https://en.wikipedia.org/wiki/NTFS "NTFS") introduced [reparse points](https://en.wikipedia.org/wiki/NTFS_reparse_point "NTFS reparse point"), which enabled, among other things, the use of [Volume Mount Points](https://en.wikipedia.org/wiki/Volume_Mount_Point "Volume Mount Point") and junction points. Junction points are for directories only, and moreover, local directories only; junction points to remote shares are unsupported. [20](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-20) The Windows 2000 and XP Resource Kits include a program called *linkd* to create junction points; a more powerful one named *Junction* was distributed by [Sysinternals](https://en.wikipedia.org/wiki/Sysinternals "Sysinternals")' [Mark Russinovich](https://en.wikipedia.org/wiki/Mark_Russinovich "Mark Russinovich").

Not all standard applications support reparse points. Most noticeably, Backup suffers from this problem and will issue an error message 0x80070003 [21](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-21) when the folders to be backed up contain a reparse point.

[Shortcuts](https://en.wikipedia.org/wiki/Computer_shortcut "Computer shortcut"), which are supported by the graphical file browsers of some operating systems, may resemble symbolic links but differ in a number of important ways. One difference is what type of software is able to follow them:

-   Symbolic links are automatically resolved by the file system. Any software program, upon accessing a symbolic link, will see the target instead, whether the program is aware of symbolic links or not.
-   Shortcuts are treated like ordinary files by the file system and by software programs that are not aware of them. Only software programs that understand shortcuts (such as the Windows shell and file browsers) treat them as references to other files.

The mechanisms also have different capabilities:

-   [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows "Microsoft Windows") shortcuts normally refer to a destination by an [absolute path](https://en.wikipedia.org/wiki/Absolute_path "Absolute path") (starting from the [root directory](https://en.wikipedia.org/wiki/Root_directory "Root directory")), whereas POSIX symbolic links can refer to destinations via either an absolute or a [relative path](https://en.wikipedia.org/wiki/Relative_path "Relative path"). The latter is useful if both the symlink and its target share some common ancestor path which is not known at creation (e.g., in an [archive file](https://en.wikipedia.org/wiki/Archive_file "Archive file") that can be unpacked anywhere).
-   Microsoft Windows application shortcuts contain additional metadata that can be associated with the destination, whereas POSIX symbolic links are just strings that will be interpreted as absolute or relative pathnames.
-   Unlike symbolic links, Windows shortcuts maintain their references to their targets even when the target is moved or renamed. Windows domain clients may subscribe to a [Windows service](https://en.wikipedia.org/wiki/Windows_service "Windows service") called Distributed Link Tracking [22](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-22) to track the changes in files and folders to which they are interested. The service maintains the integrity of shortcuts, even when files and folders are moved across the network. [23](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-23) Additionally, in Windows 9x and later, [Windows shell](https://en.wikipedia.org/wiki/Windows_shell "Windows shell") tries to find the target of a broken shortcut before proposing to delete it.

Almost like shortcuts, but transparent to the Windows shell. [24](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-24) They are implemented as ordinary folders (which need to have the *read only* and/or *system* attribute [25](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-25)) containing a shortcut named *target.lnk* which refers to the target and a (hidden) *desktop.ini* with (at least) the following contents:

```
 [.ShellClassInfo]
 CLSID2={0AFACED1-E828-11D1-9187-B532F1E9575D}
```

Folder shortcuts are created and used from the Windows shell in the *network neighborhood* for example.

The *shell objects* [26](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-26) or *shell folders* are defined in the Windows registry and can be used to implement a sort of symbolic link too. Like folder shortcuts, they are transparent to the Windows shell.

A minimal implementation is (the CLSID *{00000000-0000-0000-0000-000000000000}* is used as a placeholder):

```
 [HKEY_CLASSES_ROOT\CLSID\{00000000-0000-0000-0000-000000000000}]
 @="display name"
 [HKEY_CLASSES_ROOT\CLSID\{00000000-0000-0000-0000-000000000000}\DefaultIcon]
 @="..." ; path to icon
 [HKEY_CLASSES_ROOT\CLSID\{00000000-0000-0000-0000-000000000000}\InProcServer32]
 @="%SystemRoot%\\System32\\ShDocVw.Dll"
 "ThreadingModel"="Apartment"
 [HKEY_CLASSES_ROOT\CLSID\{00000000-0000-0000-0000-000000000000}\Instance]
 "CLSID"="{0AFACED1-E828-11D1-9187-B532F1E9575D}"
 [HKEY_CLASSES_ROOT\CLSID\{00000000-0000-0000-0000-000000000000}\Instance\InitPropertyBag]
 "Attributes"=hex:15,00,00,00
 "Target"="..." ; absolute (WITHOUT "TargetKnownFolder" or "TargetSpecialFolder" only)
                ; or relative path to target
 "TargetKnownFolder"="{guidguid-guid-guid-guid-guidguidguid}" ; GUID of target folder, Windows Vista and later
 "TargetSpecialFolder"="0x00xy" ; CSIDL of target
 [HKEY_CLASSES_ROOT\CLSID\{00000000-0000-0000-0000-000000000000}\ShellFolder]
 "Attributes"=hex:00,00,00,00
```

The *My Documents* folder on the *Desktop* as well as the *Fonts* and the *Administrative Tools* folders in the *Control Panel* are examples of *shell objects* redirected to file-system folders.

### Cygwin symbolic links

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=12 "Edit section: Cygwin symbolic links")\]

[Cygwin](https://en.wikipedia.org/wiki/Cygwin "Cygwin") simulates POSIX-compliant symbolic links in the Microsoft Windows file system. It uses identical programming and user utility interfaces as Unix (see above), but creates Windows shortcuts (.lnk files) with additional information used by Cygwin at the time of symlink resolution. Cygwin symlinks are compliant with the POSIX standard in terms of how they are resolved, and with Windows standards in terms of their on-disk representation.

Additionally, Cygwin can be set up to support native Windows symbolic links which can be used out of Cygwin without restrictions. [27](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-cygwin-27) This requires:

1.  Changing the CYGWIN environment variable to contain winsymlinks:native;
2.  Running the Cygwin with elevated rights because Windows restricts the creation of symbolic links to privileged users

Some differences exist, however. Cygwin has no way to specify shortcut-related information – such as working directory or icon – as there is no place for such parameters in `ln -s` command. To create standard Microsoft .lnk files Cygwin provides the `mkshortcut` and `readshortcut` utilities. [28](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-28)

The Cygwin User's Guide has more information on this topic. [27](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-cygwin-27) [MSYS2](https://en.wikipedia.org/wiki/MSYS2 "MSYS2"), which is based on Cygwin, has a similar set of winsymlinks settings but defaults to copying the files. [29](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-msys2-sym-29)

## Comparison of POSIX and Windows symbolic links

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=13 "Edit section: Comparison of POSIX and Windows symbolic links")\]

1.  except when using special tools
2.  On saving, becomes an absolute path
3.  Supported on Windows Vista and later. The Windows implementation is not POSIX-compliant. Creating them requires the "create symbolic link" privilege (SeCreateSymbolicLinkPrivilege). By default a user account holds this privilege when it is either an administrator or has Developer Mode enabled (Windows 10 v1703 and later). [30](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-32)
4.  POSIX permits hard links on folders but does not require them. Modern file systems tend to not support it.

## Other implementations

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=14 "Edit section: Other implementations")\]

Implementations of features similar to symbolic links.

[MIT](https://en.wikipedia.org/wiki/MIT "MIT") [Compatible Time-Sharing System](https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System "Compatible Time-Sharing System") c. 1963 and [Incompatible Timesharing System](https://en.wikipedia.org/wiki/Incompatible_Timesharing_System "Incompatible Timesharing System") both have linked files where the name of the target file is specified in a directory entry. [2](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-50th-2) [3](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-ctsspg69-3) [4](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-ctsspg63-4)

The command creating symbolic links is `makelink`, which is also used for hard links. Internally the dos.library returns an error code indicating that a target is a soft link if you try to perform actions on it that are only legal for a file, and applications that wish to follow the symbolic link then needs to explicitly make a call to follow the link and retry the operation. The [AmigaDOS](https://en.wikipedia.org/wiki/AmigaDOS "AmigaDOS") shell will follow links automatically.

In Mac OS, applications or users can also employ *[aliases](https://en.wikipedia.org/wiki/Alias_\(Mac_OS\) "Alias (Mac OS)")*, which have the added feature of following the target, even if it is moved to another location on the same volume. This is not to be confused with the shell command [alias](https://en.wikipedia.org/wiki/Alias_\(command\) "Alias (command)").

In the [OS/2](https://en.wikipedia.org/wiki/OS/2 "OS/2") operating system, symbolic links somewhat resemble [shadows](https://en.wikipedia.org/wiki/Shadow_\(OS/2\) "Shadow (OS/2)") in the graphical [Workplace Shell](https://en.wikipedia.org/wiki/Workplace_Shell "Workplace Shell"). However, shadows, due to the fully object-oriented System Object Model, are considerably more powerful and robust than a simple link. For example, shadows do not lose their capabilities when renamed or when either the object or subject of the link is relocated. [31](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-35)

## Variable symbolic links

\[[edit](https://en.wikipedia.org/w/index.php?title=Symbolic_link&action=edit&section=19 "Edit section: Variable symbolic links")\]

Symbolic links may be implemented in a context-dependent or variable fashion, such that the link points to varying targets depending on a configuration parameter, run-time parameter, or other instantaneous condition.

A *variable* or *variant symbolic link* is a symbolic link that has a variable name embedded in it. This allows some flexibility in filesystem order that is not possible with a standard symbolic link. Variables embedded in a symbolic link may include user and environment specific information.

[Operating systems](https://en.wikipedia.org/wiki/Operating_system "Operating system") that make use of variant symbolic links include [NetBSD](https://en.wikipedia.org/wiki/NetBSD "NetBSD"), [DragonFly BSD](https://en.wikipedia.org/wiki/DragonFly_BSD "DragonFly BSD"), [Domain/OS](https://en.wikipedia.org/wiki/Domain/OS "Domain/OS"). [32](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-36) [33](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-37) [5](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-:0-5) [Tru64](https://en.wikipedia.org/wiki/Tru64 "Tru64") uses a *context dependent symbolic link* where the context is the cluster member number.

[Pyramid Technology](https://en.wikipedia.org/wiki/Pyramid_Technology "Pyramid Technology")'s OSx operating system implemented *conditional symbolic links* which pointed to different locations depending on which [universe](https://en.wikipedia.org/wiki/Universe_\(Unix\) "Universe (Unix)") a program was running in. The universes supported were AT&Ts's [SysV.3](https://en.wikipedia.org/wiki/UNIX_System_V "UNIX System V") and the [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution "Berkeley Software Distribution") (BSD 4.3). For example: if the [ps](https://en.wikipedia.org/wiki/Ps_\(Unix\) "Ps (Unix)") command was run in the *att* universe, then the symbolic link for the directory */bin* would point to */.attbin* and the program */.attbin/ps* would be executed. Whereas if the ps command was run in the *ucb* universe, then */bin* would point to */.ucbbin* and */.ucbbin/ps* would be executed. Similar Conditional Symbolic Links were also created for other directories such as */lib*, */usr/lib*, */usr/include*. [34](https://en.wikipedia.org/wiki/Symbolic_link#cite_note-38)

-   [Symlink race](https://en.wikipedia.org/wiki/Symlink_race "Symlink race") — a security-vulnerability caused by symbolic links
-   [freedup](https://en.wikipedia.org/wiki/Freedup "Freedup") — generates links between identical data automatically
-   [Pointer (computer programming)](https://en.wikipedia.org/wiki/Pointer_\(computer_programming\) "Pointer (computer programming)")

1.  [Pathname resolution](https://www.opengroup.org/onlinepubs/009695399/basedefs/xbd_chap04.html#tag_04_11), [POSIX](https://en.wikipedia.org/wiki/POSIX "POSIX").
2.  Walden, David; [Van Vleck, Tom](https://en.wikipedia.org/wiki/Tom_Van_Vleck "Tom Van Vleck"), eds. (2011). ["Compatible Time-Sharing System (1961-1973): Fiftieth Anniversary Commemorative Overview"](https://multicians.org/thvv/compatible-time-sharing-system.pdf) (PDF). IEEE Computer Society. Retrieved February 20, 2022. As CTSS developed, we provided ways for users to share their files on disk, through "common files" and "linking,"
3.  Crisman, Patricia A., ed. (December 31, 1969). ["The Compatible Time-Sharing System, A Programmer's Guide"](http://www.bitsavers.org/pdf/mit/ctss/CTSS_ProgrammersGuide_Dec69.pdf) (PDF). The M.I.T Computation Center. Retrieved March 10, 2022. U.F.D. entries that point to other U.F.D. entries instead of to the file itself
4.  [Corbato, F. J.](https://en.wikipedia.org/wiki/Fernando_J._Corbat%C3%B3 "Fernando J. Corbató"); Daggett, M. M.; Daley, R. C.; Creasy, R. J.; Hellwig, J. D.; Orenstein, R. H.; Korn, L. K. (1963). ["The Compatible Time-Sharing System A Programmer's Guide"](https://www.ibiblio.org/apollo/Documents/CTSS_ProgrammersGuide.pdf) (PDF). MIT. Retrieved November 29, 2022. Link: The format is similar to Copy. The specified file is not copied
5.  [Pike, Rob](https://en.wikipedia.org/wiki/Rob_Pike "Rob Pike") (2000). [*Lexical file names in Plan 9 or getting dot-dot right*](https://static.usenix.org/events/usenix2000/general/full_papers/pikelex/pikelex.pdf) (PDF). Proc. [USENIX](https://en.wikipedia.org/wiki/USENIX "USENIX") Annual Tech. Conf.
6.  [symlink, symlinkat](https://pubs.opengroup.org/onlinepubs/9699919799/functions/symlink.html). IEEE Std 1003.1, 2013 Edition.
7.  [link, linkat](https://pubs.opengroup.org/onlinepubs/9699919799/functions/link.html). IEEE Std 1003.1, 2013 Edition.
8.  [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy "Bill Joy"); [Sam Leffler](https://en.wikipedia.org/wiki/Samuel_J._Leffler "Samuel J. Leffler"). ["Surviving with 4.1a bsd"](https://github.com/dspinellis/unix-history-repo/blob/BSD-4_1c_2/usr/man/man0/changes.4-82#L28). *[GitHub](https://en.wikipedia.org/wiki/GitHub "GitHub")*. Retrieved 8 September 2023. It also includes a few other features which you may find useful, such as *symbolic links* and an improved group scheme.
9.  [fstatat, lstat, stat - get file status](https://pubs.opengroup.org/onlinepubs/9699919799/functions/fstatat.html) IEEE Std 1003.1, 2013 Edition.
10.  [lchown - change the owner and group of a symbolic link](https://pubs.opengroup.org/onlinepubs/9699919799/functions/lchown.html) IEEE Std 1003.1, 2013 Edition.
11.  [readlink, readlinkat - read the contents of a symbolic link](https://pubs.opengroup.org/onlinepubs/9699919799/functions/readlink.html) IEEE Std 1003.1, 2013 Edition.
12.  ["lchmod(2)"](https://www.freebsd.org/cgi/man.cgi?query=lchmod&apropos=0&sektion=2&manpath=FreeBSD+11.0-RELEASE&arch=default&format=html). Manual pages for FreeBSD 11.
13.  ["lchflags(2)"](https://www.freebsd.org/cgi/man.cgi?query=lchflags&apropos=0&sektion=2&manpath=FreeBSD+11.0-RELEASE&arch=default&format=html). Manual pages for FreeBSD 11.
14.  [Ritchie, D.M.](https://en.wikipedia.org/wiki/Dennis_Ritchie "Dennis Ritchie"); [Thompson, K.](https://en.wikipedia.org/wiki/Ken_Thompson "Ken Thompson") (July 1978). "The UNIX Time-Sharing System". *Bell System Tech. J*. **57** (6): 1905–1929\. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_\(identifier\) "CiteSeerX (identifier)") [10.1.1.112.595](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.112.595). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1002/j.1538-7305.1978.tb02136.x](https://doi.org/10.1002%2Fj.1538-7305.1978.tb02136.x).
15.  ["Link Shell Extension website"](https://schinagl.priv.at/nt/hardlinkshellext/hardlinkshellext.html#symboliclinksforwindowsxp). *Link Shell Extension website*.
16.  [Symbolic Links](https://msdn.microsoft.com/en-us/library/aa365680.aspx), MSDN Library, Win32 and COM Development, 2008-01-18
17.  ["CreateSymbolicLinkA function (winbase.h)"](https://msdn.microsoft.com/en-us/library/aa363866.aspx). *[MSDN](https://en.wikipedia.org/wiki/MSDN "MSDN")*. June 2023.
18.  [Symbolic Link Programming Considerations](https://msdn.microsoft.com/en-us/library/aa365460\(VS.85\).aspx), MSDN
19.  Mark Russinovich: [Inside the Windows Vista Kernel: Part 1](https://www.microsoft.com/technet/technetmag/issues/2007/02/VistaKernel/default.aspx) – File-based symbolic links, Microsoft Technet, February 2007.
20.  ["Sysinternals Junction documentation"](https://www.microsoft.com/technet/sysinternals/FileAndDisk/Junction.mspx). *microsoft.com*. Retrieved 23 March 2018.
21.  ["Windows backup or restore errors 0x80070001, 0x81000037, or 0x80070003"](https://support.microsoft.com/kb/973455). *support.microsoft.com*.
22.  ["Distributed Link Tracking on domain controllers - Windows Server"](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/distributed-link-tracking-on-domain-controller). 23 February 2023.
23.  ["Distributed Link Tracking and Object Identifiers"](https://msdn.microsoft.com/en-us/library/aa363997%28v=VS.85%29.aspx). *[Microsoft Developers Network](https://en.wikipedia.org/wiki/Microsoft_Developers_Network "Microsoft Developers Network")*. Microsoft Corporation. 20 March 2011. Retrieved 30 June 2011.
24.  ["Specifying a Namespace Extension's Location"](https://msdn.microsoft.com/en-us/library/bb776817.aspx). *msdn.microsoft.com*. 11 January 2008. Retrieved 23 March 2018.
25.  ["You cannot view or change the Read-only or the System attributes of folders in Windows Server 2003, in Windows XP, in Windows Vista or in Windows 7"](https://support.microsoft.com/kb/256614/en-us). *support.microsoft.com*. Retrieved 2021-07-08.
26.  [Creating Shell Extensions with Shell Instance Objects](https://msdn.microsoft.com/library/ms997573.aspx). msdn.microsoft.com
27.  ["Chapter 3. Using Cygwin"](https://www.cygwin.com/cygwin-ug-net/using.html). *www.cygwin.com*. Retrieved 2021-07-08.
28.  ["Using Cygwin effectively with Windows"](https://www.cygwin.com/cygwin-ug-net/using-effectively.html#id325160).
29.  ["Coreutils: ln --symbolic creates hard links (MSYS2-packages #249)"](https://github.com/msys2/MSYS2-packages/issues/249). *GitHub*.
30.  ["Create symbolic links"](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/create-symbolic-links). *Windows client documentation for IT Pros*. [Microsoft](https://en.wikipedia.org/wiki/Microsoft "Microsoft"). 18 January 2023 – via Microsoft Learn.
31.  Rojas, Miguel (16 December 2020). ["Cómo ejecutar versiones de Python diferentes a las predeterminadas"](https://manualestutor.com/desarrollador-de-ios/como-ejecutar-versiones-de-python-diferentes-a-las-predeterminadas/). *Manualestutor*. Retrieved 20 December 2020.
32.  `[symlink(7)](https://man.netbsd.org/symlink.7)` – [NetBSD](https://en.wikipedia.org/wiki/NetBSD "NetBSD") Miscellaneous Information [Manual](https://en.wikipedia.org/wiki/Man_page "Man page"): magic symlinks.
33.  Brooks Davis (2008). ["Variant symbolic links for FreeBSD"](https://wiki.freebsd.org/200808DevSummit?action=AttachFile&do=get&target=variant-symlinks-for-freebsd.pdf) (PDF).
34.  Neil Brown (2016). ["A case for variant symlinks"](https://lwn.net/Articles/680705/). *LWN*.

-   [Q & A: The difference between hard and soft links](https://linuxgazette.net/105/pitcher.html) as applied to Linux
-   [Junction](https://technet.microsoft.com/en-us/sysinternals/bb896768): maintain NTFS junction points (for Windows 2000 and above)
-   [FSUtil Hardlink](https://technet.microsoft.com/en-us/library/cc788097%28WS.10%29.aspx): Microsoft Technet page on using the command-line tool FSUtil to create hardlinks (for Windows 2000 and above)
-   [Symbolic Drivers for Windows XP](https://emk.name/symlink.html) (in Japanese): file system drivers to enable Symbolic Links for Windows XP (also mirrored on Link Shell Extension site). Sources available.