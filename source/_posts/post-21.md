---
title: 《mac装机必备》
date: 2022-05-08 20:38:00
tags:
    - mac
category: article
author: 周文喆
toc: true
cover: /image/4.webp
---
Mac 拥有苹果自研芯片和 macOS 系统的深度整合，提供流畅的用户体验、高效能耗比、强大的安全性和优秀的图形处理能力，尤其适合创意设计、视频剪辑和开发等专业场景，同时生态系统闭环良好，设备间协作便捷。
<!-- more -->
## Automator

macOS 自带的自动化工具，帮助你批量处理重复任务或创建工作流。

## iTerm

功能强大的终端替代品，支持分屏、主题、自定义等高级功能。

### brew

macOS 上最流行的包管理器，用于安装、更新、卸载命令行工具和 GUI 应用。

### mux

终端复用工具 tmux 的配置增强方案，通常指的是 tmux-mux 或个人自定义脚本，用于管理多会话窗口和布局。

### zsh

比 bash 更现代的 shell，支持自动补全、插件系统与更强的脚本功能。

### neofetch

```shell
➜  ~ neofetch
                    'c.          zhouwenzhe@MacBook-Pro.local
                 ,xNMM.          ----------------------------
               .OMMMMo           OS: macOS 15.4.1 24E263 arm64
               OMMM0,            Host: MacBookPro17,1
     .;loddo:' loolloddol;.      Kernel: 24.4.0
   cKMMMMMMMMMMNWMMMMMMMMMM0:    Uptime: 4 days, 19 hours, 18 mins
 .KMMMMMMMMMMMMMMMMMMMMMMMWd.    Packages: 174 (brew)
 XMMMMMMMMMMMMMMMMMMMMMMMX.      Shell: zsh 5.9
;MMMMMMMMMMMMMMMMMMMMMMMM:       Resolution: 1440x900
:MMMMMMMMMMMMMMMMMMMMMMMM:       DE: Aqua
.MMMMMMMMMMMMMMMMMMMMMMMMX.      WM: Quartz Compositor
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.    WM Theme: Blue (Light)
 .XMMMMMMMMMMMMMMMMMMMMMMMMMMk   Terminal: iTerm2
  .XMMMMMMMMMMMMMMMMMMMMMMMMK.   Terminal Font: MesloLGS-NF-Regular 13
    kMMMMMMMMMMMMMMMMMMMMMMd     CPU: Apple M1
     ;KMMMMMMMWXXWMMMMMMMk.      GPU: Apple M1
       .cooc,.    .,coo:.        Memory: 2614MiB / 16384MiB
```

### pyenv

Python 多版本管理工具，可轻松切换和管理不同的 Python 版本。

```shell
➜  ~ pyenv versions
  system
  3.8.20
  3.9.20
* 3.10.14 (set by /Users/zhouwenzhe/.python-version)
  3.12.9
```

### gvm

Go 语言版本管理工具，便于安装、切换和卸载不同版本的 Go。

```shell
➜  ~ gvm list
gvm gos (installed)
   go1.16
   go1.18
=> go1.21
   go1.23.3
   system
```

### nvm

Node.js 版本管理工具，方便开发者在多个项目间切换不同版本。

```shell
➜  ~ nvm list
       v14.21.3
->     v16.20.2
       v18.20.4
        v23.1.0
```

## Cursor

基于 GPT 的 AI 编程编辑器，主打智能补全与代码生成。

## Chrome

谷歌出品的现代浏览器，速度快、插件丰富、兼容性强。

### Global Speed

浏览器视频加速插件，支持任意网站自定义播放速度。

### Tampermonkey

强大的用户脚本管理器，用于加载和管理自定义网页脚本。

### Google Translate

谷歌翻译扩展，支持快速网页翻译与划词翻译。

## Android Studio

官方 Android 开发环境，内置模拟器和调试工具，适合 Android 应用开发。

### emulator

Android 模拟器，用于测试和运行不同设备和系统版本的虚拟机。

```bash
emulator -avd Pixel_XL_API_33
```

## Xcode

苹果官方开发工具，适用于 macOS 与 iOS 应用开发。

### Simulator Location

Xcode 模拟器支持通过 GPX 文件模拟设备的地理位置，用于测试定位功能。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1">
    <wpt lat="30.95041019601779" lon="121.9134707195439">
        <name>China Shanghai Weizhan Road</name>
    </wpt>
</gpx>
```

## OrbStack

轻量虚拟化工具，支持运行 Linux 容器和虚拟机，替代 Docker Desktop 的新选择。

## Shadowrocket

iOS 上的强大代理工具，支持多种协议和规则，适合网络调试与科学上网。
