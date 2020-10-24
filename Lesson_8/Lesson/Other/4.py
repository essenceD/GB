class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name and surname: {self.name} {self.surname}"


class Teacher(Person):

    def to_teach(self, subj, *pupils):
        for pupil in pupils:
            pupil.to_take(subj)


class Pupil(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledges = []

    def to_take(self, subj):
        self.knowledges.append(subj)


class Subject:

    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def my_list(self):
        return self.subjects
