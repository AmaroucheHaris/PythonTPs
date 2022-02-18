#Amarouche Haris
#31

def mul_egyptienne(a, b):

    prod = 0
    while a != 0:
        if a % 2 == 1:  
            prod += b
        a //= 2 
        b += b 
    return prod

print(mul_egyptienne(37, 19))
        
