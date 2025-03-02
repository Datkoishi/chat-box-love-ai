from PyQt5.QtWidgets import QPushButton, QMenu
from PyQt5.QtCore import pyqtSignal

class EmojiPicker(QPushButton):
    emoji_selected = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__('😊', parent)
        self.setFixedSize(40, 40)
        self.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 20px;
                font-size: 22px;
            }
            QPushButton:hover {
                background-color: rgba(255, 107, 149, 0.2);
            }
        """)
        self.init_ui()
        
    def init_ui(self):
        self.menu = QMenu(self)
        
        # Common love emojis
        love_emojis = ['😊', '😍', '🥰', '💕', '💗', '💓', '💖', '💝', '😘', '🤗',
                      '❤️', '💘', '💌', '💞', '💟', '💑', '💏', '👩‍❤️‍👨', '💋', '🌹']
        
        for emoji_char in love_emojis:
            action = self.menu.addAction(emoji_char)
            action.triggered.connect(lambda checked, e=emoji_char: self.on_emoji_selected(e))
            
        self.setMenu(self.menu)
        
    def on_emoji_selected(self, emoji_char):
        parent = self.parent()
        if parent and hasattr(parent, 'message_input'):
            current_text = parent.message_input.text()
            parent.message_input.setText(current_text + emoji_char)