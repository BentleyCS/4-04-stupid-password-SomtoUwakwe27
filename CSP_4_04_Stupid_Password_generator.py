"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    listOfPasswords = []
    for i in range(1,n,1):
        password = ""
        password+=str(i)
        for k in range(1,n,1):
            password += str(k)
            for m in range(1, l+1,1):
                alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
                letter = ""
                letter += alphabet[m]
                m-=1
                for o in range(1, l+1, 1):
                    letter += str(alphabet[o])
                    o-=1
                    for t in range(1,n+1,1):
                        if t > i and t > k:
                            password += str(t)
                            listOfPasswords.append(f"{i}{k}{alphabet[m]}{alphabet[o]}{t}")
    return listOfPasswords
print(stupidPassword(4,2))