class PlayfairCipher:
    def __init__(self):
        pass

    def create_matrix(self, key):
        key = key.upper().replace("J", "I")

        seen = set()
        matrix = []

        for char in key:
            if char.isalpha() and char not in seen:
                seen.add(char)
                matrix.append(char)

        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                matrix.append(char)

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_pos(self, matrix, ch):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == ch:
                    return r, c

    def prepare(self, text):
        text = text.upper().replace("J", "I")
        text = "".join([c for c in text if c.isalpha()])

        res = []
        i = 0

        while i < len(text):
            a = text[i]
            b = "X"

            if i + 1 < len(text):
                if text[i + 1] != a:
                    b = text[i + 1]
                    i += 2
                else:
                    i += 1
            else:
                i += 1

            res.append(a + b)

        return res

    # ================= FIXED ENCRYPT =================
    def encrypt_text(self, text, key):
        matrix = self.create_matrix(key)
        pairs = self.prepare(text)

        result = ""

        for a, b in pairs:
            r1, c1 = self.find_pos(matrix, a)
            r2, c2 = self.find_pos(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1 + 1) % 5]
                result += matrix[r2][(c2 + 1) % 5]

            elif c1 == c2:
                result += matrix[(r1 + 1) % 5][c1]
                result += matrix[(r2 + 1) % 5][c2]

            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result

    # ================= FIXED DECRYPT =================
    def decrypt_text(self, text, key):
        matrix = self.create_matrix(key)
        text = text.upper()

        result = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]

            r1, c1 = self.find_pos(matrix, a)
            r2, c2 = self.find_pos(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1 - 1) % 5]
                result += matrix[r2][(c2 - 1) % 5]

            elif c1 == c2:
                result += matrix[(r1 - 1) % 5][c1]
                result += matrix[(r2 - 1) % 5][c2]

            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result