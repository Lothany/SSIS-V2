import sys
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="ssis"
)

mycursor = mydb.cursor()


def menu():
    print("\nPress any key to return to menu")
    print("Press 0 to exit")
    answer = input(">> ")

    if answer == '0':
        sys.exit(0)
    else:
        main()


class Course:
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name

    @staticmethod
    def display(course):
        code = course[0]
        name = course[1]
        print(f"\n    Course Code: {code}")
        print(f"    Course Name: {name}")

    @staticmethod
    def find(keyword):
        query = "SELECT * FROM courses WHERE code = %s OR name LIKE %s"
        mycursor.execute(query, (keyword, f"%{keyword}%"))
        results = mycursor.fetchall()
        if results:
            return True, results
        else:
            return False, results

    @staticmethod
    def find_code(code):
        query = "SELECT * FROM courses where code = %s or name = %s"
        mycursor.execute(query, (code, code))
        results = mycursor.fetchall()
        if results:
            return True, results
        else:
            return False, results

    @staticmethod
    def view_all():
        query = "SELECT * FROM courses"
        mycursor.execute(query)
        courses = mycursor.fetchall()
        for course in courses:
            code = course[0]
            name = course[1]
            print(f"{code} - {name}")

    def add(self):
        print("\nEnter New Course")
        new_code = input("Course Code: ")
        new_code = new_code.upper()
        code_exists, codes = self.find_code(new_code)
        if code_exists:
            print("This course code is already taken")
            return

        new_name = input("Course Name: ")
        name_exists, names = self.find_code(new_name)
        if name_exists:
            print("This course name is  already taken")
            return

        mycursor.execute("INSERT INTO courses (`code`, `name`) VALUES (%s, %s)", (new_code, new_name))
        mydb.commit()
        print("\nCourse successfully added")

        return new_code

    def search(self):
        print("\nEnter Course Code or Name")
        keyword = input("Search: ")

        is_found, results = self.find(keyword)
        if is_found:
            for course in results:
                self.display(course)
                code = course[0]
                self.show_students(code)
        else:
            print("Course not found")

    @staticmethod
    def show_students(course_code):
        print(f"    Students:")
        query = "SELECT * FROM students WHERE course = %s"
        mycursor.execute(query, (course_code,))
        enrolled = mycursor.fetchall()
        for student in enrolled:
            id_num = student[0]
            first_name = student[1]
            last_name = student[2]
            year_level = student[3]
            print(f"              {id_num} | {first_name}, {last_name} | Year {year_level}")

    def update(self):
        print("\nEnter code or name of course to be updated")
        keyword = input("Course: ")

        is_found, results = self.find(keyword)
        if is_found:
            for course in results:
                self.display(course)
                code = course[0]

            print("\nEnter new course code and name")
            new_code = input("Code: ")
            new_code = new_code.upper()
            new_name = input("Name: ")

            # Update the 'course' column in the 'students' table
            query_update_students = "UPDATE students SET course = %s WHERE course = %s"
            mycursor.execute(query_update_students, (new_code, code))
            mydb.commit()

            query_update_course = "UPDATE courses SET code = %s, name = %s WHERE code = %s"
            mycursor.execute(query_update_course, (new_code, new_name, code))
            mydb.commit()

            print("\nUpdate successful")
        else:
            print("\nCourse does not exist")

    def delete(self):
        print("\nEnter course code be deleted")
        keyword = input("Course: ")
        keyword = keyword.upper()
        is_found, results = self.find_code(keyword)
        if is_found:
            for course in results:
                self.display(course)
            print("\nDelete this course and all students under it? (y/n)")
            select = input(">> ")
            if select.upper() == "Y":
                query = "DELETE FROM courses WHERE code = %s"
                mycursor.execute(query, (keyword,))
                mydb.commit()
                print("\nCourse deleted")
            else:
                print("\nCourse was not deleted")
        else:
            print("\nCourse not found")


class Student:
    def __init__(self, id_num=None, first_name=None, last_name=None, year_level=None, gender=None, course=None):
        self.id_num = id_num
        self.first_name = first_name
        self.last_name = last_name
        self.year_level = year_level
        self.gender = gender
        self.course = course

    @staticmethod
    def display(students):
        for student in students:
            id_num = student[0]
            first_name = student[1]
            last_name = student[2]
            year_level = student[3]
            gender = student[4]
            course = student[5]

            print(f"\n    Name:       {first_name}, {last_name}")
            print(f"    ID Number:  {id_num}")
            print(f"    Course:     {course}")
            print(f"    Gender:     {gender}")
            print(f"    Year:       {year_level}")

    @staticmethod
    def find(keyword):
        query = "SELECT * FROM students WHERE id_num = %s OR first_name LIKE %s OR last_name LIKE %s"
        wildcard_keyword = f"%{keyword}%"
        mycursor.execute(query, (keyword, wildcard_keyword, wildcard_keyword))
        results = mycursor.fetchall()
        if results:
            return True, results
        else:
            return False, results

    @staticmethod
    def find_id(id_num):
        query = "SELECT * FROM students WHERE id_num = %s"
        mycursor.execute(query, (id_num,))
        results = mycursor.fetchall()
        if results:
            return True, results
        else:
            return False, results

    @staticmethod
    def view_all():
        query = "SELECT * FROM students"
        mycursor.execute(query)
        students = mycursor.fetchall()
        for student in students:
            id_num = student[0]
            first_name = student[1]
            last_name = student[2]
            year_level = student[3]
            gender = student[4]
            course = student[5]
            print(f"{id_num} | {course} | Year {year_level} | {first_name}, {last_name} | {gender}")

    @staticmethod
    def choose_gender():
        print("\nSelect Gender")
        print("1. Male")
        print("2. Female")
        print("3. Lesbian")
        print("4. Gay")
        print("5. Bisexual")
        print("6. Transgender")
        print("7. Prefer not to say")
        select = input(">> ")

        if select == "1":
            return "Male"
        elif select == "2":
            return "Female"
        elif select == "3":
            return "Lesbian"
        elif select == "4":
            return "Gay"
        elif select == "5":
            return "Bisexual"
        elif select == "6":
            return "Transgender"
        elif select == "7":
            return None
        else:
            print("Selected value is invalid")
            menu()

    @staticmethod
    def choose_course():
        query = "SELECT code FROM courses"
        mycursor.execute(query)
        courses = mycursor.fetchall()
        num_courses = len(courses)  # Store the length of courses

        print("\nSelect Course")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course[0]}")

        print("Select 0 to add a new course")
        select = int(input(">> ")) - 1

        if select < num_courses and select >= 0:
            chosen_course = courses[select][0]
        elif select == -1:
            new_course = Course()
            chosen_course = new_course.add()
        else:
            print("\nEntered value is invalid")
            menu()

        return chosen_course

    def search(self):
        print("\nEnter Student's Name or ID Number")
        keyword = input("Search: ")
        is_found, students = self.find(keyword)
        if is_found:
            self.display(students)
        else:
            print("Student not found")

    def add(self):
        print("\nEnter the required information for the new student")

        new_id = input("ID Number: ")
        id_exists, students = self.find_id(new_id)
        if id_exists:
            print("This ID number is already taken")
            return

        new_firstname = input("First Name: ")
        new_lastname = input("Last Name: ")
        new_yearlevel = input("Year Level: ")
        new_gender = self.choose_gender()
        new_course = self.choose_course()

        insert_query = "INSERT INTO students (`id_num`, `first_name`, `last_name`, `year_level`, `gender`, `course`) " \
                       "VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(insert_query, (new_id, new_firstname, new_lastname, new_yearlevel, new_gender, new_course))
        mydb.commit()
        print("\nStudent successfully added")

    def update(self):
        print("\nEnter ID Number of Student")
        idNum = input("ID Number: ")
        is_found, student = self.find_id(idNum)
        if is_found:
            self.display(student)
            print("\nEnter updated student details")

            update_id = input("ID Number: ")
            id_exists, result = self.find_id(update_id)
            if id_exists and update_id != idNum:
                print("ID Number is already taken")
                menu()

            update_first = input("First Name: ")
            update_last = input("Last Name: ")
            update_yearlevel = input("Year Level: ")
            update_gender = self.choose_gender()
            update_course = self.choose_course()

            query = "UPDATE students SET id_num = %s, first_name = %s," \
                    "last_name = %s, year_level = %s, gender = %s, course = %s WHERE id_num = %s"
            mycursor.execute(query, (
            update_id, update_first, update_last, update_yearlevel, update_gender, update_course, idNum))
            mydb.commit()
            print("\nUpdate successful")
        else:
            print("Student does not exist")

    def delete(self):
        print("\nEnter ID Number of student to be deleted")
        id_num = input("ID Number: ")
        is_found, student = self.find(id_num)
        if is_found:
            self.display(student)
            print("Delete this Student? (y/n)")
            select = input(">> ")
            if select.upper() == "Y":
                query = "DELETE FROM students WHERE id_num = %s"
                mycursor.execute(query, (id_num,))
                mydb.commit()
                print("\nStudent deleted")
            else:
                print("\nStudent was not deleted")
        else:
            print("\nStudent not found")


def view(student, course):
    print("\n1. View Students")
    print("2. View Courses")
    select = input(">> ")
    print("\n")

    if select == '1':
        student.view_all()
    elif select == '2':
        course.view_all()
    else:
        print("Selected number is invalid")
        menu()


def search(student, course):
    print("\n1. Search from Students")
    print("2. Search from Courses")
    select = input(">> ")

    if select == '1':
        student.search()
    elif select == '2':
        course.search()
    else:
        print("Selected number is invalid")
        menu()


def add(student, course):
    print("\n1. Add New Student")
    print("2. Add New Course")
    select = input(">> ")

    if select == '1':
        student.add()
    elif select == '2':
        course.add()
    else:
        print("Selected number is invalid")
        menu()


def update(student, course):
    print("\n1. Edit from Students")
    print("2. Edit from Courses")
    select = input(">> ")

    if select == '1':
        student.update()
    elif select == '2':
        course.update()
    else:
        print("Selected number is invalid")
        menu()


def delete(student, course):
    print("\n1. Delete from Students")
    print("2. Delete from Courses")
    select = input(">> ")

    if select == '1':
        student.delete()
    elif select == '2':
        course.delete()
    else:
        print("Selected number is invalid")
        menu()


def main():
    course = Course()
    student = Student()

    print("\nSelect an option")
    print("1. View")
    print("2. Search")
    print("3. Add")
    print("4. Update")
    print("5. Delete")
    select = input(">> ")

    if select == '1':
        view(student, course)
    elif select == '2':
        search(student, course)
    elif select == '3':
        add(student, course)
    elif select == '4':
        update(student, course)
    elif select == '5':
        delete(student, course)

    menu()


main()
