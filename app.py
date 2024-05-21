
import sqlite3

print ("LOGOWANIE")
login = input("Podaj nazwe uzytwkonika: ")
haslo = input("Podaj haslo: ")

conn = sqlite3.connect('klucze.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM klucze WHERE name = ? AND private_key = ?", (login, haslo))
user = cursor.fetchone()

if user:
    print("Zalogowano pomyślnie")
else:
    print("Błędne dane logowania")

conn.close()

