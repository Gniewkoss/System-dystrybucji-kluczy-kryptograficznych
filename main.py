def create_key ():
    pass


P = 23
G = 9
print(f"Public numbers: {P}, {G}")

# Alice
a = 4
#Bob
b= 3

print(f"Alice's private key: {a}, Bob's private key: {b}")

#Comute public values
x= G**a % P
y= G**b % P

#Exchange public numbers

#Alice receives public key y  and Bob receives public key x

#compute symmetric keys

ka = y**a % P
kb = x**b % P

print(f"Alice's symmetric key: {ka}, Bob's symmetric key: {kb}")

