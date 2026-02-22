---
cssclasses:
  - dashboard
  - max
title: Notes Map of Contents
tags:
  - MapOfContents
  - Notes
---
```meta-bind-button
label: Daily Note
hidden: false
class: ""
tooltip: ""
id: DailyNoteButton
style: primary
actions:
  - type: command
    command: daily-notes

```

<br/>

```meta-bind-button
label: Sermon Notes
hidden: false
class: ""
tooltip: ""
id: ""
style: default
actions:
  - type: command
    command: quickadd:choice:b23748f9-0302-40dc-9843-f50b682a9966

```

## Tags
#DailyNotes - Daily Notes
#SermonNotes - Sermon Notes

# Daily Notes
```dataview
table file.name as name, file.size as size, file.ctime as date 
from #DailyNotes
limit 10
sort file.ctime desc
```

# Sermon Notes
```dataview
table file.name as name, file.size as size, file.ctime as date 
from #SermonNotes
limit 10
sort file.ctime desc
```