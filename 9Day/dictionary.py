student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# for key in student_scores:
#     print(key) prints key i.e names

# for key in student_scores:
#     print(student_scores[key]) prints values i.e marks




student_grades = {}

# for key in student_scores:
#     print(key)
#     student_grades[key] = "hello"
#     print(student_grades)

    
for key in student_scores:
     if (student_scores[key] > 90 and student_scores[key]  <= 100):
         student_grades[key] = "Outstanding"
     elif (student_scores[key]  > 80 and student_scores[key]  <= 90 ):
         student_grades[key] = "Exceeds Expectations"
     elif (student_scores[key]  <= 70):
         student_grades[key] = "Fail"
    # student_grades["key"] = grade
    
print(student_grades)