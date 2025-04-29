---
title: 《通过ai实现微信聊天分身》
date: 2025-04-22 21:42:43
tags:
    - mlx
    - lora
    - wechat
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

### 数据库解密

1. 查看 SIP 状态

```bash
csrutil status
```

2. 进入 Recovery 模式

3. 关闭 SIP

```bash
csrutil disable
```

4. attach到运行的 WeChat

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

6. 查看聊天记录

## 对模型进行微调

### 数据集

train.jsonl

```json
{"text": "Q: 你在干嘛\nA: 在睡觉"}
{"text": "Q: 你喜欢做什么\nA: 我喜欢看电影"}
```

valid.jsonl

```json
{"text": "Q: 你在干嘛\nA: 在睡觉"}
{"text": "Q: 你喜欢做什么\nA: 我喜欢看电影"}
```

### 转换Hugging Face模型

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

### 推理

```bash
➜  ~/Code/mlx-lm git:(main) ✗ mlx_lm.generate --model Qwen2.5-14B-mlx --adapter-path adapters --prompt "你在干嘛"
==========
我是来自阿里云的超大规模语言模型，我正在为你提供高质量的文本生成服务。
==========
Prompt: 31 tokens, 197.861 tokens-per-sec
Generation: 21 tokens, 128.193 tokens-per-sec
Peak memory: 0.318 GB
```

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
