class StyleSheet:
    MAIN_WINDOW = """
        QMainWindow {
            background-color: white;
        }
    """
    
    CHAT_DISPLAY = """
        QTextEdit {
            background-color: rgba(255, 255, 255, 0.92);
            border: none;
            border-radius: 25px;
            padding: 20px;
            font-size: 14px;
            margin: 15px;
            color: #2C3E50;
        }
        QScrollBar:vertical {
            border: none;
            background: rgba(255, 255, 255, 0.1);
            width: 10px;
            margin: 0;
        }
        QScrollBar::handle:vertical {
            background: rgba(255, 107, 107, 0.5);
            min-height: 20px;
            border-radius: 5px;
        }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
    """
    
    MESSAGE_INPUT = """
        QTextEdit {
            background-color: rgba(255, 255, 255, 0.92);
            border: 2px solid rgba(255, 107, 107, 0.3);
            border-radius: 25px;
            padding: 12px 20px;
            font-size: 14px;
            margin: 10px;
            color: #2C3E50;
        }
        QTextEdit:focus {
            border: 2px solid #FF6B6B;
            background-color: white;
        }
    """
    
    SEND_BUTTON = """
        QPushButton {
            background-color: #FF6B6B;
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 30px;
            font-size: 14px;
            font-weight: bold;
            margin: 10px;
            min-width: 100px;
        }
        QPushButton:hover {
            background-color: #FF8787;
        }
        QPushButton:pressed {
            background-color: #FF5252;
        }
    """

    FEATURE_BUTTON = """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.92);
            color: #2C3E50;
            border: 2px solid #FF6B6B;
            border-radius: 20px;
            padding: 10px 20px;
            font-size: 13px;
            font-weight: bold;
            margin: 5px;
        }
        QPushButton:hover {
            background-color: #FF6B6B;
            color: white;
        }
    """

    EMOJI_BUTTON = """
        QPushButton {
            background-color: rgba(255, 255, 255, 0.92);
            border: 2px solid rgba(255, 107, 107, 0.3);
            border-radius: 25px;
            padding: 5px;
            font-size: 24px;
            min-width: 50px;
            min-height: 50px;
        }
        QPushButton:hover {
            border: 2px solid #FF6B6B;
            background-color: white;
        }
    """

    MENU_BAR = """
        QMenuBar {
            background-color: rgba(255, 255, 255, 0.92);
            border-bottom: 1px solid rgba(255, 107, 107, 0.3);
            padding: 5px;
        }
        QMenuBar::item {
            padding: 8px 15px;
            color: #2C3E50;
            border-radius: 15px;
            margin: 2px;
        }
        QMenuBar::item:selected {
            background-color: #FF6B6B;
            color: white;
        }
        QMenu {
            background-color: rgba(255, 255, 255, 0.95);
            border: 1px solid rgba(255, 107, 107, 0.3);
            border-radius: 10px;
            padding: 5px;
        }
        QMenu::item {
            padding: 8px 25px;
            border-radius: 5px;
        }
        QMenu::item:selected {
            background-color: #FF6B6B;
            color: white;
        }
    """

    LOVE_METER = """
        QProgressBar {
            border: none;
            border-radius: 10px;
            text-align: center;
            height: 20px;
            background-color: rgba(255, 107, 107, 0.1);
        }
        QProgressBar::chunk {
            background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #FF6B6B, stop:1 #FF8787);
            border-radius: 10px;
        }
    """

    CALENDAR = """
        QCalendarWidget {
            background-color: rgba(255, 255, 255, 0.92);
            border-radius: 15px;
        }
        QCalendarWidget QToolButton {
            color: #2C3E50;
            background-color: transparent;
            border: none;
            border-radius: 15px;
            padding: 5px;
            font-weight: bold;
        }
        QCalendarWidget QToolButton:hover {
            background-color: #FF6B6B;
            color: white;
        }
        QCalendarWidget QMenu {
            background-color: white;
            border: 1px solid #E0E0E0;
            border-radius: 5px;
        }
        QCalendarWidget QSpinBox {
            border: 1px solid #E0E0E0;
            border-radius: 5px;
            padding: 3px;
        }
        QCalendarWidget QTableView {
            selection-background-color: #FF6B6B;
            selection-color: white;
            alternate-background-color: rgba(255, 107, 107, 0.1);
        }
    """