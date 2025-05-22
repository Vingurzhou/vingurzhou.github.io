---
title: 《0基础翻唱歌曲》
date: 2025-05-08 20:38:00
tags:
    - rvc
    - svc
    - ai
category: article
author: 周文喆
toc: true
---
博主很喜欢唱歌，但是五音不全，又想听自己唱好听是什么样的，就尝试ai翻唱，但用了全民k歌等应用的ai翻唱效果都不太好，只好自己用ai翻唱了
<!--more-->

## 训练模型

### 采集样本

## 人声/伴奏分离和混响消除

```shell
Input #0, mp3, from '/var/folders/jz/8mpn380d50n8n02n0mb2qh1w0000gn/T/gradio/e63c888ad9912b4139f98811d6119d3d48f68b48/c001155e608726f19a19b643230dfcaa.mp3':
  Metadata:
    major_brand     : mp42
    minor_version   : 1
    compatible_brands: isommp41mp42
    copyright-eng   :
    encoder         : Lavf56.15.102
  Duration: 00:00:18.00, start: 0.025057, bitrate: 64 kb/s
  Stream #0:0: Audio: mp3 (mp3float), 44100 Hz, mono, fltp, 64 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (mp3 (mp3float) -> pcm_s16le (native))
Press [q] to stop, [?] for help
Output #0, wav, to '/Users/zhouwenzhe/Code/Retrieval-based-Voice-Conversion-WebUI/TEMP/c001155e608726f19a19b643230dfcaa.mp3.reformatted.wav':
  Metadata:
    major_brand     : mp42
    minor_version   : 1
    compatible_brands: isommp41mp42
    copyright-eng   :
    ISFT            : Lavf61.7.100
  Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 44100 Hz, stereo, s16, 1411 kb/s
      Metadata:
        encoder         : Lavc61.19.101 pcm_s16le
[out#0/wav @ 0x600002390000] video:0KiB audio:3096KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.002460%
size=    3096KiB time=00:00:17.97 bitrate=1411.2kbits/s speed=1.59e+03x
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:03<00:00,  1.98it/s]
2025-05-22 16:44:37 | INFO | infer.modules.uvr5.vr | c001155e608726f19a19b643230dfcaa.mp3.reformatted.wav instruments done
2025-05-22 16:44:37 | INFO | infer.modules.uvr5.vr | c001155e608726f19a19b643230dfcaa.mp3.reformatted.wav vocals done
```

* 音频文件:

<audio controls>
  <source src="c001155e608726f19a19b643230dfcaa.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

* 人声:

<audio controls>
  <source src="vocal_c001155e608726f19a19b643230dfcaa.mp3.reformatted.wav_10.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

* 伴奏:

<audio controls>
  <source src="instrument_c001155e608726f19a19b643230dfcaa.mp3.reformatted.wav_10.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

## 模型推理

## 最终效果

<audio controls>
  <source src="audio.wav" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
