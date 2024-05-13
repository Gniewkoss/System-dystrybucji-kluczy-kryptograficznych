import sqlite3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_keys():
    # Tworzenie parametrów Diffie-Hellmana
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    # Generowanie kluczy
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    # Serializacja kluczy
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_key_bytes, public_key_bytes

def save_keys_to_database(name, private_key_bytes, public_key_bytes):
    conn = sqlite3.connect('klucze.db')
    cursor = conn.cursor()

    # Utworzenie tabeli kluczy, jeśli nie istnieje
    cursor.execute('''CREATE TABLE IF NOT EXISTS klucze
                      (id INTEGER PRIMARY KEY, name TEXT, private_key BLOB, public_key BLOB)''')

    # Zapis kluczy do bazy danych
    cursor.execute("INSERT INTO klucze (name, private_key, public_key) VALUES (?, ?, ?)", (name, private_key_bytes, public_key_bytes))
    conn.commit()

    print("Klucze zostały przypisane użytkownikowi", name)

    # Zamykanie połączenia
    conn.close()

def main():
    # Prośba użytkownika o imię
    name = input("Podaj swoje imię: ")

    # Generowanie kluczy
    private_key_bytes, public_key_bytes = generate_keys()

    # Zapis kluczy do bazy danych
    save_keys_to_database(name, private_key_bytes, public_key_bytes)

if __name__ == "__main__":
    main()
