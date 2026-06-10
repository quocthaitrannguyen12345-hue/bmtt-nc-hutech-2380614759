from flask import Flask, request, jsonify

from Cipher.caesar import CaesarCipher
from Cipher.vigenere import VigenereCipher
from Cipher.railfence import RailFenceCipher
from Cipher.playfair import PlayfairCipher

app = Flask(__name__)

# ===================== VALIDATION HELPERS =====================
def is_valid_caesar(key):
    return str(key).isdigit()

def is_valid_vigenere(key):
    return str(key).isalpha()

def is_valid_playfair(key):
    return str(key).isalpha() and len(str(key)) >= 3

def is_valid_railfence(key):
    return str(key).isdigit() and int(key) >= 2

# ===================== CIPHERS =====================
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()

# ===================== CAESAR =====================

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text, key = data.get('plain_text'), data.get('key')
    if not plain_text or not is_valid_caesar(key):
        return jsonify({"error": "Invalid Caesar input"}), 400
    return jsonify({'encrypted_text': caesar_cipher.encrypt_text(plain_text, int(key))})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text, key = data.get('cipher_text'), data.get('key')
    if not cipher_text or not is_valid_caesar(key):
        return jsonify({"error": "Invalid Caesar input"}), 400
    return jsonify({'decrypted_text': caesar_cipher.decrypt_text(cipher_text, int(key))})

# ===================== VIGENERE =====================

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text, key = data.get('plain_text'), data.get('key')
    if not plain_text or not is_valid_vigenere(key):
        return jsonify({"error": "Invalid Vigenere input"}), 400
    return jsonify({'encrypted_text': vigenere_cipher.encrypt_text(plain_text, key.upper())})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text, key = data.get('cipher_text'), data.get('key')
    if not cipher_text or not is_valid_vigenere(key):
        return jsonify({"error": "Invalid Vigenere input"}), 400
    return jsonify({'decrypted_text': vigenere_cipher.decrypt_text(cipher_text, key.upper())})

# ===================== RAILFENCE =====================

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text, key = data.get('plain_text'), data.get('key')
    if not plain_text or not is_valid_railfence(key):
        return jsonify({"error": "Invalid RailFence input (key >= 2)"}), 400
    return jsonify({'encrypted_text': railfence_cipher.encrypt_text(plain_text, int(key))})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text, key = data.get('cipher_text'), data.get('key')
    if not cipher_text or not is_valid_railfence(key):
        return jsonify({"error": "Invalid RailFence input (key >= 2)"}), 400
    return jsonify({'decrypted_text': railfence_cipher.decrypt_text(cipher_text, int(key))})

# ===================== PLAYFAIR =====================

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text, key = data.get('plain_text'), data.get('key')
    if not plain_text or not is_valid_playfair(key):
        return jsonify({"error": "Invalid Playfair input"}), 400
    matrix = playfair_cipher.create_matrix(key)
    return jsonify({'encrypted_text': playfair_cipher.encrypt_text(plain_text, matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text, key = data.get('cipher_text'), data.get('key')
    if not cipher_text or not is_valid_playfair(key):
        return jsonify({"error": "Invalid Playfair input"}), 400
    matrix = playfair_cipher.create_matrix(key)
    return jsonify({'decrypted_text': playfair_cipher.decrypt_text(cipher_text, matrix)})

# ===================== RUN =====================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)