class University:
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
   
  def disp(self):
    print('You are in University class disp method')
 
class College (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')
 
  def show(self):
    print('College class instance method:',self.name)
 
class Student(College):
  def __init__(self):
    self.name='Martin'
    print('You are in student Class Constructor')
 
  def view(self):
    print('Student class instance method:',self.name)
 
student = Student()
student.view()
student.show()
student.disp()