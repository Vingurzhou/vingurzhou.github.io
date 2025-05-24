---
title: 《0成本让ai联网》
author: 周文喆
toc: true
date: 2025-05-12 14:50:03
tags:
    - ai
    - dify
    - selenium
    - spider
    - mcp
category: article 
---
找了好多sdk，要么限量要么付费。于是我琢磨了个白嫖的方法，缺点是扛不住并发，但个人用肯定够了
<!-- more -->
## 爬虫选型

| 特性                | Requests                          | Selenium                          | Google Custom Search JSON API       |
|---------------------|-----------------------------------|-----------------------------------|-------------------------------------|
| **速度**            | 快（纯 HTTP 请求）                | 慢（需渲染浏览器）                | 中等（API 调用）                    |
| **资源占用**        | 低（无浏览器）                    | 高（需运行浏览器）                | 低（仅网络请求）                    |
| **动态内容处理**    | 否（仅静态 HTML）                 | 是（可渲染 JavaScript）           | 否（仅返回 API 数据）               |
| **反爬机制应对**    | 需手动配置 headers/代理           | 较强（模拟用户行为）              | 无需担心（官方 API）                |
| **结果格式**        | HTML（需解析）                    | HTML（需解析）                    | JSON（结构化）                      |
| **合法性**          | 易违反服务条款                   | 易违反服务条款                   | 完全合法                            |
| **成本**            | 免费                              | 免费                              | 免费 100 次/天，超额付费           |

## 数据爬取

### 启动chrome
<!-- ## 下载引擎

### [查看Version](chrome://settings/help)

### [下载ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) -->
```shell
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome  --remote-debugging-port=9222 --user-data-dir="/Users/zhouwenzhe/Code/mcp-server/profiles"
```

### 爬取

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/search?q=上海的天气如何")
with open("output.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)
```

## 数据清理

```python
from bs4 import BeautifulSoup

with open("output.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

results = []
for item in soup.select("div.tF2Cxc"):
    title_tag = item.select_one("h3")
    link_tag = item.select_one("a")
    snippet_tag = item.select_one(".VwiC3b") or item.select_one(".aCOpRe")

    title = title_tag.get_text(strip=True) if title_tag else ""
    link = link_tag['href'] if link_tag else ""
    snippet = snippet_tag.get_text(strip=True) if snippet_tag else ""

    if title and link:
        results.append({
            "标题": title,
            "链接": link,
            "摘要": snippet
        })
print(results)
```

## mcp

### 服务端

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def search_google(query: str) -> list[dict]:
    """
    使用 Google 搜索指定关键词，并返回前几个搜索结果的标题、链接和摘要。
    """

mcp.run(transport='sse')
```

### 客户端

```python
import asyncio
from mcp.client.sse import sse_client
from mcp import ClientSession


async def main():
    async with sse_client('http://127.0.0.1:8000/sse') as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            res = await session.call_tool(
                'search_google', {
                    'query': 'OpenAI'})
            print(res)


if __name__ == '__main__':
    asyncio.run(main())
```

## 最终效果

```shell
➜  ~/Code/mcp-server python client.py
meta=None content=[
TextContent(type='text', text='{\n  "标题": "OpenAI",\n  "链接": "https://openai.com/",\n  "摘要": "Video showing miniature diorama scenes of toy-like characters interacting in various settings, emphasizing. Your browser does not support the video tag."\n}', annotations=None),
TextContent(type='text', text='{\n  "标题": "OpenAI - Wikipedia",\n  "链接": "https://en.wikipedia.org/wiki/OpenAI",\n  "摘要": ""\n}', annotations=None)
] isError=False
```
