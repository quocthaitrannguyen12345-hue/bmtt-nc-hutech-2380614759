class VigenereCipher:
    def __init__(self):
        pass

    # ================= ENCRYPT =================
    def encrypt_text(self, plain_text, key):
        if not key:
            return plain_text  # Nếu key trống, trả về nguyên bản
            
        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                # Lấy độ dịch chuyển dựa trên ký tự key tương ứng
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

                key_index += 1
            else:
                encrypted_text += char

        return encrypted_text

    # ================= DECRYPT =================
    def decrypt_text(self, cipher_text, key):
        if not key:
            return cipher_text # Nếu key trống, trả về nguyên bản
            
        decrypted_text = ""
        key_index = 0

        for char in cipher_text:
            if char.isalpha():
                # Lấy độ dịch chuyển dựa trên ký tự key tương ứng
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

                key_index += 1
            else:
                decrypted_text += char

        return decrypted_text