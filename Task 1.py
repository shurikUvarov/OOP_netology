class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(self, Reviewer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def get_average_grade(self):
        total_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()])
        return total_grade / len(self.grades)


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()]) / len(self.grades)
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: " \
               f"{average_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\n" \
               f"Завершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __gt__(self, other):
        return self.get_average_grade() > other.get_average_grade()

    def __le__(self, other):
        return self.get_average_grade() <= other.get_average_grade()

    def __ge__(self, other):
        return self.get_average_grade() >= other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def get_average_grade(self):
        total_grade = sum([sum(grades) / len(grades) for grades in self.grades.values()])
        return total_grade / len(self.grades)

some_student = Student('Ruoy', 'Eman', 'man')
some_student.courses_in_progress += ['Python']
some_lecturer = Lecturer('Some', 'Lecturer')
some_lecturer.courses_attached+=['Python']
some_reviewer = Reviewer('John', 'Doe')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_student.rate_lecture(some_lecturer,'Python', 10)
some_student.rate_lecture(some_lecturer,'Java', 3)
some_student.rate_lecture(some_lecturer,'Python', 7)
some_student.finished_courses+=['Введение']

some_student1 = Student('Ivan', 'Ivanov', 'man')
some_student1.courses_in_progress += ['Python']
some_lecturer1 = Lecturer('Indiana', 'Johns')
some_lecturer1.courses_attached+=['Python']
some_reviewer1 = Reviewer('Harrison', 'Ford')
some_reviewer1.courses_attached += ['Python']

some_reviewer1.rate_hw(some_student, 'Python', 5)
some_reviewer1.rate_hw(some_student, 'Python', 7)
some_reviewer1.rate_hw(some_student, 'Python', 2)
some_student1.rate_lecture(some_lecturer,'Python', 3)
some_student1.rate_lecture(some_lecturer,'Java', 5)
some_student1.rate_lecture(some_lecturer,'Python', 8)
some_student1.finished_courses+=['Введение']

def calculate_average_grade_by_course(units, course):
    grades_sum = 0
    unit_count = 0
    for unit in units:
        if course in unit.grades:
            grades_sum += sum(unit.grades[course])
            unit_count += len(unit.grades[course])
    if unit_count > 0:
        return grades_sum / unit_count
    else:
        return 0
# Пример использования функции
students = [some_student1, some_student]
course = "Python"
average_grade = calculate_average_grade_by_course(students, course)
print(f"Средняя оценка за домашние задания по курсу {course}: {average_grade}")

lecturers = [some_lecturer, some_lecturer1]
course = "Python"
average_grade = calculate_average_grade_by_course(lecturers, course)
print(f"Средняя оценка за домашние задания по курсу {course}: {average_grade}")




