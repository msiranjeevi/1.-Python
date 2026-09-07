# Newclass - Student Grade Calculator
class SGC():
    # Calculate CGP using 3 functions
    # total for 5 subjects
    def totalMarks():
        m1 = int(input("Enter your English mark:"))
        m2 = int(input("Enter your Social mark:"))
        m3 = int(input("Enter your Science mark:"))
        m4 = int(input("Enter your Maths mark:"))
        m5 = int(input("Enter your AI    mark:"))
        total = m1 + m2 + m3 + m4 + m5
        return total

    # Calculate average
    def avgMarks(total):
        return total / 5

    # Calculate cgp
    def cgp(average):
        return average / 10

    def grade(total, average, cgpa):
        if total >= 450 and average >= 90 and cgpa >= 9.0:
            return "A+ Grade"
        elif total >= 400 and average >= 80 and cgpa >= 8.0:
            return "A Grade"
        elif total >= 350 and average >= 70 and cgpa >= 7.0:
            return "B Grade"
        elif total >= 300 and average >= 60 and cgpa >= 6.0:
            return "C Grade"
        else:
            return "Fail"
