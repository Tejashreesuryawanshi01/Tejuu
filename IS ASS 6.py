def calculatePower(x, y, P):
    result = 0
    if y == 1:
        return x
    else:
        result = pow(x, y, P)
        return result

def main():
    print("Both the users should be agreed upon the public keys G and P")
    G = int(input("Enter value for public key G: "))
    P = int(input("Enter value for public key P: "))

    a = int(input("Enter value for private key a selected by user1: "))
    b = int(input("Enter value for private key b selected by user2: "))

    x = calculatePower(G, a, P)
    y = calculatePower(G, b, P)

    ka = calculatePower(y, a, P)
    kb = calculatePower(x, b, P)

    print("Secret key for User1 is:", ka)
    print("Secret key for User2 is:", kb)

if __name__ == "__main__":
    main()
