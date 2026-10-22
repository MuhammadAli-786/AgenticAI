def main():
    name = input("Enter student name: ").strip()
    
    # Validation
    if name == "":
        print("Invalid name")
        return
    
    # Calculation
    marks = 80
    bonus = 5
    total_marks = marks + bonus
    
    # Output
    print(f"Student: {name}")
    print(f"Total Marks: {total_marks}")

if __name__ == "__main__":
    main()
def main():
    name = input("Enter student name: ")
    
    # Validate name
    if name == "":
        print("Invalid name")
        return
        
    marks = int(input("Enter marks: "))
    
    # Validate marks
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return
        
    # Calculate grade
    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"
        
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
def validate_name(name):
    return name != ""

def validate_marks(marks):
    return 0 <= marks <= 100

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    name = input("Enter student name: ")
    if not validate_name(name):
        print("Invalid name")
        return
        
    marks = int(input("Enter marks: "))
    if not validate_marks(marks):
        print("Invalid marks")
        return
        
    grade = calculate_grade(marks)
    
    print("\nStudent Report")
    print("----------------")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
