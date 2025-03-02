from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QProgressBar, 
                           QLabel, QPushButton, QDialog, QCalendarWidget,
                           QHBoxLayout)
from PyQt5.QtCore import Qt, QDate, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor, QPalette
from ..ui.styles import StyleSheet
import random
import math

class LoveMeter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setup_animations()
        
    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.92);
                border-radius: 20px;
                padding: 10px;
            }
        """)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        
        # Create label
        self.label = QLabel("Độ rung động 💗")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            QLabel {
                color: #FF6B6B;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        layout.addWidget(self.label)
        
        # Create progress bar
        self.progress = QProgressBar()
        self.progress.setStyleSheet(StyleSheet.LOVE_METER)
        self.progress.setRange(0, 100)
        self.progress.setValue(50)  # Initial value
        layout.addWidget(self.progress)
        
        self.current_value = 50

    def setup_animations(self):
        self.value_animation = QPropertyAnimation(self.progress, b"value")
        self.value_animation.setDuration(1000)
        self.value_animation.setEasingCurve(QEasingCurve.OutElastic)

    def update_love_meter(self):
        new_value = random.randint(50, 100)
        
        # Animate progress bar
        self.value_animation.setStartValue(self.current_value)
        self.value_animation.setEndValue(new_value)
        self.value_animation.start()
        
        # Update label with animation
        if new_value > 80:
            text = "Độ rung động 💗 (Rất đáng yêu!)"
            color = "#FF4081"
        elif new_value > 60:
            text = "Độ rung động 💗 (Đang phát triển tốt!)"
            color = "#FF6B6B"
        else:
            text = "Độ rung động 💗 (Hãy tiếp tục trò chuyện!)"
            color = "#FF8787"
            
        self.label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: 16px;
                font-weight: bold;
                transition: color 0.3s ease;
            }}
        """)
        self.label.setText(text)
        
        self.current_value = new_value

class LoveCalendar(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("Nhật ký tình yêu 📅")
        self.setStyleSheet(StyleSheet.CALENDAR)
        self.setMinimumSize(400, 500)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Create title
        title = QLabel("Nhật ký tình yêu 💕")
        title.setStyleSheet("""
            QLabel {
                color: #FF6B6B;
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Create calendar
        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.date_clicked)
        layout.addWidget(self.calendar)
        
        # Create note label
        self.note_label = QLabel("Chọn một ngày để ghi lại kỷ niệm đẹp ❤️")
        self.note_label.setAlignment(Qt.AlignCenter)
        self.note_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                padding: 15px;
                background-color: rgba(255, 107, 107, 0.3);
                border-radius: 15px;
                margin: 10px;
            }
        """)
        layout.addWidget(self.note_label)

    def date_clicked(self, date):
        special_dates = {
            QDate(2024, 2, 14): "Valentine's Day 🌹",
            QDate(2024, 3, 8): "Ngày Quốc tế Phụ nữ 🌸",
            QDate(2024, 5, 20): "Ngày của Tình yêu 💑",
            QDate(2024, 10, 20): "Ngày Phụ nữ Việt Nam 💐",
            QDate(2024, 12, 24): "Đêm Giáng sinh 🎄",
            QDate(2024, 12, 31): "Đêm Giao thừa ✨"
        }
        
        if date in special_dates:
            message = f"Hôm nay là {special_dates[date]}"
            style = """
                background-color: rgba(255, 107, 107, 0.5);
                color: white;
            """
        else:
            message = "Hãy tạo kỷ niệm đẹp cho ngày này ✨"
            style = """
                background-color: rgba(255, 255, 255, 0.3);
                color: white;
            """
            
        self.note_label.setText(message)
        self.note_label.setStyleSheet(f"""
            QLabel {{
                font-size: 14px;
                padding: 15px;
                border-radius: 15px;
                margin: 10px;
                {style}
            }}
        """)

class LoveQuotes:
    @staticmethod
    def get_random_quote():
        quotes = [
            "Yêu không phải là nhìn nhau, mà là cùng nhau nhìn về một hướng 💑",
            "Tình yêu không cần phải hoàn hảo, chỉ cần chân thành 💕",
            "Có những người đến trong đời, khiến ta nhận ra cuộc sống thật đẹp 🌟",
            "Yêu là cho đi mà không cần nhận lại 🎁",
            "Tình yêu không phải là tìm được người hoàn hảo, mà là học cách yêu một người không hoàn hảo một cách hoàn hảo 💖",
            "Đôi khi, một ánh mắt đủ làm rung động cả trái tim 👀💗",
            "Hạnh phúc đơn giản là được ở bên người mình yêu 🥰",
            "Tình yêu không cần lý do, vì chính nó là lý do 💝",
            "Yêu là khi hạnh phúc của người ấy trở thành hạnh phúc của mình 💑",
            "Có những người, chỉ cần gặp một lần đã khiến ta nhớ cả đời 💭",
            "Tình yêu là khi trái tim đập nhanh hơn mỗi khi nghĩ về nhau 💓",
            "Yêu là chấp nhận mọi khuyết điểm của nhau 🫂",
            "Tình yêu làm cho cuộc sống thêm nhiều màu sắc 🌈",
            "Hạnh phúc là được nắm tay nhau đi đến cuối con đường 👫",
            "Yêu là khi có thể cười với nhau về những điều nhỏ nhặt 😊"
        ]
        return random.choice(quotes)