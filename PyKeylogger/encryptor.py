from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key):
        self.cipher = Fernet(key)

    @staticmethod
    def generate_key():
        return Fernet.generate_key()

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, data):
        return self.cipher.decrypt(data).decode()
