---
cssclasses:
  - dashboard
  - max
---

## Maps of Content

🥸 [[Professional MOC|Professional]]
😇 [[Life and Wisdom MOC|Life and Wisdom]]
📝 [[Notes MOC|Notes]]
📂 [[PKM MOC|PKM]]
🏘️ [[People MOC|My People]]
😎 [[All About Me MOC|Me]]


## Vault Info
- 🗄 Recent file updates
 `$=dv.markdownList(dv.pages('').sort(f=>f.file.mtime.ts,"desc").limit(4).file.link)`
- 😎 Tagged:  favorite 
 `$=dv.markdownList(dv.pages('#favorite AND -"50 Reference/00 Templates"').sort(f=>f.file.name,"desc").limit(4).file.link)`
- 📈 Stats
	-  File Count: `$=dv.pages().length`
	-  Inbox Items: `$=dv.pages('"00 Meta/00.00 Inbox"').length`
	-  TBD Items: `$=dv.pages('"00 Meta/00.01 TBD"').length`
	-  Notes: `$=dv.pages('"40 Atomic/41 Notes"').length`
	- Questions: `$=dv.pages('"40 Atomic/43 Questions"').length`
	- Web Clippings: `$=dv.pages('#clippings').length`
	- Humor: `$=dv.pages('#Humor').length`
	- Quotes: `$=dv.pages('#Quotes').length`
	- Musings: `$=dv.pages('#Musings').length`

---


***Upcoming Events:***
```dataview
TABLE WITHOUT ID file.link as "What", duedate AS "When", duedate - date(today) AS "Remaining days"  
WHERE duedate AND duedate >= date(today) 
sort duedate asc
```













