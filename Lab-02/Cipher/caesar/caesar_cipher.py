from cipher.caesar import ALPHABET  
class CaesarCipher:
    def __init__(self, shift):
        self.alphabet = ALPHABET

    def encypt_text(self, text: str, shift: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_letter_index = (letter_index + shift) % alphabet_len
            output_letter = self.alphabet[output_index]
            encrypted_text.append(output_letter)
        return ''.join(encrypted_text)
    
    def decrypt_text(self, text: str, shift: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            output_letter_index = (letter_index - shift) % alphabet_len
            output_letter = self.alphabet[output_index]
            decrypted_text.append(output_letter)
        return ''.join(decrypted_text)
