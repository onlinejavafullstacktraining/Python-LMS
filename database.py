# This will act as an in-memory database
users_db = {}
courses_db = {}
enrollments_db = {}

def add_user(user_id, user_data):
    users_db[user_id] = user_data

def get_user(user_id):
    return users_db.get(user_id)

def add_course(course_id, course_data):
    courses_db[course_id] = course_data

def get_course(course_id):
    return courses_db.get(course_id)

def enroll_user_in_course(user_id, course_id):
    if user_id not in enrollments_db:
        enrollments_db[user_id] = []
    enrollments_db[user_id].append(course_id)

def get_user_enrollments(user_id):
    return enrollments_db.get(user_id, [])
