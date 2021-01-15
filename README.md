###### LPR

2021.1.15 Open the topic  

*Author  Jier*  

*The maintenance email   Jwjier@gmail.com*  

License plate recognition and charging system of parking lot .  



###### INFO

The software development and running environment of the system are as follows.   
"operating system: MacOS, Windows 10.   
Python version: Python 3.7.  
Development tool: PyCharm 2020.   
"Python built-in modules: os, time, datetime.   
"third-party modules: opencv-python, pandas, matplotlib, pygame, baidu-aip, xlrd  



##### start

This project uses the API interface of Baidu Cloud AI. 
Therefore, you need to apply for the corresponding API permission first. The specific steps are as follows. 
(1) enter ai.baidu.com, in the address bar of a web browser (such as Chrome or Firefox) to go to Baidu Cloud AI's official website and click the blue "console" button. 
(2) go to the login page of Baidu Cloud AI official website, where you need to enter your Baidu account and password. If not, please click the "register now" hyperlink to apply. 
(3) after logging in successfully, go to the console page of Baidu Cloud AI official website, click "products and Services" in the left navigation, expand the list, and you can see the category of "artificial intelligence" at the bottom of the list. Select "Image recognition" in this category. 
(4) to enter the "Image recognition-Overview" page, you need to apply for permission to use the API, of Baidu Cloud AI, and you need to create your own application before applying for permission, so click "create Application". 
5) go to the "create Application" page, where you need to enter the name of the application, select the application type, select the interface to enter the application description, and click the "create now" button. 
(6) after the creation is completed, click the "return to App list" button, and the page jumps to the App list page, where you can view the created Apps and the values of AppID, API Key and Secret Key, automatically assigned to you by Baidu Cloud, which vary from application to application. Be sure to save them properly.