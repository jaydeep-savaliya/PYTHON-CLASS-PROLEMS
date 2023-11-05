class Father:
  def __init__(self):
    print('You are in Father Class Constructor')
   
  def disp(self):
    print("Father Class instance Method")
         
class Mother:
  def __init__(self):
    print("You are in Mother Class Constructor")
   
  def show(self):
    print("Mother Class instance Method")
         
class Son(Father, Mother):
    def __init__(self):
        super().__init__()
        print("You are in Son Class Constructor")
   
    def view(self):
        print("Son Class Instance Method")
         
         
son = Son()
son.view()
son.show()
son.disp()