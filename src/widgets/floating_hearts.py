from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QPainterPath, QColor
import random
import math

class FloatingHeart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.hearts = []
        self.setGeometry(0, 0, parent.width(), parent.height())
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.show()

    def add_heart(self):
        heart = {
            'x': random.randint(50, self.width() - 50),
            'y': self.height(),
            'size': random.randint(20, 40),
            'opacity': 1.0,
            'speed': random.uniform(1, 3),
            'wobble': random.uniform(-2, 2),
            'color': QColor(
                random.randint(200, 255),
                random.randint(20, 147),
                random.randint(100, 147),
                255
            )
        }
        self.hearts.append(heart)

    def start_animation(self):
        for _ in range(10):  # Create 10 hearts
            self.add_heart()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate_frame)
        self.timer.start(16)  # 60 FPS

    def animate_frame(self):
        any_visible = False
        for heart in self.hearts[:]:
            heart['y'] -= heart['speed']
            heart['x'] += heart['wobble'] * math.sin(heart['y'] / 30)
            heart['opacity'] -= 0.008
            
            if heart['opacity'] > 0:
                any_visible = True
            else:
                self.hearts.remove(heart)
                
        self.update()
        if not any_visible:
            self.timer.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for heart in self.hearts:
            color = heart['color']
            color.setAlpha(int(255 * heart['opacity']))
            painter.setBrush(color)
            painter.setPen(Qt.NoPen)

            path = QPainterPath()
            size = heart['size']
            x, y = heart['x'], heart['y']

            path.moveTo(x, y + size / 4)
            path.cubicTo(
                x - size / 2, y - size / 2,
                x - size, y + size / 4,
                x, y + size
            )
            path.cubicTo(
                x + size, y + size / 4,
                x + size / 2, y - size / 2,
                x, y + size / 4
            )

            painter.drawPath(path)