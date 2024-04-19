
<h1 align="center">
<b>nicegui-g6</b>
</h1>

基于 AntV [G6](https://github.com/antvis/g6) 可视化引擎的一个 [NiceGUI](https://github.com/zauberzeug/nicegui) 组件 。


## 🔨 开始

要安装 `nicegui-g6`，在终端中运行以下命令：

```bash
pip install nicegui-g6
```

要使用 nicegui-g6，您只需导入 g6 函数并将图形数据传递给它。以下是一个示例：

```python
from nicegui_g6 import g6
from nicegui import ui

# 定义图形数据
# 您可以参考 G6 文档了解更多细节。
data = {
    "nodes": [
        {
            "id": "node1",
            "x": 100,
            "y": 200,
        },
        {
            "id": "node2",
            "x": 300,
            "y": 200,
        },
    ],
    "edges": [
        {
            "source": "node1",
            "target": "node2",
        },
    ],
}

g6(data)

ui.run()
```
