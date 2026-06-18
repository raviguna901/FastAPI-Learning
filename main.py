from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def welcome():
    return "welcome to build your first profile"

students_data=[
    {"id" : 1,"name":"Ravi","place":"AP","course":"DA","marks":78},
    {"id" : 2,"name":"Guna","place":"AP","course":"DA","marks":90},
    {"id" : 3,"name":"Praveen","place":"HYD","course":"DS","marks":65},
    {"id" : 4,"name":"Joy","place":"HYD","course":"DS","marks":56},
    {"id" : 5,"name":"Mani","place":"AP","course":"DA","marks":98}
]

# class Student:
#     def __init__(self,id,name,place,course,marks):
#         self.id=id
#         self.name=name
#         self.place=place
#         self.course=course
#         self.marks=marks
# students_data=[Student(id=1,name="Ravi",place="AP",course="DS",marks=98),
#                Student(id=2,name="Guna",place="AP",course="DS",marks=100),
#                Student(id=3,name="Praveen",place="HYD",course="DA",marks=44)
# ]

@app.get("/stud")
def cls_students():
    return students_data

@app.get("/sid/{id}")
def student_by_id(id : int):
    for student in students_data:
        if student["id"]==id:
            return student
    return "student not found"

@app.get("/courses")
def get_courses():
    courses=set()
    for student in students_data:
        courses.add(student['course'])
    if courses:
        return courses
    else:
        return "No courses found"

@app.get("/names")
def get_names():
    names=set()
    for student in students_data:
        names.add(student['name'])
    if names:
        return names
    else:
        return "No names found"
    
@app.get("/places")
def get_places():
    places=set()
    for student in students_data:
        places.add(student['place'])
    if places:
        return places
    else:
        return "No places found"