class Person:
  def __init__(self): 
    self.name = 'Manjula'
    self.__lastname = 'Dube'
    
  def PrintName(self):
    return self.name +' ' + self.__lastname
    
#Outside class    
P = Person()
print(P.name)
print(P.PrintName())
print(P.__lastname)