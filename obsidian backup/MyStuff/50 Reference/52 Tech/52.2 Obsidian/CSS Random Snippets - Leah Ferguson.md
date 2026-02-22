```
title: CSS Random Snippets
aliases: 
created: 2021-08-07 14:16
publish: true
type: 
jd-number: 
tags: 
cssclass: 
```

Snippets have been tested with a minimum of 0.13.14 unless otherwise noted.

## Plugin: Admonitions

### Remove drop shadow

```
/* Remove drop shadow from Admonitions */
.admonition {
  box-shadow: unset !important;
}
```

## Plugin: Kanban

Styling kanban dates / completed cards (from mgmeyers)

```
.kanban-plugin__item.is-future:not(.is-complete)
  .kanban-plugin__item-metadata-date {
  color: var(--text-muted);
}

.kanban-plugin__item.is-today:not(.is-complete)
  .kanban-plugin__item-metadata-date {
  color: var(--interactive-success);
  font-weight: bold;
}

.kanban-plugin__item.is-past:not(.is-complete)
  .kanban-plugin__item-metadata-date {
  color: var(--text-error);
  font-weight: bold;
}

.kanban-plugin__item.is-complete .kanban-plugin__item-markdown {
  text-decoration: line-through;
  text-decoration-color: var(--text-muted);
}
```

## Plugin: Supercharged Links

### Add emoji based on type value

```
/* Add emoji based on type value */
.data-link-icon[data-link-type*="people" i]::before{
    content: "👤 "
}
```

### Create coloured field around note titles with a specific tag

```
:not(:empty)[data-link-tags*="#yourTagHere" i]{
    color: white;
    background-color: #e94830;
    border-radius: 2px;
    padding: 1px 5px;
}
```

## Tags

### Change pill shape to a square

```
a.tag {
  border-radius:2px !important;
}

span.cm-hashtag.cm-hashtag-begin {
  border-top-left-radius:2px !important;
  border-bottom-left-radius:2px !important;
}
span.cm-hashtag.cm-hashtag-end {
  border-top-right-radius:2px !important;
  border-bottom-right-radius:2px !important;
}
```

### Set Tags a specific colour

```
.tag[href="#yourTagHere"],
.cm-line .cm-hashtag.cm-tag-yourTagHere {
    color: white;
    background-color: #e94830;
    border:0px;
}

.cm-s-obsidian span.cm-hashtag-yourTagHere {
    color: white;
    background-color: #e94830;
    border:0px;
}

span.cm-hashtag.cm-hashtag-begin-yourTagHere {
    color: white;
    background-color: #e94830;
    border:0px;
}

span.cm-hashtag.cm-hashtag-end-yourTagHere {
    color: white;
    background-color: #e94830;
    border:0px;
}
```

## YAML

### Hide front matter in Reading view

```
/* Hides the front matter in Reading view */
.frontmatter-container {
    display: none;
}
```

### Make front matter text size smaller

[#followup](https://publish.obsidian.md/#followup) _Not working in 0.13.14_

```
/* Makes the front matter text size smaller */
.cm-hmd-frontmatter {
    font-size: 0.7em; 
    line-height: .8em; 
    display: block; 
}
```

## Tables

```
/* Set minimum column width and alignment for a Dataview table*/
.table-view-table td {
  min-width: 100px;
  vertical-align: text-top;
}
```