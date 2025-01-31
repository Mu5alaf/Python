#Example 1
a = 5
b = 10

print('The sub of A and B')
print(f'A is = {a} and B is = {b} = {a + b} ')


#Example 2
student = {
    "name": "John Doe",
    "subjects": [
        {
            "name": "Mathematics",
            "grade": 88,
            "comment": "Excellent improvement.",
        },
        {
            "name": "Science",
            "grade": 92,
            "comment": "Outstanding performance.",
        },
        {
            "name": "History",
            "grade": 78,
            "comment": "Needs to participate more.",
        },
        {
            "name": "Art",
            "grade": 85,
            "comment": "Very creative."
        },
    ],
}

def student_report(student):

    report_header = f"Progress Report. Student: {student['name']}"
    total = sum(subject["grade"] for subject in student["subjects"])
    average = total/len(student['subjects'])
    average_report = f"Average: {average:.2f} / 100\n"
    subject_report = "Course Details:\n"
    for subject in student['subjects']:
        subject_report += (
            f"{subject['name']:<15} "
            f"Grade: {subject['grade']:3d} "
            f"Comment: {subject['comment']}\n"
        )
    print( f"""
    {report_header}
    {average_report}
    {subject_report}
    """)
student_report(student)



name = "I'm Bob"

print("Hello, %s "%name)

age = 28

print("I have %o year's old" %age) #integer

my_hight = 182.50

print("My hight is %f" %my_hight)# floating point 

