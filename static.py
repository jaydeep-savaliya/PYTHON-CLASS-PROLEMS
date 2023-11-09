class School:
    school_name = "ABC School"
    def __init__(self,name):
        self.name = name
        print(self.school_name)
        print(School.school_name)
school = School("SOS")