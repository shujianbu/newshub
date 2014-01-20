# Newshub

In today’s information-driven world, news websites publish several thousand stories a day. Many times, particularly in authoritarian regimes, changes are made to articles without any communication to readers. This can be due to political interference, or a nexus between the media and influential entities.  <br/>

We are building a system to track censorship and inappropriate journalistic practice post-publication. We embarked on this project because we wanted the public to be empowered and hold journalism accountable. The project has a special focus on Asian countries.  <br/>

The project has been funded through [Magic Grant](http://brown.stanford.edu/magic), awarded annually by the  [Brown Institue for Media Innovation](http://brown.columbia.edu/) , a collaboration between [Columbia University](http://www.columbia.edu/)  and [Stanford University](http://www.stanford.edu/) . 


### Localization

Translations of the guide are available in the following languages. 
* [Chinese Simplified](https://github.com/shujianbu/newshub/README-zhCN.md)
* [Chinese Traditional](https://github.com/shujianbu/newshub/README-zhTW.md)
* [Hindi](https://github.com/shujianbu/newshub/README-Hindi.md)

### Setup 

```Python
  
  # sync the database
  python website/manage.py syncdb 
  
  # migration
  python website/manage.py migrate  
  
```

### Browser Addon 

Newshub is expecting to have browser addons to allow users add articles they want to track. The Browser addon will indicate whether an article is already in our database and whether changes have been made to the article. Readers will be able to add new articles and publications to our database and receive email alerts if they wish to. 


### Findings & Reports 

We will also produce monthly reports and visualizations to help our readers better understand the data that we collect. Monthly reports will highlight publications that make major changes to their online articles with both stories and visualizations. We will also write individual stories on substantial changes related to important news events.


### Team 

Newshub is the joint effort of the following Columbia graduates:

* Shujian Bu, sb3331@columbia.edu
* Yue Qiu, yq2154@columbia.edu 
* Yi Du, yd2257@columbia.edu 
* Anirvan Ghosh, ag3299@columbia.edu
* Sophie Chou, sbc2125@columbia.edu


### Contribution 

Eric Price, Newsdiffs; <br/>
Jonathan Stray, Fellow at Columbia Graduate School of Journalism;<br/>
Mark Hansen, Director of Brown Institute for Media Innovation, Columbia Graduate School of Journalism; <br/>
Scott Klein, Senior Editor at ProPublica;<br/>
Shi-fu Chang, Senior Vice Dean of Engineering, Fu Foundation School  of Engineering and Applied Sciences, Columbia University; <br/>
Sisi Wei, News Application Developer at ProPublica; <br/>
Sravan Bhamitipati, recent graduate from Fu Foundation School  of Engineering and Applied Sciences, Columbia University.


### Contact Us

We welcome suggestions and questions on publication selection, data interpretation, algorithm, etc. Please contact us at info@newshub.cc. 


### License
![Creative Commons License](http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png)
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike CC BY-NC-SA License 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/)




