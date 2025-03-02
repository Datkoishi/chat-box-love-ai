from PyQt5.QtWidgets import QPushButton, QMenu
from PyQt5.QtCore import pyqtSignal
import emoji

class EmojiPicker(QPushButton):
    emoji_selected = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__('😊', parent)
        self.setFixedSize(50, 50)
        self.init_ui()
        
    def init_ui(self):
        self.menu = QMenu(self)
        
        # Common emojis
        common_emojis = ['😊', '😍', '🥰', '💕', '💗', '💓', '💖', '💝', '😘', '🤗']
        
        for emoji_char in common_emojis:
            action = self.menu.addAction(emoji_char)
            action.triggered.connect(lambda checked, e=emoji_char: self.on_emoji_selected(e))
            
        self.setMenu(self.menu)
        
    def on_emoji_selected(self, emoji_char):
        parent = self.parent()
        if parent and hasattr(parent, 'message_input'):
            current_text = parent.message_input.toPlainText()
            parent.message_input.setPlainText(current_text + emoji_char)