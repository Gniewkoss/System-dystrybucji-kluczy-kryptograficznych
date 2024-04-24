import random


def diffie_hellman():
    p = 23  # liczba pierwsza
    g = 5  # liczba pierwotna

    #klucz prywatny
    a = random.randint(1, p - 1)
    b = random.randint(1, p - 1)

    #wartość publiczną
    A = pow(g, a, p)
    B = pow(g, b, p)

    shared_key_alice = pow(B, a, p)
    shared_key_bob = pow(A, b, p)

    print(f"Wartość publiczna Alice (A): {A}")
    print(f"Wartość publiczna Bob (B): {B}")
    print(f"Klucz wspólny obliczony przez Alice: {shared_key_alice}")
    print(f"Klucz wspólny obliczony przez Bob: {shared_key_bob}")

    if shared_key_alice == shared_key_bob:
        print("Alice i Bob mają ten sam klucz wspólny!")
    else:
        print("Coś poszło nie tak, klucze nie są identyczne.")


diffie_hellman()
