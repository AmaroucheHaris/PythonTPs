#Amarouche Haris
#31

def syracuse():
    number = int(input("Veuillez saisir un nombre entier : \n"))
    i = 0
    while number != 1:
        if number %2 == 0:
            number//=2
        else:
            number = number * 3 + 1
        print(number, "\n")
        i+=1
    print("1 au bout de : ",i)

syracuse()