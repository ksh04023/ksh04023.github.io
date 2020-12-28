---
layout: post
title:  "Make your own blog with Github Pages"
date:   2020-12-27 19:26:00
categories: Github
---
\
For my very first post in my new technical blog, I'm going to give an example how to make a github blog.
I've considered several tools for making my own blog and I decided to make a github blog. It's simple, easy to customize, and free hosted. I could learn some new web front-end skills which I haven't done yet.

1. What is Jekyll?\
-based blog. I'm now going to show how to make a new blog using jekyll and Github Pages. 

### What is Jekyll?
<img src="https://jekyllrb.com/img/logo-2x.png" alt="drawing" height="100"/>

- Jekyll is a simple, static, blog-aware framework website generator written in Ruby. You can refer to the [Jekyll docs](https://jekyllrb.com) or [Github repository](https://github.com/jekyll/jekyll).
- You can make your own blog in a very simple way using Jekyll, which can be easily hosted using [Github Pages](https://pages.github.com/). 
- 
## Let's get started


### 1. Download & Install Ruby
If you haven't installed Ruby, you have to install it first. From [here]([https://rubyinstaller.org/downloads/](https://rubyinstaller.org/downloads/)), I downloaded `Ruby+Devkit 2.6.6-2 (x64)` (because I have an 64-bit OS) and installed it with the default settings. If you have 32-bit OS, you can download one with `(x86)`.

### 2. Choose a Jekyll theme
You have hundreds of choices here (http://jekyllthemes.org/).\
You can look around the example website with the `demo` button. \
\
It was hard for me to choose one so I got some help from [Top 10 Jekyll Themes](https://jekyll-themes.com/blog/top-jekyll-themes/).
I chose the one on the top - [Kasper](https://jekyll-themes.com/kasper/), the simplest one.

### 3.  Fork the repository and rename it
//TODO
1. Fork and clone
[image1] - where the fork is
2. Download ZIP file
[image2] - how to download the zip file


You can make your own one by renaming the forked (or copied) repository, with `<username>.github.io`. or `<organization>.github.io` when it's owned by an organization. Now you can access to your own blog with the url `https://<username>.github.io`

### 4. Install Jekyll
There must be a `Gemfile` in your folder. Change directory to the folder containing `Gemfile`. Follow the commands below.
```
gem install jekyll
gem install jekyll-paginate
```
### 5. Change _config.yml
```
baseurl: ""
domain_name: "https://<username>.github.io"
```
### 6. How to use it

Build page and start local web server
```
jekyll serve
```

Build page into  `_site`  folder

```
jekyll build
```



[jekyll-gh]: https://github.com/mojombo/jekyll
[jekyll]:    http://jekyllrb.com
<!--stackedit_data:
eyJoaXN0b3J5IjpbNTg1OTcwMjU4LC01ODAxNDg2NDBdfQ==
-->
