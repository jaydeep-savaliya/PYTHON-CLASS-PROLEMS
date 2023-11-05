class University:
  def __init__(self):
    self.name = 'Yele University'
    print("You are in University Class Constructor")
 
class College (University):
  def __init__(self):
    self.name = 'Yale School of Medicine'
    print('You are in college Class Constructor')
 
  def show(self):
    print('College class instance method:',self.name)
    
college = College()
college.show()