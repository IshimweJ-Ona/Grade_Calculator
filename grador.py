# Base class
class Assignment:
    def __init__(self, name, weight, grade):
        name.self = name
        weight.self = weight
        grade.self = grade
    
    def calculate_weight_grade(self):
        return (self.grade * self.weight) / 100

# Sub_classes
class Formative_Assignment(Assignment):
    def __init__(self, name, weight, grade):
        super().__init__(name, weight, grade)
    
class Summative_Assignment(Assignment):
    def __init__(self, name, weight, grade):
        super().__init__(name, weight, grade)

# Input collection 
def collect_assignments():
    assignments = []
    total_weight = 0
    num_assignments = int(input("Enter the number of assignments\n:"))

    for i in range(num_assignments):
        print("\nEnter assignment details:")
        name = input("Assignment name:")
        category = input("Category (Formative or Summative): ").capitalize()
        weight = float(input("Weight (% of total grade): "))
        grade = float(input("Grade obtained (out of 100): "))

        # Validate inputs
        if weight <= 0 or weight > 100 or grade < 0 or grade > 100:
            print("Invalid input. Please enter valid weights and grades.")
            continue

        if total_weight + weight > 100:
            print("Total weight exceeds 100%. Please adjust.")
            continue

        # Add assignment to the correct category
        if category == "Formative":
            assignments.append(Formative_Assignment(name, weight, grade))
        elif category == "Summative":
            assignments.append(Summative_Assignment(name, weight, grade))
        else:
            print("Invalid category. Please enter Formative or Summative.")

        total_weight += weight

    return assignments


# Calculate Grades
def calculate_grades(assignments):
    formative_total = 0
    summative_total = 0
    overall_total = 0

    for assignment in assignments:
        weighted_grade = assignment.calculate_weight_grade()
        overall_total += weighted_grade
        if isinstance(assignment, Formative_Assignment):
            formative_total += weighted_grade
        elif isinstance(assignment, Summative_Assignment):
            summative_total += weighted_grade
    
    return formative_total, summative_total, overall_total

# Function to determine pass or fail 
def pass_fail(formative_total, summative_total, formative_agv, summative_agv):
    if formative_total >= formative_agv:
        print("Pass")
    elif summative_total >= summative_agv:
        print("Pass")
    else:
        return "Fail and Repeat"
    
# Main Function
def main():
    print("Welcome to the Grade Generator Calculator.")
    print("Choose what kind of caluation u want to do:")
    print("1. Calculate grades")
    print("2. GPA Calculation")
# Make the user choose what kind of assignment to input details
    choice = input("Enter your choice (1 or 2):")
    if choice == "1":
        assignments = collect_assignments()
        formative_total, summative_total, overall_total = calculate_grades(assignments)
       #Display Results 
        print("\n--- Grade Results ---")
        print(f"Formative Total: {formative_total:.2f}")
        print(f"Summative Total: {summative_total:.2f}")
        print(f"Overall Total: {overall_total:.2f}")
    elif choice == "2":
        assignments = collect_assignments()
        _, _, overall_total = calculate_grades(assignments)
        gpa = (overall_total / 100) * 5

        # Display result
        print("\n--- GPA Result---")
        print(f"GPA: {gpa:.2f}") 

    else:
        print("Invalid choice. Re-Enter between the choice given")
    
    # Calculate totals 
    formative_total, summative_total, overall_total = calculate_grades(assignments)
    
     # Calculate average for assignment assuming both equal weight
    formative_avg = overall_total / 2 
    summative_avg = overall_total / 2

    # Compute GPA on 5
    gpa = (overall_total / 100) * 5

    # Determine pass of fail 
    result = pass_fail(formative_total, summative_total, formative_avg, summative_avg)

    # Display results 
    print("\n---Results ---")
    print(f"Formative Total: {formative_total:.2f}")
    print(f"Summative Total: {summative_total:.2f}")
    print(f"GPA: {gpa:.2f}")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
assignments = ["Math", "English", "Physics","Linux","E-Lab"]

