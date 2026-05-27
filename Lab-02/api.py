from flask import Flask, request, jsonify

from Cipher.caesar import CaesarCipher
from Cipher.vigenere import VigenereCipher
from Cipher.railfence import RailFenceCipher
from Cipher.playfair import PlayfairCipher

app = Flask(__name__)

# ===================== CIPHERS =====================
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()

# ===================== CAESAR =====================

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()

    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or key is None:
        return jsonify({"error": "missing plain_text or key"}), 400

    encrypted_text = caesar_cipher.encrypt_text(plain_text, int(key))

    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()

    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or key is None:
        return jsonify({"error": "missing cipher_text or key"}), 400

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, int(key))

    return jsonify({'decrypted_text': decrypted_text})


# ===================== VIGENERE =====================

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()

    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({"error": "missing plain_text or key"}), 400

    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)

    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()

    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({"error": "missing cipher_text or key"}), 400

    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)

    return jsonify({'decrypted_text': decrypted_text})


# ===================== RAILFENCE =====================

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()

    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or key is None:
        return jsonify({"error": "missing plain_text or key"}), 400

    encrypted_text = railfence_cipher.rail_fence_encrypt(
        plain_text,
        int(key)
    )

    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()

    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or key is None:
        return jsonify({"error": "missing cipher_text or key"}), 400

    decrypted_text = railfence_cipher.rail_fence_decrypt(
        cipher_text,
        int(key)
    )

    return jsonify({'decrypted_text': decrypted_text})


# ===================== PLAYFAIR =====================

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.get_json()

    key = data.get('key')
    if not key:
        return jsonify({"error": "missing key"}), 400

    matrix = playfair_cipher.create_playfair_matrix(key)

    return jsonify({'matrix': matrix})


@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()

    plain_text = data.get('plain_text')
    key = data.get('key')

    if not plain_text or not key:
        return jsonify({"error": "missing plain_text or key"}), 400

    matrix = playfair_cipher.create_playfair_matrix(key)

    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)

    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()

    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if not cipher_text or not key:
        return jsonify({"error": "missing cipher_text or key"}), 400

    matrix = playfair_cipher.create_playfair_matrix(key)

    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)

    return jsonify({'decrypted_text': decrypted_text})


# ===================== RUN =====================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)