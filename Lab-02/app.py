from flask import Flask, render_template, request

from Cipher.caesar import CaesarCipher
from Cipher.vigenere import VigenereCipher
from Cipher.playfair import PlayfairCipher
from Cipher.railfence import RailFenceCipher

app = Flask(__name__)


# ================= KEY VALIDATION =================
def validate_int_key(key):
    try:
        key = int(key)
        if key <= 0:
            return None
        return key
    except:
        return None


def validate_int_key_min2(key):
    try:
        key = int(key)
        if key < 2:
            return None
        return key
    except:
        return None


def validate_alpha_key(key):
    if not key.isalpha():
        return None
    return key.upper()


# ================= HOME =================
@app.route('/')
def home():
    return render_template('index.html')


# ================= CAESAR =================
@app.route('/caesar')
def caesar_page():
    return render_template('caesar.html')


@app.route('/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = validate_int_key(request.form['inputKeyPlain'])

    if key is None:
        return "❌ Lỗi: Key Caesar phải là số nguyên dương!"

    cipher = CaesarCipher()
    result = cipher.encrypt_text(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>encrypted text:</b> {result}
    """


@app.route('/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = validate_int_key(request.form['inputKeyCipher'])

    if key is None:
        return "❌ Lỗi: Key Caesar phải là số nguyên dương!"

    cipher = CaesarCipher()
    result = cipher.decrypt_text(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>decrypted text:</b> {result}
    """


# ================= VIGENERE =================
@app.route('/vigenere')
def vigenere_page():
    return render_template('vigenere.html')


@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = validate_alpha_key(request.form['inputKeyPlain'])

    if key is None:
        return "❌ Lỗi: Key Vigenere chỉ được chứa chữ cái (A-Z)!"

    cipher = VigenereCipher()
    result = cipher.encrypt(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>encrypted text:</b> {result}
    """


@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = validate_alpha_key(request.form['inputKeyCipher'])

    if key is None:
        return "❌ Lỗi: Key Vigenere chỉ được chứa chữ cái (A-Z)!"

    cipher = VigenereCipher()
    result = cipher.decrypt(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>decrypted text:</b> {result}
    """


# ================= PLAYFAIR =================
@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html')


@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = validate_alpha_key(request.form['inputKeyPlain'])

    if key is None:
        return "❌ Lỗi: Key Playfair chỉ được chứa chữ cái (A-Z)!"

    cipher = PlayfairCipher()
    result = cipher.encrypt(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>encrypted text:</b> {result}
    """


@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = validate_alpha_key(request.form['inputKeyCipher'])

    if key is None:
        return "❌ Lỗi: Key Playfair chỉ được chứa chữ cái (A-Z)!"

    cipher = PlayfairCipher()
    result = cipher.decrypt(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>decrypted text:</b> {result}
    """


# ================= RAILFENCE =================
@app.route('/railfence')
def railfence_page():
    return render_template('railfence.html')


@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = validate_int_key_min2(request.form['inputKeyPlain'])

    if key is None:
        return "❌ Lỗi: RailFence key phải là số nguyên ≥ 2!"

    cipher = RailFenceCipher()
    result = cipher.encrypt(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>encrypted text:</b> {result}
    """


@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = validate_int_key_min2(request.form['inputKeyCipher'])

    if key is None:
        return "❌ Lỗi: RailFence key phải là số nguyên ≥ 2!"

    cipher = RailFenceCipher()
    result = cipher.decrypt(text, key)

    return f"""
    <b>text:</b> {text} <br>
    <b>key:</b> {key} <br>
    <b>decrypted text:</b> {result}
    """


# ================= RUN =================
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)