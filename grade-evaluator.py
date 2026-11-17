import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    if not data:
        print("There are no assignement grades in the file.")
        sys.exit(1)
    # TODO: a) Check if all scores are percentage based (0-100)
    grades_valid = True 
    for item in data:
        if not (0 <= item['score'] <= 100):
            print(f"Invalid score found: {item['score']} for assignment '{item['assignment']}'")
            grades_valid = False

 # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    formative = [i for i in data if i['group']. strip().lower() == 'formative']
    summative = [i for i in data if i['group'].strip().lower() == 'summative']
    unidentified = len(data) - len(formative) - len(summative)
    if unidentified > 0:
         print(f"Warning: {unidentified} assignment(s) have an unrecognized group.will be ignored in calculations.")
    total_weight = round(sum(i['weight'] for i in data), 2)
    formative_weight = round(sum(i['weight'] for i in formative), 2)
    summative_weight = round(sum(i['weight'] for i in summative), 2)
 
    weights_valid = unidentified == 0 
    if total_weight != 100:
         print(f"Error: total weight: {total_weight}. The expected is: 100.")
         weights_valid = False
    if formative_weight != 60:
         print(f"Error: formative weight: {formative_weight}. The expected is: 60.")
         weights_valid = False
    if summative_weight != 40:
         print(f"Error: summative weight: {summative_weight}. The expected is: 40.")
         weights_valid = False
    if not (grades_valid and weights_valid):
         print("\nError: grade and weight validation failed. Recheck the grades CSV file and run again.")
         sys.exit(1)

    

   
pass

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)