def check_prime(p):
    for i in range(2,p):
        if p%i == 0:
            return False
    return True

#
# def create_key (P,G,a,b):
#     x= G**a % P
#     y= G**b % P
#
#     ka = y**a % P
#     kb = x**b % P
#     return ka, kb


# print("Shared secret:" + str(create_key(2,1,3,5)))

