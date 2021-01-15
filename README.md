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

###### 本项目使用了百度云 AI 的 API 接口实现。因此需要先申请对应的 API 使用权限，具体步骤如下。  

(1)在网页浏览器(比如 Chrome 或者火狐)的地址栏中输入 ai.baidu.com，进入到百度云 AI 的官网， 点击蓝色“控制台”按钮。  
(2)进入到百度云 AI 官网的登录页面，该页面中需要输入百度账号和密码，如果没有，请单击“立即注册”超链接进行申请。  
(3)登录成功后，进入到百度云 AI 官网的控制台页面，单击左侧导航中的“产品服务”，展开列表， 在列表的最右侧下方看到有“人工智能”的分类，该分类中选择“图像识别”。  
(4)进入“图像识别 - 概览”页面，要使用百度云 AI 的 API，首先需要申请权限，申请权限之前需要先创建自己的应用，因此单击“创建应用”。  
5)进入到“创建应用”页面，该页面中需要输入应用的名称，选择应用类型，并选择接口输入应用描述，单击“立即创建”按钮。  
(6)创建完成后，单击“返回应用列表”按钮，页面跳转到应用列表页面，该页面中即可查看创建的应用，以及百度云自动为您分配的 AppID、API Key、Secret Key，这些值根据应用的不同而不同，一定要妥善保存。

 