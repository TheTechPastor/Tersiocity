---
cssclasses:
  - dashboard
  - max
tags:
  - Dashboard
---


> [!multi-column|center]
> 
>> [!blank-container |center]
>> ![[note 1.png|80]] <br/> [[Notes MOC|Notes]]
>> 
>> ![[people1.png|80]] <br/> [[People MOC|People]]
>
>>[!blank-container|center]
>> ![[know 1.png|80]] <br/> [[PKM MOC|PKM]]
>> 
>> ![[pro1.png|80]] <br/> [[Professional MOC|Professional]]
>
>>[!blank-container|center]
>>  ![[life 1.png|80]] <br/> [[Life and Wisdom MOC|Life & Wisdom]]
>>  
>>  ![[me1.png|80]] <br/> [[All About Me MOC|My Stuff]]
>

# Vault Info
- 🗄️ Recent file updates
 `$=dv.markdownList(dv.pages('').sort(f=>f.file.mtime.ts,"desc").limit(4).file.link)`
- 😎 Tagged:  favorite 
 `$=dv.markdownList(dv.pages('#favorite AND -"50 Reference/00 Templates"').sort(f=>f.file.name,"desc").limit(4).file.link)`





- 📈 Stats
	-  File Count: `$=dv.pages().length`
	-  Inbox Items: `$=dv.pages('"00 Meta/00.00 Inbox"').length`
	-  TBD Items: `$=dv.pages('"00 Meta/00.01 TBD"').length`
	-  Notes: `$=dv.pages('"40 Atomic/41 Notes"').length`
	- Questions: `$=dv.pages('"40 Atomic/43 Questions"').length`

- 📂 Files
	- Web Clippings: `$=dv.pages('#clippings').length`
	- Quotes: `$=dv.pages('#Quotes').length`
	- Musings: `$=dv.pages('#Musings').length`
	- Humor: `$=dv.pages('#Humor').length`
---


***Upcoming Events:***
```dataview
TABLE WITHOUT ID file.link as "What", duedate AS "When", duedate - date(today) AS "Remaining days"  
WHERE duedate AND duedate >= date(today) 
sort duedate asc
```


