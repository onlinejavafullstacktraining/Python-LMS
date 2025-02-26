from user import User
from course import Course
from database import get_user_enrollments


def main():
    print("Welcome to the LMS!")

    # Simple menu for user interaction
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. View all courses")
        print("4. Enroll in a course")
        print("5. View enrolled courses")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':  # Register
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = len(users_db) + 1
            user = User(user_id, username, password)
            user.register()
            print("Registration successful!")

        elif choice == '2':  # Login
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = User.login(username, password)
            if user:
                print(f"Welcome {user.username}!")
            else:
                print("Invalid credentials!")

        elif choice == '3':  # View all courses
            courses = Course.view_all_courses()
            if courses:
                for idx, course in enumerate(courses, 1):
                    print(f"{idx}. {course['name']}: {course['description']}")
            else:
                print("No courses available.")

        elif choice == '4':  # Enroll in a course
            if not user:
                print("You need to login first.")
                continue
            course_id = int(input("Enter course ID to enroll: "))
            courses = Course.view_all_courses()
            if course_id <= len(courses):
                course = courses[course_id - 1]
                Course.enroll_user(user, course['name'])
                print(f"You've been enrolled in {course['name']}.")
            else:
                print("Invalid course ID.")

        elif choice == '5':  # View enrolled courses
            if not user:
                print("You need to login first.")
                continue
            enrolled_courses = get_user_enrollments(user.user_id)
            if enrolled_courses:
                for course_name in enrolled_courses:
                    print(course_name)
            else:
                print("You are not enrolled in any courses.")

        elif choice == '6':  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
