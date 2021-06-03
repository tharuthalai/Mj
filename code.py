from math import gcd
from PIL import Image
import os
import stepic


def KeyGenerator():
    print("\n::KEY GENERATION::")

    def prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, "Is Not A Prime Number.")
                    exit()
                    break
        else:
            print(num, "Is Not A Prime Number.")
            exit()

    print("Enter A Prime Number:")
    P = int(input())
    prime(P)

    print("Enter Another Prime Number:")
    Q = int(input())
    prime(Q)

    N = P * Q
    PN = (P - 1) * (Q - 1)

    print("Enter A Number From 1 To", PN, ":")
    E = int(input())

    if E <= 1:
        print("The Number Should Be Above 1")
        exit()
    elif E >= PN:
        print("The Number Should Be Below", PN)
        exit()

    def coprime(n, pn):
        if gcd(n, pn) == 1:
            return n
        else:
            return coprime(n + 1, pn)

    E = coprime(E, PN)

    def congruent(e, pn):
        td = 1
        while ((e * td) % pn) != 1:
            td = td + 1
        d = td
        return d

    D = congruent(E, PN)

    print("Your Public Key Is:")
    print(E, end="")
    print(" ", end="")
    print(N)
    print("Your Private Key Is:")
    print(D, end="")
    print(" ", end="")
    print(N)
    main()


def Encrypter():
    print("\n::Encryption::")
    print("Enter Message:")
    M = input()

    print("Enter Public Key:")
    U = input()

    LL = []
    for M1 in U:
        LL.append(M1)

    LL1 = []
    LL2 = []
    for i in range (len(LL)):
        if (LL[i] == " "):
            LL3 = ''.join(LL2)
            LL1.append(int(LL3))
            LL2.clear()

        elif (i == (len(LL)-1)):
            LL2.append(LL[i])
            LL3 = ''.join(LL2)
            LL1.append(int(LL3))
            LL2.clear()

        else:
            LL2.append(LL[i])

    E, N = LL1

    print("Encrypting The Message using RSA algorithm")

    L = []
    for M1 in M:
        L.append(ord(M1))

    L1 = []
    for M1 in L:
        L1.append(pow(M1, E, N))

    L2 = []
    for M1 in L1:
        L2.append(chr(M1))

    L3 = []
    for M1 in L1:
        L3.append(str(M1))

    L4 = []
    for M1 in L3:
        L4.append(M1)
        L4.append(" ")

    L5 = ''.join(L2)
    print("Encrypted Message:")
    print(L5)

    L6 = ''.join(L4)

    L7 = L6.encode('utf-8')

    print("Enter Image Name (With Extension) :")
    originalfile = str(input())

    print("Creating Encrypted Image")

    im = Image.open(originalfile)

    im1 = stepic.encode(im, L7)
    encodedfile = "Encrypted" + originalfile
    im1.save(encodedfile)

    print(encodedfile, "Was Successfully Created")
    main()


def Decrypter():
    try:
        print("\n::Decryption::")
        print("Enter Encrypted Image Name ( With Extension ) :")
        encodedfile = str(input())

        print("Retrieving Encrypted Message From", encodedfile, "")

        im1 = Image.open(encodedfile)
        L = stepic.decode(im1)

        L1 = []
        L2 = []
        for M1 in L:
            if M1 == " ":
                L3 = ''.join(L2)
                L1.append(L3)
                L2.clear()
            else:
                L2.append(M1)

        L4 = []
        for M1 in L1:
            L4.append(int(M1))

        L5 = []
        for M1 in L4:
            L5.append(chr(M1))

        L6 = ''.join(L5)
        print("Encrypted Message:")
        print(L6)

        print("Enter Private Key:")
        R = input()

        LL = []
        for M1 in R:
            LL.append(M1)

        LL1 = []
        LL2 = []
        for M1 in LL:
            if M1 == " ":
                LL3 = ''.join(LL2)
                LL1.append(int(LL3))
                LL2.clear()

            elif M1 == LL[-1]:
                LL2.append(M1)
                LL3 = ''.join(LL2)
                LL1.append(int(LL3))
                LL2.clear()

            else:
                LL2.append(M1)

        D, N = LL1

        print("Decrypting The Encrypted Message Using RSA algorithm")

        L7 = []
        for M1 in L4:
            L7.append(pow(M1, D, N))

        L8 = []
        for M1 in L7:
            L8.append(chr(M1))

        L9 = ''.join(L8)
        print("Decrypted Message:")
        print(L9)
        main()
    except ValueError:
        print("Not A Stego Image")


def main():
    print("\n::Select One Of The Following Options::")
    print("1.Key Generation")
    print("2.Encryption")
    print("3.Decryption")
    print("4.Exit")
    a = int(input())
    if a == 1:
        KeyGenerator()
    elif a == 2:
        Encrypter()
    elif a == 3:
        Decrypter()
    elif a == 4:
        exit()
    else:
        print("Enter A Valid Input")


main()
