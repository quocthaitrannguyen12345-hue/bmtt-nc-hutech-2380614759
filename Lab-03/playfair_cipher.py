import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.playfair import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def validate_input(self):
        """Kiểm tra khóa và văn bản đầu vào."""
        key = self.ui.txt_key.toPlainText().strip()
        text = self.ui.txt_plaintext.toPlainText().strip()
        
        if not key.isalpha() or len(key) < 3:
            QMessageBox.warning(self, "Lỗi Input", "Khóa phải là chữ cái và dài ít nhất 3 ký tự!")
            return None, None
        if not text:
            QMessageBox.warning(self, "Lỗi Input", "Vui lòng nhập văn bản!")
            return None, None
        return text, key

    def call_api_encrypt(self):
        text, key = self.validate_input()
        if not text: return

        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {"plain_text": text, "key": key}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["encrypted_text"])
                QMessageBox.information(self, "Thành công", "Encrypted Successfully")
            else:
                QMessageBox.critical(self, "API Error", response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi kết nối", str(e))

    def call_api_decrypt(self):
        # Lưu ý: Khi giải mã, text đầu vào thường nằm ở ô txt_cipher (hoặc txt_plaintext tùy giao diện)
        text = self.ui.txt_plaintext.toPlainText().strip() 
        key = self.ui.txt_key.toPlainText().strip()
        
        if not text or not key.isalpha():
            QMessageBox.warning(self, "Lỗi Input", "Vui lòng kiểm tra lại văn bản và khóa!")
            return

        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {"cipher_text": text, "key": key}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setPlainText(data["decrypted_text"])
                QMessageBox.information(self, "Thành công", "Decrypted Successfully")
            else:
                QMessageBox.critical(self, "API Error", response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi kết nối", str(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())