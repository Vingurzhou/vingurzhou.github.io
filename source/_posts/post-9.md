---
title: 《通过ai实现微信聊天分身》
date: 2025-04-22 21:42:43
tags:
    - ai
    - wechat
    - gewe
    - docker
    - sqlite
category: article
timeline: article
author: 周文喆
toc: true
---

起因是朋友认识了个异地的男生，但是表白失败了，我寻思亲不到摸不着跟ai有啥区别，加上以前玩微信机器人，所以打算以他俩的聊天记录模拟一个微信号给她。
（以前用的itchat协议被封了，这次换大佬弄的ipad协议）
<!--more-->
## 导出微信聊天记录

### 找到聊天记录位置

```shell
open ~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application\ Support/com.tencent.xinWeChat/2.0b4.0.9
```

### 数据库解密

1. 查看 SIP 状态

```shell
csrutil status
```

2. 进入 Recovery 模式

3. 关闭 SIP

```shell
csrutil disable
```

4. attach到运行的 WeChat

```shell
lldb -p <pid>
```

```shell
br set -n sqlite3_key
```

```
c
```

```
memory read --size 1--format
```

6. 查看数据

## 对模型进行微调

### 导入聊天记录

![图片标题](2.png)

### 选择模型

![图片标题](3.png)

### 训练

![图片标题](4.png)

## 微信接入ai

### 部署gewe→[GitHub](https://github.com/Vingurzhou/deploy/blob/main/docker-compose.yml#L119)

![图片标题](1.png)

### 设置回调接口

```bash
curl --location --request POST 'http://127.0.0.1:2531/v2/api/tools/setCallback' \
--header 'X-GEWE-TOKEN: 1a856e3f100e48bbaf8ff3cb68bfe3d8' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token": "1a856e3f100e48bbaf8ff3cb68bfe3d8",
    "callbackUrl": "http://www.baidu.com"
}'
```

### 编写接口逻辑→[GitHub](https://github.com/Vingurzhou/wechat-robot/blob/main/internal/logic/callbacklogic.go)

## 最终效果

效果很差😓，大家别看我的帖子了～
