from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import QTime

class HieuUngTinNhan:
    def __init__(self, text_edit: QTextEdit):
        self.text_edit = text_edit
        self._thiet_lap_giao_dien()

    def _thiet_lap_giao_dien(self):
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #F0F2F5;
                border: none;
                padding: 20px;
            }
            QTextEdit QScrollBar:vertical {
                width: 8px;
                background: transparent;
            }
            QTextEdit QScrollBar::handle:vertical {
                background-color: #BCC0C4;
                border-radius: 4px;
            }
        """)

    def gui_tin_nhan_nguoi_dung(self, tin_nhan: str):
        thoi_gian = QTime.currentTime().toString("HH:mm")
        html = f'''
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 10px;">
                <tr>
                    <td style="width: 100%; padding: 0;">
                        <div style="
                            width: 100%;
                            display: flex;
                            justify-content: flex-end;
                            align-items: flex-end;
                            padding-right: 15px;
                        ">
                            <div style="
                                max-width: 65%;
                            ">
                                <div style="
                                    background-color: #0084FF;
                                    color: white;
                                    padding: 20px;
                                    border-radius: 20px;
                                    border-top-right-radius: 5px;
                                    font-family: Arial, sans-serif;
                                    font-size: 14px;
                                    line-height: 1.4;
                                    margin-bottom: 5px;
                                    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
                                    display: inline-block;
                                    word-wrap: break-word;
                                    white-space: pre-wrap;
                                ">
                                    {tin_nhan}
                                </div>
                                <div style="
                                    text-align: right;
                                    font-size: 11px;
                                    color: #65676B;
                                    padding-right: 8px;
                                    font-family: Arial, sans-serif;
                                ">
                                    {thoi_gian}
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
        '''
        self._them_tin_nhan(html)

    def gui_tin_nhan_bot(self, tin_nhan: str):
        thoi_gian = QTime.currentTime().toString("HH:mm")
        html = f'''
            <table width="100%" cellpadding="0" cellspacing="0" style="margin-bottom: 10px;">
                <tr>
                    <td style="width: 100%; padding: 0;">
                        <div style="
                            width: 100%;
                            display: flex;
                            justify-content: flex-start;
                            align-items: flex-start;
                            padding-left: 15px;
                        ">
                            <div style="
                                max-width: 65%;
                            ">
                                <div style="
                                    background-color: #E4E6EB;
                                    color: black;
                                    padding: 20px;
                                    border-radius: 20px;
                                    border-top-left-radius: 5px;
                                    font-family: Arial, sans-serif;
                                    font-size: 14px;
                                    line-height: 1.4;
                                    margin-bottom: 5px;
                                    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
                                    display: inline-block;
                                    word-wrap: break-word;
                                    white-space: pre-wrap;
                                ">
                                    {tin_nhan}
                                </div>
                                <div style="
                                    text-align: left;
                                    font-size: 11px;
                                    color: #65676B;
                                    padding-left: 8px;
                                    font-family: Arial, sans-serif;
                                ">
                                    {thoi_gian}
                                </div>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
        '''
        self._them_tin_nhan(html)

    def _them_tin_nhan(self, html):
        self.text_edit.append(html)
        self.text_edit.verticalScrollBar().setValue(
            self.text_edit.verticalScrollBar().maximum()
        )

    def xoa_tin_nhan(self):
        self.text_edit.clear()