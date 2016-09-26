import math

def main():
    print ("This program will calculate the real roots of a quadratic")
    print ("in the form of Ax^2 + Bx + C = 0")

    a = input("Enter A: ")
    b = input("Enter B: ")
    c = input("Enter C: ")

    a = float(a)
    b = float(b)
    c = float(c)

    discRoot = math.sqrt(b**2 - (4*a*c))
    root1 = (-b + discRoot)/(2*a)
    root2 = (-b - discRoot)/(2*a)

    print("The solutions are :" + str(root1) + " & " + str(root2))

main()

