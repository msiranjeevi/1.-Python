class FA2():
    def subfields():
        print("Sub-fields in AI Are: \n Machine Learning \n Nueral Network \n Vision \n Robotics \n Speech Processing \n Natural Language Processing ")

    # ODD and EVEN
    # define function

    def oe():
        no = int(input("Enter a number to check:"))
        if no % 2 == 0:
            return "Its an even number"
        else:
            return "Its an odd number"

    def eli():
        gen = str(input("Enter your gender (M/F):"))
        age = int(input("Enter your age:"))
        if gen == 'M' and age >= 21:
            return "Congrats! You are a Male and you are eligible for getting married!"
        elif gen == 'F' and age >= 18:
            return "Congrats! You are a Female and you are eligible for getting married!"
        else:
            return "You are not eligible for marriage"

    def tp():
        s1 = int(input("Enter sub1 mark:"))
        s2 = int(input("Enter sub2 mark:"))
        s3 = int(input("Enter sub3 mark:"))
        s4 = int(input("Enter sub4 mark:"))
        s5 = int(input("Enter sub5 mark:"))

        total = s1 + s2 + s3 + s4 + s5
        return total

    def pr(total):
        per = (total / 500) * 100
        return per

    def triangle():
        h1 = float(input("Enter the height:"))
        b1 = float(input("Enter the base:"))
        tri = .5 * h1 * b1
        print("Height is:", h1)
        print("Base is:", b1)
        print("Formula applied: 0.5 * height * base")
        print("Area of triangle:", tri)
        s1 = float(input("Enter side1:"))
        s2 = float(input("Enter side2:"))
        s3 = float(input("Enter side3:"))
        peri = s1 + s2 + s3
        print("side 1 is:", s1)
        print("side 2 is:", s2)
        print("side 3 is:", s3)
        print("perimeter value is:", round(peri, 2))
