''' Question 1: Student Report Card
Scenario: Ek student ke exam ka result display karna hai.

Variables: student_name = "Rahul", subject = "Maths", marks = 95

Expected Output: "Hello Rahul, you have scored 95 marks in Maths."
'''

student_name = "Rahul"
subject = "Maths"
marks = 95 

output_template = "Hello {}, you have scored {} marks in {}."
print(output_template)

output_message = output_template.format(student_name, marks, subject)
print(output_message)