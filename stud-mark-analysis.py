# Student Marks Analysis

students = {
    "Aman": 85,
    "Riya": 92,
    "Rahul": 76,
    "Sneha": 88,
    "Arjun": 95
}

# Average marks
average = sum(students.values()) / len(students)
print("Average Marks:", average)

# Highest marks
topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

# Students above average
print("Students above average:")
for name, marks in students.items():
    if marks > average:
        print(name, marks)