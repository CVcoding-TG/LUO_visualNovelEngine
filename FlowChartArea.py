import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from FlowChartNode import *


class NodeAttrEditor(QWidget):
    """节点属性编辑器"""
    __instances = {}
    __new_counts = {}

    def __new__(cls, node: FlowChartNode, *args):
        if node not in cls.__instances:
            cls.__instances[node] = super().__new__(cls)
            cls.__new_counts[node] = 0
        cls.__new_counts[node] += 1
        return cls.__instances[node]

    def __init__(self, node: FlowChartNode, parent=None):
        if self.__new_counts[node] > 1:
            return
        super().__init__(parent)
        self.node = node
        self._layout = QGridLayout(self)
        self.attr_refresh = {}  # 属性对应的刷新方式

        for i, name in enumerate(self.node.attrs):
            l_name = QLabel()
            l_name.setText(name)
            self._layout.addWidget(l_name, i, 0)

            val = self.node.attrs[name]
            if isinstance(val, int):
                w_val = QSpinBox()
                w_val.setMaximum(2**31-1)
                w_val.setMinimum(-2**31)
                w_val.setValue(val)
                w_val.valueChanged.connect(
                    lambda _, n=name, w=w_val: self.setAttr(n, w.value))
                self.attr_refresh[name] = w_val.value
            elif isinstance(val, str):
                w_val = QLineEdit()
                w_val.setText(val)
                w_val.textChanged.connect(
                    lambda _, n=name, w=w_val: self.setAttr(n, w.text))
                self.attr_refresh[name] = w_val.text
            self._layout.addWidget(w_val, i, 1)

    def refresh(self):
        for key, val in self.attr_refresh.items():
            self.node.attrs[key] = val()

    def setAttr(self, name, val_getter):
        self.node.attrs[name] = val_getter()


class FlowChartArea(QWidget):
    """流程图区域"""

    def __init__(self) -> None:
        super().__init__()
        self.ox, self.oy = 0, 0  # 原点坐标
        self.nodes: list[FlowChartNode] = []  # 流程图中的节点
        self.cur_node: FlowChartNode = None  # 当前节点
        self.nodeattreditor: NodeAttrEditor = None  # 节点属性编辑器
        self.last_mousepos = None  # 上一个鼠标位置
        self.addNode()
        self.addNode()
        self.nodes[0].connect_node(self.nodes[1])

    def addNode(self, x=0, y=0):
        """添加节点"""
        self.nodes.append(FlowChartNode(x, y))

    def getNodeAt(self, x: int, y: int):
        """获取(x,y)位置的节点"""
        for node in self.nodes:
            if self.ox+node.x <= x <= self.ox+node.x+node.w and self.oy+node.y <= y <= self.oy+node.y+node.h:
                return node

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)
        for node in self.nodes:
            node.draw(painter, self.ox, self.oy)
        return super().paintEvent(a0)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.cur_node = self.getNodeAt(a0.x(), a0.y())
        self.last_mousepos = (a0.x(), a0.y())
        if self.cur_node != None:
            self.nodeattreditor = NodeAttrEditor(self.cur_node)
            self.nodeattreditor.show()
            self.nodeattreditor.activateWindow()
        return super().mousePressEvent(a0)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        dx = a0.x()-self.last_mousepos[0]
        dy = a0.y()-self.last_mousepos[1]
        if self.cur_node:
            self.cur_node.x += dx
            self.cur_node.y += dy
        else:
            self.ox += dx
            self.oy += dy
        self.repaint()
        self.last_mousepos = (a0.x(), a0.y())
        return super().mouseMoveEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    flowchartarea = FlowChartArea()
    flowchartarea.show()
    app.exec()
