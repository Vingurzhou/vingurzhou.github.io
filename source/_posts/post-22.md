---
title: 《让ai使用工具》
author: 周文喆
toc: true
date: 2025-05-12 14:50:03
tags:
    - ai
    - dify
    - mcp
category: article 
---   
dify并不是什么插件都有，只能自己开发一个mcp来实现功能了
<!-- more -->

## mcp

### 服务端

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def execute_cmd(cmd: str) -> list[dict]:
    """
    
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
                'execute_cmd', {
                    'cmd': 'ls'})
            print(res)


if __name__ == '__main__':
    asyncio.run(main())
```

## 最终效果
