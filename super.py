class University:
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
   
  def disp(self):
    print('You are in University class disp method')
 
class College (University):
  def __init__(self):
    super().__init__()
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')
 
  def show(self):
    print('College class instance method:',self.name)
 
college = College()
college.show()
college.disp()