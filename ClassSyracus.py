class ClassSyracus:

    def __init__(self, input, output):
       self.inputFile = open("input.txt", "r")
       self.outputFile = open("output.txt", "w")

    def syracuse(self):
        number = int(self.inputFile.read())
        i = 0
        while number != 1:
            if number %2 == 0:
                number//=2
            else:
                number = number * 3 + 1
            print(number, "\n")
            i+=1
        print("1 au bout de : ",i)
        self.outputFile.write(str(number))

syrac = ClassSyracus("input.txt", "output.txt")
syrac.syracuse()

