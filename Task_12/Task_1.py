class Student:
    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects_file = subjects_file
        self.subjects = self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name':
            if not all(word.isalpha() and word.istitle() for word in value.split()):
                pass
                # print("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __str__(self):
        subjects_with_data = [subject for subject, data in self.subjects.items() if 'grade' in data or 'test_score' in data]
        subjects_str = ', '.join(subjects_with_data)
        return f"Студент: {self.name}\nПредметы: {subjects_str}" if subjects_str else f"Студент: {self.name}\nПредметы: Нет данных"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='UTF-8') as file:
            subjects_line = file.readline().strip()
            subjects_list = subjects_line.split(',')
            return {subject: {} for subject in subjects_list}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
        else:
            self.subjects[subject]['grade'] = grade

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
        else:
            self.subjects[subject]['test_score'] = test_score

    def get_average_grade(self):
        total_grades = sum(data['grade'] for data in self.subjects.values() if 'grade' in data)
        total_subjects = len([data for data in self.subjects.values() if 'grade' in data])
        return total_grades / total_subjects if total_subjects != 0 else 0

    def get_average_test_score(self, subject):
        total_scores = sum(data['test_score'] for subj, data in self.subjects.items() if subj == subject and 'test_score' in data)
        total_tests = len([data for subj, data in self.subjects.items() if subj == subject and 'test_score' in data])
        return total_scores / total_tests if total_tests != 0 else 0


student = Student("123 Иван", "subjects.csv")
