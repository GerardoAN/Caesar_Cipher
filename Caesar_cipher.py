import string


class CaesarCipher:
    def __init__(self, shift=3):
        self.shift = shift
        self.key, self.reverse_key = self._generator_keys(shift)

    def _generator_keys(self, shift):
        letters = string.ascii_lowercase
        key = {c: letters[(i + shift) % 26] for i, c in enumerate(letters)}
        return key, {v: k for k, v in key.items()}

    def encrypt(self, plaintext: str) -> str:
        return "".join([self.key[c] if c in self.key else c for c in plaintext.lower()])

    def decrypt(self, ciphertext: str) -> str:
        return "".join([self.reverse_key[c] if c in self.reverse_key else c for c in ciphertext.lower()])


if __name__ == "__main__":
    cipher = CaesarCipher(shift=3)
    cipher.plaintext = input('输入明文：')
    encrypted = cipher.encrypt(cipher.plaintext)
    print(f"加密结果:{encrypted}")
    print(f"解密结果:{cipher.decrypt(encrypted)}")
