class student:
    def __init__(self, name, standard, gpa, is_on_probation):
        self.name = name
        self.standard = standard
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_roll_honour(self):
        if self.gpa >= 7.5:
            return True
        else:
            return False
