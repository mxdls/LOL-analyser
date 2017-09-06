---
#LOL-analyser
-------------

> 关于我，欢迎关注  
  博客：[NOVA的小站](http://www.novadva.top/) 

## 项目简介 ##
项目目的是实现对lol战绩的爬取，然后对战绩进行分析，训练一个用于预测战局胜利方的机器学习模型。<br>
战局信息用MySQL存储。神经网络初步使用keras+tensorflow后端进行训练。

## 更新日志 ##
**2017.9.5**<br>
重写战局统计功能，对简单的神经网络用7W条排位信息训练，效果不佳，严重过拟合<br>
**2017.9.4**<br>
增加统计战局英雄到二进制文件功能<br>
**2017.9.3**<br>
统计战局插入的数量和重复的数量，输出重复的比例<br>
**2017.9.1**<br>
修复获取json时出现的错误，优化数据获取逻辑<br>
**2017.8.18**<br>
增加项目介绍，增加多线程功能<br>


## 使用方法 ##
**user：**<br>
- 按用户名查找用户<br>
- 更新用户信息<br>

**battle：**<br>
- 按用户和区获取战绩列表<br>
- 获取战局详细信息<br>

**spider：**<br>
- 随机按用户爬取对局信息，保存到数据库<br>
- 多线程爬取数据，包括战局信息和用户信息<br>

**query：**<br>
- 显示统计信息<br>

**make_train_test：**<br>
- 生成供网络训练用的二进制文件，参数n为测试集大小<br>

## 后续部分 ##
完成预测部分
完善爬虫功能
增添数据分析模块
