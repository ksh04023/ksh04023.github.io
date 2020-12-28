---
layout: post
title:  "How to Set Title Background Image"
date:   2020-12-28 19:26:00
categories: Github
---
\
Let's see how to change the background image. As a web front-end newbie, I was wandering about how to change the title background.
It was so simple that I just had to edit a little bit in `index.html`.

I had no idea where the variable `page.cover` comes from, but the answer was here.

```yaml
---
layout: default
title: Home
cover: false
about: 'about.html'
---
```
The upper part of the file, which is called **front matter**, was the key.
[**Yaml front matter**](https://jekyllrb.com/docs/front-matter/) is used to format each file and all the variables are _global_ through the whole blog.

**Before:**
```yaml
cover: false
```
\
Change the variable to image link or the relative path of the background image.\
\
**After:**
```yaml
cover: 'assets/images/background.jpg'
```

<img src="https://i.ibb.co/5k8ZwsB/background.png" alt="background" border="0" width ="200">\
\
Now you can set a beautiful image to your title background🤩




[jekyll-gh]: https://github.com/mojombo/jekyll
[jekyll]:    http://jekyllrb.com
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTg1OTcwMjU4LC01ODAxNDg2NDBdfQ==
-->
