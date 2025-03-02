from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtGui import QPainter, QPainterPath, QColor
import random

class HeartAnimation(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.hearts = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        
    def start(self):
        self.hearts = []
        for _ in range(5):  # Create 5 hearts
            self.hearts.append({
                'x': random.randint(0, self.parent.width()),
                'y': self.parent.height(),
                'speed': random.uniform(1, 3)
            })
        self.show()
        self.timer.start(50)  # Update every 50ms
        
    def update_animation(self):
        any_visible = False
        for heart in self.hearts:
            heart['y'] -= heart['speed']
            if heart['y'] > -20:  # Heart is still visible
                any_visible = True
                
        if not any_visible:
            self.timer.stop()
            self.hide()
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        for heart in self.hearts:
            self.draw_heart(painter, heart['x'], heart['y'])
            
    def draw_heart(self, painter, x, y):
        path = QPainterPath()
        
        # Define heart shape
        path.moveTo(x, y + 10)
        path.cubicTo(x - 7, y - 8, x - 25, y + 10, x, y + 25)
        path.cubicTo(x + 25, y + 10, x + 7, y - 8, x, y + 10)
        
        # Set color with transparency
        color = QColor(255, 20, 147, 150)  # Pink with alpha
        painter.fillPath(path, color)