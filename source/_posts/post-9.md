---
title: 《微信聊天分身》
date: 2025-04-22 21:42:43
tags:
    - mlx
    - lora
    - wechat
    - chroma
    - rag
category: article
author: 周文喆
toc: true
---

起因是朋友认识了个异地的男生，但是表白失败了，我寻思亲不到摸不着跟ai有啥区别，加上以前玩微信机器人，所以打算以他俩的聊天记录模拟一个微信号给她。
（以前用的itchat协议被封了，这次换大佬弄的ipad协议）
<!--more-->
## 导出微信聊天记录

### 找到聊天记录位置

```bash
open ~/Library/Containers/com.tencent.xinWeChat/Data/Library/Application\ Support/com.tencent.xinWeChat/2.0b4.0.9
```

### 逆向微信

1、查看 SIP 状态

```bash
csrutil status
```

2、进入 Recovery 模式

3、关闭 SIP

```bash
csrutil disable
```

4、attach到运行的 WeChat

```bash
lldb -p <pid>
```

```bash
br set -n sqlite3_key
```

```bash
c
```

```bash
memory read --size 1--format
```

5、获取密钥

### 查看数据

![图片标题](2.png)

## 对模型进行微调

### 数据处理

```json
{"prompt": "你好呀", "completion": "你好"}
{"prompt": "我是朋友介绍的 请问你要找对象吗 想认识一下可以吗", "completion": "6"}
{"prompt": "本来还想谈个恋爱 居然这么快就被识破了", "completion": "我有防撤回…"}
{"prompt": "好吧 其实我也想跟你咨询一下显卡的 可以吗 听说你好像是学计算机之类的专业", "completion": "我不是计算机的…"}
{"prompt": "可以吗", "completion": "下班了，回去再说"}
```

### 量化模型

```bash
➜  ~/Code/mlx-lm git:(main) ✗ mlx_lm.convert --hf-path Qwen/Qwen2.5-14B-Instruct --mlx-path Qwen2.5-14B-mlx -q
[INFO] Loading
Fetching 15 files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 15/15 [00:00<00:00, 28301.65it/s]
[INFO] Quantizing
[INFO] Quantized model with 4.501 bits per weight.
```

### 训练

```bash
➜  ~/Code/mlx-lm git:(main) ✗ mlx_lm.lora --model Qwen2.5-14B-mlx --train --iters 600  --data data --batch-size 1 --num-layers 4 

Loading pretrained model
Loading datasets
Training
Trainable parameters: 0.004% (0.524M/14770.034M)
Starting training..., iters: 600
Iter 1: Val loss 4.594, Val took 8.173s
Iter 10: Train loss 4.793, Learning Rate 1.000e-05, It/sec 1.693, Tokens/sec 31.829, Trained Tokens 188, Peak mem 8.422 GB
```

### 启动服务(openai api规范)

```bash
➜  ~/Code/mlx-lm git:(main) ✗ mlx_lm.server
2025-04-30 09:41:18,822 - INFO - Starting httpd at 127.0.0.1 on port 8080...
```

## 接入向量数据库

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

![图片标题](3.png)
