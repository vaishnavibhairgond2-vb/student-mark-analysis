# 📊 Student Marks Analysis (Python Project)

This project analyzes student marks using Python and provides basic insights such as the average score, the top-performing student, and students who scored above the average.

It is a beginner-friendly project created to practice Python programming and simple data analysis logic.

---

## 🚀 Features

- Calculate the average marks of all students
- Find the student with the highest marks
- Display students who scored above average
- Simple and easy-to-understand Python code

---

## 🛠️ Technologies Used

- Python
- Basic Python concepts (loops, dictionaries, conditions)

---

## 📂 Project Structure

student-marks-analysis  
│  
├── student_marks_analysis.py  
└── README.md  

---

## 💻 Code

```python
students = {
    "Aman": 85,
    "Riya": 92,
    "Rahul": 76,
    "Sneha": 88,
    "Arjun": 95
}

average = sum(students.values()) / len(students)
print("Average Marks:", average)

topper = max(students, key=students.get)
print("Topper:", topper, "-", students[topper])

print("Students scoring above average:")

for name, marks in students.items():
    if marks > average:
        print(name, marks)
