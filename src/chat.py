from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                           QTextEdit, QPushButton, QLabel, QFrame, QScrollArea, 
                           QSizePolicy, QSpacerItem)
from PyQt5.QtCore import Qt, QTimer, QSize, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap
import random
import emoji
import datetime

class MessengerStyle:
    # Colors
    PRIMARY_BLUE = "#0099FF"
    LIGHT_GRAY = "#F0F2F5"
    DARK_TEXT = "#050505"
    SECONDARY_TEXT = "#65676B"
    WHITE = "#FFFFFF"
    HOVER_GRAY = "#E4E6EB"
    
    # Dimensions
    SIDEBAR_WIDTH = 320
    HEADER_HEIGHT = 64
    INPUT_HEIGHT = 44
    
    # Styles
    MAIN_WINDOW = f"""
        QMainWindow {{
            background-color: {WHITE};
        }}
    """
    
    SIDEBAR = f"""
        QWidget {{
            background-color: {WHITE};
            border-right: 1px solid #E4E6EB;
        }}
    """
    
    CHAT_AREA = f"""
        QScrollArea {{
            background-color: {WHITE};
            border: none;
        }}
        QScrollBar:vertical {{
            border: none;
            background: {WHITE};
            width: 8px;
            margin: 0;
        }}
        QScrollBar::handle:vertical {{
            background: #BCC0C4;
            min-height: 30px;
            border-radius: 4px;
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
    """
    
    INPUT_AREA = f"""
        QFrame {{
            background-color: {WHITE};
            border-top: 1px solid #E4E6EB;
        }}
    """
    
    MESSAGE_INPUT = f"""
        QTextEdit {{
            background-color: {LIGHT_GRAY};
            border: none;
            border-radius: 20px;
            padding: 12px 12px;
            font-size: 15px;
            color: {DARK_TEXT};
        }}
    """
    
    SEND_BUTTON = f"""
        QPushButton {{
            background-color: transparent;
            border: none;
            padding: 8px;
            qproperty-iconSize: 24px 24px;
        }}
        QPushButton:hover {{
            background-color: {LIGHT_GRAY};
            border-radius: 50%;
        }}
    """

class ChatBubble(QFrame):
    def __init__(self, message, is_user=False, parent=None):
        super().__init__(parent)
        self.is_user = is_user
        self.init_ui(message)
        
    def init_ui(self, message):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 2, 16, 2)
        layout.setSpacing(8)
        
        if not self.is_user:
            # Bot avatar
            avatar_frame = QFrame()
            avatar_frame.setFixedSize(28, 28)
            avatar_frame.setStyleSheet(f"""
                QFrame {{
                    background-color: {MessengerStyle.PRIMARY_BLUE};
                    border-radius: 14px;
                    margin-right: 8px;
                }}
            """)
            avatar_layout = QHBoxLayout(avatar_frame)
            avatar_layout.setContentsMargins(0, 0, 0, 0)
            
            avatar_label = QLabel("AI")
            avatar_label.setStyleSheet("""
                QLabel {
                    color: white;
                    font-weight: bold;
                    font-size: 12px;
                }
            """)
            avatar_label.setAlignment(Qt.AlignCenter)
            avatar_layout.addWidget(avatar_label)
            
            layout.addWidget(avatar_frame)
        else:
            layout.addSpacerItem(QSpacerItem(36, 1))
        
        # Message container
        message_container = QFrame()
        message_container.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        message_layout = QVBoxLayout(message_container)
        message_layout.setContentsMargins(0, 0, 0, 0)
        message_layout.setSpacing(2)
        
        # Message text
        message_frame = QFrame()
        message_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {MessengerStyle.PRIMARY_BLUE if self.is_user else MessengerStyle.LIGHT_GRAY};
                border-radius: 18px;
                padding: 8px 12px;
            }}
        """)
        message_frame_layout = QVBoxLayout(message_frame)
        message_frame_layout.setContentsMargins(8, 8, 8, 8)
        
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setStyleSheet(f"""
            QLabel {{
                color: {'white' if self.is_user else MessengerStyle.DARK_TEXT};
                font-size: 15px;
                line-height: 20px;
            }}
        """)
        message_frame_layout.addWidget(message_label)
        message_layout.addWidget(message_frame)
        
        # Time stamp
        time_label = QLabel(datetime.datetime.now().strftime("%H:%M"))
        time_label.setStyleSheet(f"""
            QLabel {{
                color: {MessengerStyle.SECONDARY_TEXT};
                font-size: 12px;
                margin-top: 2px;
            }}
        """)
        time_label.setAlignment(Qt.AlignLeft if not self.is_user else Qt.AlignRight)
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
        self.setStyleSheet(MessengerStyle.CHAT_AREA)
        
        # Container widget
        self.container = QWidget()
        self.container.setStyleSheet(f"background-color: {MessengerStyle.WHITE};")
        
        # Layout for messages
        self.layout = QVBoxLayout(self.container)
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(0, 20, 0, 20)
        self.layout.addStretch()
        
        # Set up scroll area
        self.setWidget(self.container)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
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
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Messenger')
        self.setStyleSheet(MessengerStyle.MAIN_WINDOW)
        self.setMinimumSize(950, 650)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add sidebar
        self.create_sidebar(main_layout)
        
        # Create chat container
        chat_container = QWidget()
        chat_layout = QVBoxLayout(chat_container)
        chat_layout.setSpacing(0)
        chat_layout.setContentsMargins(0, 0, 0, 0)
        
        # Add header
        self.create_header(chat_layout)
        
        # Add chat area
        self.chat_area = ChatArea()
        chat_layout.addWidget(self.chat_area)
        
        # Add input area
        self.create_input_area(chat_layout)
        
        main_layout.addWidget(chat_container)
        
        # Send welcome message
        self.display_welcome_message()
        
    def create_sidebar(self, layout):
        sidebar = QWidget()
        sidebar.setFixedWidth(MessengerStyle.SIDEBAR_WIDTH)
        sidebar.setStyleSheet(MessengerStyle.SIDEBAR)
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        
        # Search bar
        search_container = QFrame()
        search_container.setFixedHeight(MessengerStyle.HEADER_HEIGHT)
        search_container.setStyleSheet(f"background-color: {MessengerStyle.WHITE};")
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(16, 8, 16, 8)
        
        search_frame = QFrame()
        search_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {MessengerStyle.LIGHT_GRAY};
                border-radius: 50px;
                padding: 8px 16px;
            }}
        """)
        search_frame_layout = QHBoxLayout(search_frame)
        search_frame_layout.setContentsMargins(0, 0, 0, 0)
        
        search_icon = QLabel("🔍")
        search_text = QLabel("Tìm kiếm trên Messenger")
        search_text.setStyleSheet(f"""
            QLabel {{
                color: {MessengerStyle.SECONDARY_TEXT};
                font-size: 15px;
            }}
        """)
        search_frame_layout.addWidget(search_icon)
        search_frame_layout.addWidget(search_text)
        search_layout.addWidget(search_frame)
        
        sidebar_layout.addWidget(search_container)
        
        # Chats list
        chats_label = QLabel("Chat")
        chats_label.setStyleSheet("""
            QLabel {
                font-size: 17px;
                font-weight: bold;
                padding: 16px;
            }
        """)
        sidebar_layout.addWidget(chats_label)
        
        # Active chat
        active_chat = QFrame()
        active_chat.setStyleSheet(f"""
            QFrame {{
                background-color: {MessengerStyle.LIGHT_GRAY};
                border-radius: 8px;
                margin: 0 8px;
            }}
        """)
        active_chat_layout = QHBoxLayout(active_chat)
        
        chat_avatar = QLabel("AI")
        chat_avatar.setFixedSize(56, 56)
        chat_avatar.setStyleSheet(f"""
            QLabel {{
                background-color: {MessengerStyle.PRIMARY_BLUE};
                color: white;
                border-radius: 28px;
                font-weight: bold;
                font-size: 20px;
            }}
        """)
        chat_avatar.setAlignment(Qt.AlignCenter)
        
        chat_info = QVBoxLayout()
        chat_name = QLabel("Love AI")
        chat_name.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 15px;
            }
        """)
        chat_preview = QLabel("Đang hoạt động")
        chat_preview.setStyleSheet(f"""
            QLabel {{
                color: {MessengerStyle.SECONDARY_TEXT};
                font-size: 13px;
            }}
        """)
        chat_info.addWidget(chat_name)
        chat_info.addWidget(chat_preview)
        
        active_chat_layout.addWidget(chat_avatar)
        active_chat_layout.addLayout(chat_info)
        active_chat_layout.addStretch()
        
        sidebar_layout.addWidget(active_chat)
        sidebar_layout.addStretch()
        
        layout.addWidget(sidebar)
        
    def create_header(self, layout):
        header = QFrame()
        header.setFixedHeight(MessengerStyle.HEADER_HEIGHT)
        header.setStyleSheet(f"""
            QFrame {{
                background-color: {MessengerStyle.WHITE};
                border-bottom: 1px solid {MessengerStyle.LIGHT_GRAY};
            }}
        """)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(16, 0, 16, 0)
        
        # Chat info
        chat_info = QHBoxLayout()
        
        avatar = QLabel("AI")
        avatar.setFixedSize(40, 40)
        avatar.setStyleSheet(f"""
            QLabel {{
                background-color: {MessengerStyle.PRIMARY_BLUE};
                color: white;
                border-radius: 20px;
                font-weight: bold;
                font-size: 16px;
            }}
        """)
        avatar.setAlignment(Qt.AlignCenter)
        chat_info.addWidget(avatar)
        
        info = QVBoxLayout()
        name = QLabel("Love AI")
        name.setStyleSheet("""
            QLabel {
                font-weight: bold;
                font-size: 15px;
            }
        """)
        status = QLabel("Đang hoạt động")
        status.setStyleSheet(f"""
            QLabel {{
                color: {MessengerStyle.SECONDARY_TEXT};
                font-size: 13px;
            }}
        """)
        info.addWidget(name)
        info.addWidget(status)
        chat_info.addLayout(info)
        
        header_layout.addLayout(chat_info)
        header_layout.addStretch()
        
        # Header buttons
        for icon in ["📞", "📹", "ℹ️"]:
            button = QPushButton(icon)
            button.setFixedSize(36, 36)
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {MessengerStyle.LIGHT_GRAY};
                    border-radius: 18px;
                    font-size: 18px;
                }}
                QPushButton:hover {{
                    background-color: {MessengerStyle.HOVER_GRAY};
                }}
            """)
            header_layout.addWidget(button)
            
        layout.addWidget(header)
        
    def create_input_area(self, layout):
        input_frame = QFrame()
        input_frame.setStyleSheet(MessengerStyle.INPUT_AREA)
        input_layout = QHBoxLayout(input_frame)
        input_layout.setContentsMargins(16, 12, 16, 12)
        input_layout.setSpacing(8)
        
        # Add buttons before input
        for icon in ["➕", "📷", "😊"]:
            button = QPushButton(icon)
            button.setFixedSize(36, 36)
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: 18px;
                    font-size: 20px;
                }}
                QPushButton:hover {{
                    background-color: {MessengerStyle.LIGHT_GRAY};
                }}
            """)
            input_layout.addWidget(button)
        
        # Add message input
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Aa")
        self.message_input.setFixedHeight(MessengerStyle.INPUT_HEIGHT)
        self.message_input.setStyleSheet(MessengerStyle.MESSAGE_INPUT)
        input_layout.addWidget(self.message_input)
        
        # Add send button
        send_button = QPushButton("➤")
        send_button.setFixedSize(36, 36)
        send_button.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border-radius: 18px;
                font-size: 20px;
                color: {MessengerStyle.PRIMARY_BLUE};
            }}
            QPushButton:hover {{
                background-color: {MessengerStyle.LIGHT_GRAY};
            }}
        """)
        send_button.clicked.connect(self.send_message)
        input_layout.addWidget(send_button)
        
        layout.addWidget(input_frame)
        
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
            self.chat_area.add_message(message, True)
            self.message_input.clear()
            QTimer.singleShot(1000, lambda: self.generate_response(message))
            
    def generate_response(self, user_message):
        responses = [
            "Tôi hiểu cảm xúc của bạn 💕",
            "Hãy chia sẻ thêm với tôi nhé! 🌟",
            "Tình yêu thật tuyệt vời, phải không? 💝",
            "Đôi khi ta cần thời gian để hiểu rõ trái tim mình 💭",
            "Hãy luôn giữ niềm tin vào tình yêu nhé! ✨"
        ]
        self.chat_area.add_message(random.choice(responses), False)