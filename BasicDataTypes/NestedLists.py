"""
Title     : Nested Lists
Subdomain : Data Types
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 06 januaryuary 2024
Problem   : https://www.hackerrank.com/challenges/nested-list/problem
"""
if __name__ == "__main__":
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        scores.append(score)
    second_min_score = sorted(set(scores))[1]
    student_names = sorted(
        [student[0] for student in students if student[1] == second_min_score]
    )
    print("\n".join(student_names))
