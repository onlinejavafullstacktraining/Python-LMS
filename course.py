from database import add_course, get_course, enroll_user_in_course, get_user_enrollments

class Course:
    def __init__(self, course_id, name, description):
        self.course_id = course_id
        self.name = name
        self.description = description

    def create_course(self):
        add_course(self.course_id, {"name": self.name, "description": self.description})

    @staticmethod
    def view_course(course_id):
        course = get_course(course_id)
        if course:
            return course
        return None

    @staticmethod
    def view_all_courses():
        return list(courses_db.values())

    @staticmethod
    def enroll_user(user, course_id):
        enroll_user_in_course(user.user_id, course_id)
