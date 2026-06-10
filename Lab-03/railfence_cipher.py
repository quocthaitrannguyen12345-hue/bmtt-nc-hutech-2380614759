import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.railfence import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def validate_key(self):
        """Kiểm tra khóa có phải số nguyên dương không."""
        key = self.ui.txt_key.toPlainText()
        if not key.isdigit() or int(key) < 2:
            QMessageBox.warning(self, "Lỗi Input", "Khóa RailFence phải là số nguyên >= 2")
            return None
        return key

    def call_api_encrypt(self):
        key = self.validate_key()
        if not key: return

        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        payload = {
            "plain_text": self.ui.txt_plaintext.toPlainText(),
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["encrypted_text"]) # Dùng setPlainText thay cho setText cho ô nhập
                QMessageBox.information(self, "Thành công", "Encrypted Successfully")
            else:
                QMessageBox.critical(self, "API Error", response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", str(e))

    def call_api_decrypt(self):
        key = self.validate_key()
        if not key: return

        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        payload = {
            "cipher_text": self.ui.txt_plaintext.toPlainText(), # Lưu ý: Nên dùng txt_plaintext để chứa cipher text khi giải mã
            "key": key
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["decrypted_text"])
                QMessageBox.information(self, "Thành công", "Decrypted Successfully")
            else:
                QMessageBox.critical(self, "API Error", response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Connection Error", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())