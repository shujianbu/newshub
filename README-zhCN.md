# Newshub —— 让新闻更可靠


在今天这样一个信息爆炸的时代, 新闻网站每日刊登数以千计的文章.很多时候，网站在不告知读者的情况下擅自更改或删除已经刊登的文章。这背后的原因有时是公司、财团的贿赂，有时是政府的新闻审查。 <br/>

Newhushub是一个帮助读者监督新闻网站的平台。我们正在努力搭建这个平台，使读者可以实时跟踪新闻网站对文章做出的改动，参与到监督新闻媒体的行动中来，让新闻变得更可靠，我们的关注重点是亚洲国家的网络媒体。

这个项目由布朗媒体创新中心（ [Brown Institue for Media Innovation](http://brown.columbia.edu/) ）的 [Magic Grant](http://brown.stanford.edu/magic)支持。布朗媒体创新中心是哥伦比亚大学（ [Columbia University](http://www.columbia.edu/) ） and 和斯坦福大学（[Stanford University](http://www.stanford.edu/) ）的合作项目，旨在鼓励新媒体环境下的媒体创新. 

了解更多请访问: http://brown.stanford.edu/magic

### Localization

请参阅如下语言. 
* [英语](https://github.com/shujianbu/newshub/blob/master/README.md)
* [印度语](https://github.com/shujianbu/newshub/blob/master/README-hindi.md)

### Set Up

```Python
  
  # sync the database
  python website/manage.py syncdb 
  
  # migration
  python website/manage.py migrate  
  
```

### Browser Addon 

我们将会设计浏览器插件，让读者能够将他们感兴趣的文章和网站加入到我们的数据库中。浏览器插件会以不同颜色告知读者一篇文章是否已经在我们的数据库中、网站是否对这一文章进行过更改。读者也可以自己设置提示等级，收到有关文章变化的邮件提示。


### Findings & Reports 

我们将撰写月度报告，为读者解读这一个月来我们收集到的数据，用故事和可视化的形式展现网络媒体在更改文章上的表现。我们也会针对热点新闻事件撰写独立的故事。

### Team 

我们的团队由哥伦比亚大学新闻学院和机械与应用科学学院的毕业生组成。我们是：

[Shujian Bu](mailto:sb3331@columbia.edu), [Yue Qiu](mailto:yq2154@columbia.edu), [Yi Du](mailto:yd2257@columbia.edu), [Anirvan Ghost](mailto:ag3299@columbia.edu), [Sophie Chou](mailto:sbc2125@columbia.edu)


### Contribution 

感谢[Eric Price](mailto:ecprice@mit.edu), [Greg Price](mailto:gnprice@gmail.com), 和 [Jennifer 8. Lee](mailto:jenny@jennifer8lee.com) 与我们分享 [Newsdiff](http://newsdiffs.org/)的源代码。感谢哥伦比亚大学[Mark Hansen](http://www.journalism.columbia.edu/profile/428-mark)教授和 [Shih-Fu Chang](http://www.ee.columbia.edu/shih-fu-chang)教授的帮助和支持。 同时感谢ProPublica的 [Scott Klein](https://twitter.com/kleinmatic) 和 [Sisi Wei](https://twitter.com/sisiwei)。 Sravan Bhamitipati 对本项目亦有贡献。


### Contact Us

我们欢迎关于算法设计、数据分析、网站选取等各方面的问题和建议。如果你知道媒体行为失范或政府审查干预的故事, 请联系我们 [info@newshub.cc](mailto:info@newshub.cc)


### License
![Creative Commons License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike CC BY-NC-SA License 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/)

