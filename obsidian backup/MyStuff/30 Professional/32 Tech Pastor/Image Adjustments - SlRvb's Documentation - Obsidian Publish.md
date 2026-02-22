---
title: Image Adjustments - SlRvb's Documentation - Obsidian Publish
source: https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments
author:
  - "[[SlRvb's Documentation]]"
published:
created: 2025-02-06
description: Image Adjustments - SlRvb's Documentation - Powered by Obsidian Publish.
tags:
  - clippings
---
```yaml
tag: Snippet
description: Image Adjustments provides more flexibility to move/position and re-size images in notes.
```

> More flexibility to move/position and re-size images in notes.

**Do not** use the snippet version with the ITS Theme installed

- [Position](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Position)
- [Inner Image Positions](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Inner%20Image%20Positions)
- [Sizing](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Sizing)
- [Obsidian Sizing](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Obsidian%20Sizing)
- [Types](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Types)
- [Banner](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Banner)
- [Portrait](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Portrait)
- [Profile](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Profile)
- [Extras](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Extras)
- [Invert Colors](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Invert%20Colors)
- [CSS Classes](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#CSS%20Classes)

## Syntax

```markdown
![[Internal Image.png|attribute attribute2]]
![[Internal Image.png|sban cover hs-med]]
```

```markdown
![External Image|attribute attribute2](.png)
![External Image|sban cover hs-med](.png)
```

## Position

| Attribute | Description |
| --- | --- |
| `left` | Move the image to the left. |
| `right` | Move the image to the right. |
| `center` | Move the image to the center. |

Position Attributes will not work in Live Preview

This causes issues with editing notes so it is and will not be natively supported by me unless that stops occurring. If you're okay with these potential issues, include the `|lp` option to allow it in Live Preview.

I will not attempt to fix any issues that arise out of the use of `|lp`. If something goes wrong with your notes with my theme or snippet, try removing this option before reporting that issue.

## Inner Image Positions

| Attribute | Description |
| --- | --- |
| `p+l` | Move inside of the image to the left. |
| `p+r` | Move inside of the image to the right. |
| `p+t` | Move inside of the image to the top. |
| `p+b` | Move inside of the image to the bottom. |
| `p+c` | Move inside of the image to the center. |

| Attribute | Description |
| --- | --- |
| `p+cr` | Move inside of the image to the center right. |
| `p+cl` | Move inside of the image to the center left. |
| \--- |  |
| `p+ct` | Move inside of the image to the center top of the image. |
| `p+cct` | Move inside of the image to the center top, slightly higher than `p+ct` |
| `p+tc` | Move inside of the image to the center top, slightly lower than `pt` |
| `p+tcc` | Move inside of the image to the center top, slightly lower than `p+tc` |
| \--- |  |
| `p+cb` | Move inside of the image to the center bottom of the image. |
| `p+ccb` | Move inside of the image to the center bottom, slightly lower than `p+cb` |
| `p+bc` | Move inside of the image to the center bottom, slightly higher than `pb` |
| `p+bcc` | Move inside of the image to the center bottom, slightly higher than `p+bc` |

## Sizing

| Attributes | Resize Image Height |
| --- | --- |
| `hmicro` | 70px |
| `htiny` | 100px |
| `hsmall` | 200px |
| `hs-med` | 300px |
| `hm-sm` | 400px |
| `hmed` | 500px |
| `hm-tl` | 600px |
| `htall` | 700px |
| `hfull` | 100% horizontally |

| Attributes | Resize Image Width | Relative Sizing |
| --- | --- | --- |
| `wmicro` | 70px | 10% |
| `wtiny` | 100px | 20% |
| `wsmall` | 200px | 30% |
| `ws-med` | 300px | 40% |
| `wm-sm` | 400px | 50% |
| `wmed` | 500px | 60% |
| `wm-tl` | 600px | 70% |
| `wtall` | 700px | 85% |
| `wfull` | 100% vertically | 100% |

The `relative` attribute will use percentage sizing based on current window size and scale image to that. It only uses the width attributes for sizing.

**Syntax/Formatting**: `![[Image.png|relative wtiny]]`

## Obsidian Sizing

Place the `|<numbers>` sizing at the *end* of the text and it will shrink the image to that size.

## Types

## Banner

| Attribute | Description |
| --- | --- |
| `banner` | Crop the image height-wise to 150px while setting the width to cover the entire page. |
| `banner+small` | Crop the image height-wise to 100px while setting the width to cover the entire page. |
| `banner+tall` | Crop the image height-wise to 500px while setting the width to cover the entire page. |
| `sban` | Only sets image's width to 100% to cover the entire page |

## Portrait

| Attribute | Description |
| --- | --- |
| `portrait` | `portrait` will crop the image width-wise to 40% while setting the height to a standard of 400px. |
| `portrait+small` | `portrait+small` will crop the image width-wise to 20% while setting the height to a standard of 200px. |
| `portrait+tall` | `portrait+tall` will crop the image width-wise to 50% while setting the height to a standard of 500px. |

## Profile

| Attribute | Description |
| --- | --- |
| `profile` | Round the borders of the image to create a round image and size it to 100px. |
| `profile+medium` | Round the borders of the image to create a round image and resize it to 250px. |

## Extras

| Attribute | Description |
| --- | --- |
| `cover` | A resized image will maintain aspect ratio and avoid stretching. |
| `clear` | Allow image to sit below another image if it's on the same side instead of sitting in the middle of the page. |
| `#cap` | Add caption to image using the alternate text of an image   `![[image.png#cap#wtiny\\|Caption text]]`   ([Sizing](https://publish.obsidian.md/slrvb-docs/ITS+Theme/Image+Adjustments#Sizing) syntax is the only way to resize with this option) |

## Invert Colors

| Attribute | Description |
| --- | --- |
| `invertb` | Invert the image's colors (dark mode). |
| `invertw` | Invert the image's colors (light mode). |
| `invertbc` | Invert colors and increase contrast (dark mode). |
| `invertwc` | Invert colors and increase contrast (light mode). |

## Flip / Rotation

| Abbr | Full | Description |
| --- | --- | --- |
| `flip-x` | `flip-horizontal` | Flip image horizontally |
| `flip-y` | `flip-vertically` | Flip image vertically |
| `flip-xy` | `flip-vertical-horizontal` | Flip image vertically and horizontally |

## CSS Classes

| CSSClass | Description |
| --- | --- |
| `clear-hr` | Force images to stay above/below horizontal lines |
| `clear-headings` | Force images to stay above/below all headings |
| `clear-heading-#` | Force images to stay above/below heading level specified: `1-6` |