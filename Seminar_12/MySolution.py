import csv


class FullNameValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value is not None and (not value.istitle() or not value.replace(" ", "").isalpha()):
            raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name] if self.name in instance.__dict__ else None


class Student:
    name = FullNameValidator()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            subjects = file.read().split(',')
            self.subjects = {subject: {'grades': [], 'test_scores': []} for subject in subjects}

    def add_grade(self, subject, grade):
        if grade not in range(2, 6):
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if test_score not in range(0, 101):
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        scores = self.subjects[subject]['test_scores']
        return sum(scores) / len(scores) if scores else 0

    def get_average_grade(self):
        all_grades = [grade for subject in self.subjects for grade in self.subjects[subject]['grades']]
        return sum(all_grades) / len(all_grades) if all_grades else 0


    def __str__(self):
        subject_list = ', '.join(subject for subject in self.subjects if self.subjects[subject]['grades'])
        return f'Студент: {self.name}\nПредметы: {subject_list}'

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)