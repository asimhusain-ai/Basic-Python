File = "TMU_Courses.txt"

with open(File, 'a') as file:
    additional_courses = [
        "6. ME (In Collaboration with TCS ION)",
        "7. PH.D. Chemistry",
        "8. Ph.D. Mathematics",
        "9. B.A. - LL.B(Hons.)",
        "10. M.B.B.S(Bachelor of Medicine and Bachelor of Surgery)"
    ]

    for course in additional_courses:
        file.write(course + '\n')

with open(File, 'r') as file:
    contents = file.read()
    print(contents)