#Joey Ma
import math
import random

def test(w1, w2, w3, w4):
    lis = []

    with open("in.txt") as f:
        content = f.readlines()

    for i in range(len(content)):

        x1 = int(content[i][1])
        x2 = int(content[i][3])
        x3 = int(content[i][5])
        x4 = int(content[i][7])

        Y = x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4
        Y = math.ceil(Y)
        lis.append(Y)

    with open('out.txt', 'w') as f:
        for item in lis:
            print(item, file=f)
            
def main():
    #Learning rate
    a = 0.1
    #Error
    e = 0
    num_error = 1

    #Weights
    w1 = round(random.uniform(-0.9,0.9),1)
    w2 = round(random.uniform(-0.9,0.9),1)
    w3 = round(random.uniform(-0.9,0.9),1)
    w4 = round(random.uniform(-0.9,0.9),1)

    #Inputs
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0

    #Actual output
    Y = 0
    #Expected output
    EY = 0

    #Get the correct weights
    while num_error != 0:
        num_error = 0

        for i in range(2):
            x1 = i
            for j in range(2):
                x2 = j
                for k in range(2):
                    x3 = k
                    for h in range(2):
                        x4 = h

                        #OR gate
                        if x1 == 1 or x2 == 1 or x3 == 1 or x4 == 1:
                            EY = 1
                        else:
                            EY = 0

                        #The actual output of the perceptron
                        Y = x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4
                        Y = math.ceil(Y)

                        #If actual ouput does not equal expected output,
                        #we adjust the error
                        if Y != EY:
                            e = EY - Y
                            num_error += 1
                        else:
                            e = 0

                        #Adjust weights
                        w1 = w1 + a * x1 * e
                        w2 = w2 + a * x2 * e
                        w3 = w3 + a * x3 * e
                        w4 = w4 + a * x4 * e

    test(w1,w2,w3,w4)

main()
