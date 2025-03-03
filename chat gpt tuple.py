def manage_student_records(students):
    for student in students:
        name, scores = student[0], student[1]
        avg_score = sum(scores) / len(scores)
        
        if avg_score >= 90:
            grade = 'A'
        elif avg_score >= 80:
            grade = 'B'
        elif avg_score >= 70:
            grade = 'C'
        elif avg_score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"Student: {name}, Scores: {scores}, Final Grade: {grade}")

# Example usage
students = (
    ("Alice", (85, 90, 78)),
    ("Bob", (70, 75, 80)),
    ("Charlie", (92, 88, 95)),
    ("David", (60, 55, 58))
)

manage_student_records(students)
