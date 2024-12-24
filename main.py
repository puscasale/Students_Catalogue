
from controller.controller_grade import Grade_Manager
from controller.controller_student import Student_Controller
from controller.controller_subject import Subject_Controller
from repository.repository_grade import Grade_Repository_file
from repository.repository_student import Student_repository_file
from repository.repository_subject import Subject_Repository_file
from user_interface.ui import UI
from user_interface.validator import Student_Validator, Subject_Validator, Validator



def main():
    student_repo = Student_repository_file("data/students.txt")
    student_validator = Student_Validator()
    student_control = Student_Controller(student_repo, student_validator)

    subject_repo = Subject_Repository_file("data/subjects.txt")
    subject_validator = Subject_Validator()
    subject_control = Subject_Controller(subject_repo, subject_validator)

    grade_repo = Grade_Repository_file("data/grades.txt")

    validator = Validator()

    common_control = Grade_Manager(grade_repo, student_repo)

    console = UI(student_control, subject_control, common_control)
    console.option_main_menu()

if __name__ == "__main__":
    main()

