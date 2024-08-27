student = {
    "name": "Khursheed",
    "age": 21,
    "id": "F20220650...",
    "subjects": ["DBMS", "OS", "DSA"],
    "skills": {
        "web": "MERN stack",
        "programmingLanguage": ["C++", "Python", "Javascript"]
    }
}

print(student)
print(type(student))
print(student["skills"])
print(student["subjects"])

student["age"] = 22
print(student)

student["semester"] = 5
print(student)

print(student.keys())
print(len(student))
print(student.values())
print(student.items())
print(student.get("id"))

newData = {
    "newSubjects": ["OOP", "DM"]
}

student.update(newData)

print(student)