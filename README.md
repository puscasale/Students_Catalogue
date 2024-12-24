# Student Catalog

## Description
This project is a student and course management catalog in a console-based application. Users can add, modify, and delete students and courses, assign grades, and view statistics on student performance.

## Features
- **Student Management**
  - Add student
  - Modify student name
  - Delete student
  - Search student
  - Generate random students
- **Course Management**
  - Add course
  - Modify course name
  - Modify course instructor
  - Delete course
  - Search course
- **Grade Management**
  - Assign grades to students for courses
  - View grades for students
- **Statistics**
  - List students and their grades for a course
  - List students sorted alphabetically by name
  - List students sorted by grade in a course
  - Top 20% of students based on average grade

## Project Structure

### `domain`
- `domain_student.py`: Contains the definition of the `Student` class with the necessary attributes and methods.
- `domain_subject.py`: Defines the `Subject` class with the necessary attributes and methods.
- `domain_grade.py` : Defines the `Grade` class for managing the grades assigned to students.

### `repository`
- `repository_student.py`: Repository for managing students, providing methods for adding, searching, deleting, and modifying students.
- `repository_subject.py`: Repository for managing courses, providing methods for adding, searching, deleting, and modifying courses.
- `repository_grade.py`: Repository for managing grades, providing methods for assigning and fetching grades for students.

### `controller`
- `controller_student.py`: Contains the business logic for managing students.
- `controller_subject.py`: Contains the business logic for managing courses.
- `controller_grade.py`: Contains the business logic for assigning grades to students.

### `user_interface`
- `menu.py`: Defines the menus for user interaction.
- `validator.py`: Contains validators to check the validity of user inputs.
- `ui.py`: Contains the logic for the user interface (UI), including managing interactions through menus.


