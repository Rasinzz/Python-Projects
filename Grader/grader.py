def getGrade(grade):
    isPercent = False
    isLetter = False

    if grade.isdigit():
        isPercent = True
        grade = int(grade) # Convert (cast) grade to integer
    else:
        isLetter = True

    if isLetter:
        if grade == "A":
            return "Grade is 90% - 100\%"
        elif grade == "B":
            return "Grade is 80% - 90\%"
        elif grade == "C":
            return "Grade is 70% - 80\%"
        elif grade == "D":
            return "Grade is 60% - 70\%"
        elif grade == "F":
            return "Grade is 0% - 60\%"
        else:
            return "Invalid input"
    elif isPercent:
        if grade >= 90 and grade <= 100:
            return "Grade is an A"
        elif grade >= 80 and grade <= 90:
            return "Grade is a B"
        elif grade >= 70 and grade <= 80:
            return "Grade is a C"
        elif grade >= 60 and grade <= 70:
            return "Grade is a D"
        elif grade >= 0 and grade <= 60:
            return "Grade is an F"
        else:
            return "Invalid input"
    else:
        return "Invalid input"

while True:
    grade = input("What is the grade? (percent/letter): ")

    print(getGrade(grade))