from encryptor import Encryptor

def generate_and_save_key():
    # Generate a new encryption key
    key = Encryptor.generate_key()
    
    # Display the key for reference
    print("Generated encryption key:", key.decode())
    
    # Save the key to a file (e.g., key.key) securely
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key saved to key.key")

if __name__ == "__main__":
    generate_and_save_key()
