# wechat_bot
微信聊天机器人

原文见[把聊天机器人接入微信](http://blog.just4fun.site/create-wechat-bot.html)


另外如果你要使用中文语料库，参考[构建自己的智能聊天机器人](http://blog.just4fun.site/create-a-smart-chat-bot.html)

经@sunchenguang同学提醒，项目中的wxbot有问题（成旧），建议大家使用官方最新的，我个人已经迁往itchat，所以就不在此从上游库更新，除此微信通讯部分外，其他流程和原理依然可用

# usage
### 运行bot api
安装依赖：pip3 install hug ，chatterbot的安装方法参考[构建自己的智能聊天机器人](http://blog.just4fun.site/create-a-smart-chat-bot.html)


运行：`hug -f bot_api.py`

测试：`http://127.0.0.1:8000/get_response?user_input=你好`

### 连接微信
参考[把聊天机器人接入微信](http://blog.just4fun.site/create-wechat-bot.html)

# 开始聊天

这是程序收到的消息
![](http://oav6fgfj1.bkt.clouddn.com/botaed8c5a1.png)

这是被机器人接管的聊天界面

![](http://oav6fgfj1.bkt.clouddn.com/wechat_bot6055328f.png)


