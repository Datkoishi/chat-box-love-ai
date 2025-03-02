class LoveTheme:
    # Colors
    PRIMARY = "#0084FF"
    SECONDARY = "#E4E6EB"
    BACKGROUND = "#F0F2F5"
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    GRAY = "#65676B"
    
    # Message colors
    USER_MESSAGE_BG = "#E3F2FD"
    BOT_MESSAGE_BG = "#FFFFFF"
    
    # Font sizes
    FONT_SMALL = "13px"
    FONT_NORMAL = "14px"
    FONT_LARGE = "16px"

class StyleSheet:
    MAIN_WINDOW = f"""
        QMainWindow {{
            background-color: {LoveTheme.BACKGROUND};
        }}
    """
    
    SIDEBAR = f"""
        QWidget {{
            background-color: {LoveTheme.WHITE};
            border-right: 1px solid {LoveTheme.SECONDARY};
        }}
    """
    
    SIDEBAR_BUTTON = f"""
        QPushButton {{
            background-color: {LoveTheme.BACKGROUND};
            border: none;
            border-radius: 8px;
            padding: 5px;
            font-size: 22px;
        }}
        QPushButton:hover {{
            background-color: {LoveTheme.SECONDARY};
        }}
    """
    
    CHAT_DISPLAY = f"""
        QTextEdit {{
            border: none;
            background-color: {LoveTheme.BACKGROUND};
            padding: 10px;
            font-size: {LoveTheme.FONT_NORMAL};
            color: {LoveTheme.BLACK};
        }}
        QScrollBar:vertical {{
            border: none;
            background: transparent;
            width: 8px;
            margin: 0px;
        }}
        QScrollBar::handle:vertical {{
            background: rgba(0, 0, 0, 0.2);
            min-height: 30px;
            border-radius: 4px;
        }}
        QScrollBar::handle:vertical:hover {{
            background: rgba(0, 0, 0, 0.3);
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: none;
        }}
    """
    
    INPUT_FRAME = f"""
        QFrame {{
            background-color: {LoveTheme.BACKGROUND};
            border-radius: 20px;
        }}
    """
    
    MESSAGE_INPUT = f"""
        QLineEdit {{
            background-color: transparent;
            border: none;
            padding: 8px;
            font-size: {LoveTheme.FONT_NORMAL};
            color: {LoveTheme.BLACK};
        }}
        QLineEdit::placeholder {{
            color: {LoveTheme.GRAY};
        }}
    """
    
    SEND_BUTTON = f"""
        QPushButton {{
            background-color: {LoveTheme.PRIMARY};
            color: {LoveTheme.WHITE};
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: {LoveTheme.FONT_NORMAL};
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: #006ACD;
        }}
        QPushButton:pressed {{
            background-color: #0055A4;
        }}
    """