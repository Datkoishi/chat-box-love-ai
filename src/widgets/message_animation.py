from PyQt5.QtCore import QTimer

class MessageAnimation:
    def __init__(self, text_edit):
        self.text_edit = text_edit
        
    def animate_message(self, message, is_user=False):
        style = "user" if is_user else "bot"
        html = f'''
            <div style="
                text-align: {'right' if is_user else 'left'};
                margin: 10px;
            ">
                <span style="
                    display: inline-block;
                    background-color: {'#DCF8C6' if is_user else 'white'};
                    color: #2C3E50;
                    padding: 10px 15px;
                    border-radius: 15px;
                    max-width: 80%;
                    word-wrap: break-word;
                ">
                    {message}
                </span>
            </div>
        '''
        
        current_html = self.text_edit.toHtml()
        new_html = current_html[:-14] + html + "</body></html>"
        self.text_edit.setHtml(new_html)
        
        # Auto scroll
        scrollbar = self.text_edit.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())