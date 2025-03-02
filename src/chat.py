from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QTextEdit, QPushButton, QMenuBar, QMenu, QAction,
                           QLabel, QFrame, QScrollArea, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer, QSize, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap
from .widgets.heart_widget import HeartAnimation
from .widgets.emoji_picker import EmojiPicker
from .widgets.message_animation import MessageAnimation
from .widgets.love_features import LoveMeter, LoveCalendar, LoveQuotes
from .data.topics import load_topics
from .data.emotions import load_emotions
from .ui.styles import StyleSheet
import random
import emoji

class ChatBubble(QFrame):
    def __init__(self, message, is_user=False, parent=None):
        super().__init__(parent)
        self.is_user = is_user
        self.init_ui(message)
        
    def init_ui(self, message):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        
        if not self.is_user:
            # Bot avatar
            avatar_label = QLabel()
            avatar_pixmap = QPixmap("src/assets/bot_avatar.png")
            if avatar_pixmap.isNull():
                # Fallback if image not found
                avatar_label.setText("🤖")
                avatar_label.setStyleSheet("""
                    QLabel {
                        background: #FF6B6B;
                        border-radius: 20px;
                        padding: 10px;
                        font-size: 20px;
                    }
                """)
            else:
                avatar_pixmap = avatar_pixmap.scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                avatar_label.setPixmap(avatar_pixmap)
            avatar_label.setFixedSize(40, 40)
            layout.addWidget(avatar_label)

        # Message content
        message_container = QFrame()
        message_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        message_layout = QVBoxLayout(message_container)
        message_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add name for bot messages
        if not self.is_user:
            name_label = QLabel("Love AI")
            name_label.setStyleSheet("""
                QLabel {
                    color: #FF6B6B;
                    font-weight: bold;
                    font-size: 12px;
                    margin-bottom: 2px;
                }
            """)
            message_layout.addWidget(name_label)
        
        # Message text
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setStyleSheet(f"""
            QLabel {{
                background-color: {'#DCF8C6' if self.is_user else 'white'};
                border-radius: 15px;
                padding: 10px 15px;
                font-size: 14px;
                color: #2C3E50;
            }}
        """)
        message_layout.addWidget(message_label)
        
        # Time stamp
        time_label = QLabel("Vừa xong")
        time_label.setStyleSheet("""
            QLabel {
                color: #999;
                font-size: 11px;
                margin-top: 2px;
            }
        """)
        message_layout.addWidget(time_label)
        
        if self.is_user:
            layout.addStretch()
        layout.addWidget(message_container)
        if not self.is_user:
            layout.addStretch()

class ChatArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        # Container widget
        self.container = QWidget()
        self.container.setStyleSheet("""
            QWidget {
                background-color: #F0F2F5;
            }
        """)
        
        # Layout for messages
        self.layout = QVBoxLayout(self.container)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 10, 0, 10)
        self.layout.addStretch()
        
        # Set up scroll area
        self.setWidget(self.container)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: #F0F2F5;
            }
            QScrollBar:vertical {
                border: none;
                background: #F0F2F5;
                width: 10px;
                margin: 0;
            }
            QScrollBar::handle:vertical {
                background: rgba(0, 0, 0, 0.2);
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
    def add_message(self, message, is_user=False):
        bubble = ChatBubble(message, is_user)
        self.layout.insertWidget(self.layout.count() - 1, bubble)
        self.scroll_to_bottom()
        
    def scroll_to_bottom(self):
        QTimer.singleShot(100, lambda: self.verticalScrollBar().setValue(
            self.verticalScrollBar().maximum()
        ))

class ChatLoveAI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topics = load_topics()
        self.emotions = load_emotions()
        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.show_typing_animation)
        self.is_typing = False
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Chat Love AI 💕')
        self.setStyleSheet(StyleSheet.MAIN_WINDOW)
        self.setMinimumSize(800, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create header
        self.create_header(layout)
        
        # Create chat area
        self.chat_area = ChatArea()
        layout.addWidget(self.chat_area)
        
        # Create input area
        self.create_input_area(layout)
        
        # Send welcome message
        self.display_welcome_message()
        
    def create_header(self, layout):
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background-color: white;
                border-bottom: 1px solid #E4E6EB;
            }
        """)
        header.setFixedHeight(60)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(15, 0, 15, 0)
        
        # Bot info
        info_layout = QHBoxLayout()
        
        avatar_label = QLabel("🤖")
        avatar_label.setStyleSheet("""
            QLabel {
                background: #FF6B6B;
                border-radius: 20px;
                padding: 10px;
                font-size: 20px;
            }
        """)
        avatar_label.setFixedSize(40, 40)
        info_layout.addWidget(avatar_label)
        
        text_layout = QVBoxLayout()
        
        name_label = QLabel("Love AI")
        name_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #1C1E21;
            }
        """)
        text_layout.addWidget(name_label)
        
        status_label = QLabel("Đang hoạt động")
        status_label.setStyleSheet("""
            QLabel {
                color: #65676B;
                font-size: 13px;
            }
        """)
        text_layout.addWidget(status_label)
        
        info_layout.addLayout(text_layout)
        header_layout.addLayout(info_layout)
        
        # Add buttons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        for icon in ["📞", "📹", "ℹ️"]:
            button = QPushButton(icon)
            button.setFixedSize(40, 40)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #F0F2F5;
                    border-radius: 20px;
                    font-size: 18px;
                }
                QPushButton:hover {
                    background-color: #E4E6EB;
                }
            """)
            buttons_layout.addWidget(button)
            
        header_layout.addLayout(buttons_layout)
        layout.addWidget(header)
        
    def create_input_area(self, layout):
        input_frame = QFrame()
        input_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-top: 1px solid #E4E6EB;
            }
        """)
        input_layout = QHBoxLayout(input_frame)
        input_layout.setContentsMargins(15, 10, 15, 10)
        
        # Add emoji picker
        emoji_button = QPushButton("😊")
        emoji_button.setFixedSize(40, 40)
        emoji_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border-radius: 20px;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: #F0F2F5;
            }
        """)
        input_layout.addWidget(emoji_button)
        
        # Add message input
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Nhắn tin...")
        self.message_input.setFixedHeight(40)
        self.message_input.setStyleSheet("""
            QTextEdit {
                background-color: #F0F2F5;
                border: none;
                border-radius: 20px;
                padding: 10px 15px;
                font-size: 14px;
            }
        """)
        input_layout.addWidget(self.message_input)
        
        # Add send button
        send_button = QPushButton("Gửi")
        send_button.setFixedSize(60, 40)
        send_button.setStyleSheet("""
            QPushButton {
                background-color: #0084FF;
                color: white;
                border: none;
                border-radius: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0073E6;
            }
        """)
        send_button.clicked.connect(self.send_message)
        input_layout.addWidget(send_button)
        
        layout.addWidget(input_frame)
        
    def show_typing_animation(self):
        if self.is_typing:
            self.typing_dots = (self.typing_dots + 1) % 4
            dots = "." * self.typing_dots
            self.chat_area.add_message(f"Đang nhập{dots}", False)
            
    def display_welcome_message(self):
        welcome_messages = [
            "Xin chào! Hãy chia sẻ với tôi điều bạn đang cảm thấy 💕",
            "Rất vui được gặp bạn! Hãy trò chuyện về tình yêu nhé 💝",
            "Chào bạn! Tôi ở đây để lắng nghe và chia sẻ cùng bạn 🌟"
        ]
        self.chat_area.add_message(random.choice(welcome_messages), False)
        
    def send_message(self):
        message = self.message_input.toPlainText().strip()
        if message:
            # Display user message
            self.chat_area.add_message(message, True)
            
            # Clear input
            self.message_input.clear()
            
            # Start typing animation
            self.is_typing = True
            self.typing_dots = 0
            self.typing_timer.start(500)
            
            # Generate and display bot response after delay
            QTimer.singleShot(2000, lambda: self.generate_response(message))
            
    def generate_response(self, user_message):
        # Stop typing animation
        self.is_typing = False
        self.typing_timer.stop()
        
        # Analyze message sentiment
        love_keywords = {
            'positive': ['yêu', 'thích', 'vui', 'hạnh phúc', 'tuyệt vời', 'nhớ', 'thương', 'quan tâm', 'ngọt ngào'],
            'negative': ['buồn', 'chán', 'khó', 'cô đơn', 'thất tình', 'chia tay', 'giận'],
            'question': ['làm sao', 'thế nào', 'tại sao', 'có nên', 'bằng cách nào']
        }

        message_lower = user_message.lower()
        
        # Analyze message type
        is_positive = any(word in message_lower for word in love_keywords['positive'])
        is_negative = any(word in message_lower for word in love_keywords['negative'])
        is_question = any(word in message_lower for word in love_keywords['question'])
        
        # Generate appropriate response
        if is_question:
            response = random.choice(self.topics['advice'])
        elif is_positive:
            response = random.choice(self.topics['positive'])
        elif is_negative:
            response = random.choice(self.topics['comfort'])
        else:
            response = random.choice(self.topics['neutral'])
            
        # Add random quote
        if random.random() < 0.3:  # 30% chance to add quote
            response += f"\n\n{LoveQuotes.get_random_quote()}"
            
        # Add emotion
        emotion = random.choice(self.emotions)
        response = f"{response} {emotion}"
        
        # Display response
        self.chat_area.add_message(response, False)