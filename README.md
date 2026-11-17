# ALU Transcript Generator

A two-part toolkit for handling course grades: a Python application that calculates a student's final academic status from a CSV file, and a Bash script that archives the grade data and logs its actions.


##Requirements to run the program

-Python 3
-Bash 

A.Part 1: Grade Evaluator (`grade-evaluator.py`)

##How to run

```bash
python3 grade-evaluator.py
```

The program asks for the name of the CSV file to process. Enter `grades.csv` (or the path to any other grades file).

#Features

1.File loading**
Prompts for a filename, checks that the file exists, and reads each assignment's name, group, score, and weight. Scores and weights are converted to numbers (decimals are supported). The file must contain the columns `assignment`, `group`, `score`, and `weight`.

2.Grade validation**
Checks that every assignment score is a valid percentage between 0 and 100. Every invalid score is reported by assignment name.

3.Weight validation**
Splits the assignments into Formative and Summative groups and verifies that:
-all weights add up to exactly 100
-Formative weights add up to exactly 60
-Summative weights add up to exactly 40
-every assignment belongs to a recognised group

If any check fails, the program lists every problem and stops without calculating a result.

4.GPA calculation
Each assignment contributes (score x weight / 100) points. The points are added into a final grade out of 100, and the GPA is calculated.

5.Pass/Fail decision
Each category is converted to a percentage of its own maximum. The student is "PASSED"only if they score at least 50% in both Formative and Summative. Failing either category results in "Failed", even if the overall grade is above 50%.

6.Resubmission logic
Looks at the Formative assignments scoring below 50% and finds the highest weight among them. Every failed Formative assignment with that weight is listed as eligible for resubmission, so ties are all shown. If no Formative assignment failed, the program reports that no resubmission is needed.

7.Results report
Prints the Formative and Summative totals with percentages, the final grade, the GPA, the final decision, and the resubmission options.

##Error handling

The program prints a clear message and exits without crashing when:
-the file is missing
-the file is empty or contains no assignment records
-a column is missing, or a score or weight is not a number
-a score is outside 0 to 100
-the weights do not add up to 100, 60, and 40
-an assignment has an unrecognised group

Weight totals and percentages are rounded, so decimal values do not cause false validation errors from floating-point rounding.

B.Part 2: Organizer.sh script

##How to run

bash
chmod +x organizer.sh   # only needed once, makes the script executable
./organizer.sh
```

Run it from the project folder, because it looks for "grades.csv" in the current directory.

###Features

1.Archive directory check
Looks for a directory named "archive". If it does not exist, the script creates it.

2. Missing file check
If `grades.csv` cannot be found, the script prints an error and exits instead of archiving nothing.

3. Timestamped archiving
Generates a timestamp in the format "YYYYMMDD-HHMMSS", renames "grades.csv" to "grades_<timestamp>.csv", and moves it into the "archive" directory. Because every file gets a unique timestamp, earlier archives are never overwritten.

4. Workspace reset
Immediately after the move, creates a new empty "grades.csv" in the current directory so the workspace is ready for the next batch of grades.

5. Logging
Appends an entry to "organizer.log" containing the timestamp, the original filename, and the new archived filename. The log accumulates entries from every run, giving a history of all archived files.


# Workflow

1. Place the grades to be evaluated in `grades.csv`.
2. Run the evaluator: `python3 grade-evaluator.py`
3. Run the organizer: `./organizer.sh`
4. Add the next batch of grades to the new `grades.csv` and repeat from step 2.

Always run the evaluator before the organizer, because the organizer empties grades.csv. If the evaluator is run on an empty grades.csv, it reports that there are no assignment grades in the file. To evaluate a previously archived batch, enter its path when the evaluator asks for a filename, for example `archive/grades_20261117-221500.csv`.
