from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class FlowChartNode(QObject):
    """流程图节点"""

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x, self.y = x, y  # 坐标
        self.w, self.h = 100, 100
        self.connected_nodes: list[FlowChartNode] = []  # 连接的节点
        self.attrs = {
            "A": 132,
            "B": "fdas"
        }  # 节点属性

    def draw(self, painter: QPainter, ox: int, oy: int):
        """绘制"""
        x = ox+self.x
        y = oy+self.y
        painter.drawRect(x, y, int(self.w), int(self.h))

        for node in self.connected_nodes:
            _x = ox+node.x
            _y = oy+node.y
            painter.drawLine(x, y, _x, _y)

    def connect_node(self, node: "FlowChartNode"):
        self.connected_nodes.append(node)

    def disconnect_node(self, node: "FlowChartNode"):
        if node in self.connected_nodes:
            self.connected_nodes.remove(node)
