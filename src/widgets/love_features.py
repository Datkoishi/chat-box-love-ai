from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                           QProgressBar, QFrame)
from PyQt5.QtCore import Qt
import random

class LoveFeatures(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)
        
        # Love Story Section
        story_label = QLabel("💕 Câu chuyện tình yêu")
        story_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        layout.addWidget(story_label)
        
        # Love Quote Frame
        quote_frame = QFrame()
        quote_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 107, 149, 0.1);
                border-radius: 15px;
                padding: 15px;
            }
        """)
        quote_layout = QVBoxLayout(quote_frame)
        
        quote_title = QLabel("💌 Trích dẫn tình yêu")
        quote_title.setStyleSheet("color: white; font-weight: bold;")
        quote_layout.addWidget(quote_title)
        
        self.quote_text = QLabel("Tình yêu không cần phải hoàn hảo, chỉ cần chân thành...")
        self.quote_text.setWordWrap(True)
        self.quote_text.setStyleSheet("color: rgba(255, 255, 255, 0.8);")
        quote_layout.addWidget(self.quote_text)
        
        layout.addWidget(quote_frame)
        
        # Love Tips Frame
        tips_frame = QFrame()
        tips_frame.setStyleSheet("""
            QFrame {
                background: rgba(255, 107, 149, 0.1);
                border-radius: 15px;
                padding: 15px;
            }
        """)
        tips_layout = QVBoxLayout(tips_frame)
        
        tips_title = QLabel("💝 Lời khuyên về tình yêu")
        tips_title.setStyleSheet("color: white; font-weight: bold;")
        tips_layout.addWidget(tips_title)
        
        self.tips_text = QLabel(
            "1. Hãy luôn chân thành\n"
            "2. Lắng nghe và thấu hiểu\n"
            "3. Tôn trọng lẫn nhau"
        )
        self.tips_text.setWordWrap(True)
        self.tips_text.setStyleSheet("color: rgba(255, 255, 255, 0.8);")
        tips_layout.addWidget(self.tips_text)
        
        layout.addWidget(tips_frame)
        layout.addStretch()

    def update_quote(self, quote: str):
        self.quote_text.setText(quote)

    def update_tips(self, tips: str):
        self.tips_text.setText(tips)