from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QTextEdit, QPushButton, QLabel, QFrame,
                           QLineEdit)
from PyQt5.QtCore import Qt, QTimer, QTime
import random
import emoji

from .widgets.message_animation import MessageAnimation
from .widgets.love_features import LoveFeatures
from .widgets.emoji_picker import EmojiPicker
from .data.topics import LoveTopics
from .ui.styles import StyleSheet, LoveTheme

class ChatLoveAI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.love_meter_value = 50
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Chat Love AI')
        self.setStyleSheet(StyleSheet.MAIN_WINDOW)
        self.setMinimumSize(1400, 800)
        
        # Main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Left sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(80)
        sidebar.setStyleSheet(StyleSheet.SIDEBAR)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 15, 10, 15)
        sidebar_layout.setSpacing(15)
        
        # Logo/Home button
        home_btn = QPushButton("❤️")
        home_btn.setFixedSize(60, 60)
        home_btn.setStyleSheet(StyleSheet.SIDEBAR_BUTTON)
        sidebar_layout.addWidget(home_btn)
        
        # Navigation buttons
        nav_buttons = [
            ("💌", "Tin nhắn yêu thương"),
            ("💝", "Câu chuyện tình"),
            ("💑", "Hẹn hò"),
            ("💘", "Tìm kiếm tình yêu"),
            ("💖", "Yêu thích")
        ]
        
        for icon, tooltip in nav_buttons:
            btn = QPushButton(icon)
            btn.setFixedSize(60, 60)
            btn.setStyleSheet(StyleSheet.SIDEBAR_BUTTON)
            btn.setToolTip(tooltip)
            sidebar_layout.addWidget(btn)
        
        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar)
        
        # Chat container
        chat_container = QWidget()
        chat_container.setStyleSheet("""
            QWidget {
                background-color: #F0F2F5;
            }
        """)
        chat_layout = QVBoxLayout(chat_container)
        chat_layout.setContentsMargins(0, 0, 0, 0)
        chat_layout.setSpacing(0)
        
        # Chat header
        header = QWidget()
        header.setFixedHeight(80)
        header.setStyleSheet("""
            QWidget {
                background: #FFFFFF;
                border-bottom: 1px solid #E4E6EB;
            }
        """)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(30, 0, 30, 0)
        
        # AI Info
        ai_info = QHBoxLayout()
        ai_avatar = QLabel("❤️")
        ai_avatar.setFixedSize(50, 50)
        ai_avatar.setStyleSheet("""
            QLabel {
                background-color: #F0F2F5;
                color: black;
                border-radius: 25px;
                font-size: 24px;
            }
        """)
        ai_avatar.setAlignment(Qt.AlignCenter)
        ai_info.addWidget(ai_avatar)
        
        ai_text = QVBoxLayout()
        ai_name = QLabel("Chat Love AI")
        ai_name.setStyleSheet("color: black; font-size: 16px; font-weight: bold;")
        ai_status = QLabel("Đang hoạt động")
        ai_status.setStyleSheet("color: #65676B; font-size: 13px;")
        ai_text.addWidget(ai_name)
        ai_text.addWidget(ai_status)
        ai_info.addLayout(ai_text)
        header_layout.addLayout(ai_info)
        
        header_layout.addStretch()
        chat_layout.addWidget(header)
        
        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet(StyleSheet.CHAT_DISPLAY)
        chat_layout.addWidget(self.chat_display)
        
        # Input area
        input_container = QWidget()
        input_container.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                border-top: 1px solid #E4E6EB;
            }
        """)
        input_layout = QHBoxLayout(input_container)
        input_layout.setContentsMargins(20, 15, 20, 15)
        input_layout.setSpacing(15)
        
        # Message input frame
        input_frame = QFrame()
        input_frame.setStyleSheet(StyleSheet.INPUT_FRAME)
        input_frame_layout = QHBoxLayout(input_frame)
        input_frame_layout.setContentsMargins(15, 5, 15, 5)
        input_frame_layout.setSpacing(10)
        
        # Text input
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Aa")
        self.message_input.setStyleSheet(StyleSheet.MESSAGE_INPUT)
        self.message_input.returnPressed.connect(self.send_message)
        input_frame_layout.addWidget(self.message_input)
        
        # Emoji picker
        self.emoji_picker = EmojiPicker(self)
        input_frame_layout.addWidget(self.emoji_picker)
        
        input_layout.addWidget(input_frame)
        
        # Send button
        send_btn = QPushButton("Gửi")
        send_btn.setFixedSize(60, 36)
        send_btn.setStyleSheet(StyleSheet.SEND_BUTTON)
        send_btn.clicked.connect(self.send_message)
        input_layout.addWidget(send_btn)
        
        chat_layout.addWidget(input_container)
        main_layout.addWidget(chat_container)
        
        # Initialize message animation
        self.message_animation = MessageAnimation(self.chat_display)
        
        # Welcome message
        self.message_animation.display_bot_message(
            "Xin chào! Mình là Chat Love AI. Bạn có thể chia sẻ với mình bất cứ điều gì về tình yêu nhé! 💕"
        )

    def send_message(self):
        message = self.message_input.text().strip()
        if message:
            self.message_animation.display_user_message(emoji.emojize(message))
            self.message_input.clear()
            QTimer.singleShot(1000, lambda: self.generate_response(message))

    def generate_response(self, user_message):
        message_lower = user_message.lower()
        
        is_positive = any(word in message_lower for word in LoveTopics.KEYWORDS['positive'])
        is_negative = any(word in message_lower for word in LoveTopics.KEYWORDS['negative'])
        is_question = any(word in message_lower for word in LoveTopics.KEYWORDS['question'])
        
        if is_question:
            response = random.choice(LoveTopics.RESPONSES['question'])
        elif is_positive:
            response = random.choice(LoveTopics.RESPONSES['positive'])
        elif is_negative:
            response = random.choice(LoveTopics.RESPONSES['negative'])
        else:
            response = random.choice(LoveTopics.RESPONSES['neutral'])
        
        if random.random() < 0.3:
            response += f"\n\n{random.choice(LoveTopics.QUOTES)}"
        
        self.message_animation.display_bot_message(response)