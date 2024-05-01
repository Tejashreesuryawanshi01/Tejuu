import math
plaintext="Transposition Technique"
key=5
ciphertext=[""]*key
for column in range(key):
    pointer=column  #set pointer to column
    while pointer < len (plaintext):
        ciphertext [column]+= plaintext [pointer]
        print(ciphertext)
        pointer +=key
        cipher=''.join(ciphertext)
        print(cipher)
        numOfColumns=math.ceil (len(cipher)/key)
        print(numOfColumns)
        numOfRows=key
        numOfShadedBoxes = numOfColumns * numOfRows - len (cipher)
        print(numOfShadedBoxes)
        pt=['']* numOfColumns
        col=0
        row=0
        for sym in cipher:
            pt [col] +=sym
            col += 1
            if (col==numOfColumns )or (col==numOfColumns - 1 and row >=numOfRows-numOfShadedBoxes ):
                col=0
                row=row+1
                print(pt)
                print(''.join(pt))  
