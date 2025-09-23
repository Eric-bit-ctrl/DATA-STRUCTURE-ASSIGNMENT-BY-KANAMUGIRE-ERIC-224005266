# Student Marks Tracker Assignment
# Student-style solution with comments

# --- Integers ---
# Example student marks in a semester
student_marks = [85, 92, 78, 96, 89]

# Compute total, average, min and max
total_marks = sum(student_marks)
average_marks = total_marks / len(student_marks)
min_marks = min(student_marks)
max_marks = max(student_marks)

# --- Strings (f-strings report) ---
report = f"Total student marks: {total_marks}\n"
report += f"Average marks: {average_marks:.2f}\n"
report += f"Minimum marks: {min_marks}, Maximum marks: {max_marks}"

print("---- Marks Report ----")
print(report)

# --- Booleans ---
# Threshold condition + compound check
threshold = 80
if average_marks > threshold and max_marks > 90:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# --- Lists ---
subjects = ["Math", "English", "Science", "History"]
print("\nOriginal List:", subjects)

# Add a new element
subjects.append("Geography")

# Remove one (if Science exists)
if "Science" in subjects:
    subjects.remove("Science")

# Sort the list
subjects.sort()
print("Modified List:", subjects)

# --- Arrays ---
import array

# Store a subset of marks using array
marks_array = array.array('i', [85, 92, 78])
array_sum = sum(marks_array)

print("\nSum of array:", array_sum)


# --- Dictionaries ---
# Each record has id, name, and value
student_records = [
    {"id": 1, "name": "Alice", "value": 85},
    {"id": 2, "name": "Bob", "value": 92},
    {"id": 3, "name": "Charlie", "value": 78}
]

# Update Bob's value
student_records[1]["value"] = 95

# Delete Charlie's record
del student_records[2]

# Compute total value across all records
total_value = sum(record["value"] for record in student_records)

print("\nStudent Records:", student_records)
print("Total Value of Records:", total_value)
