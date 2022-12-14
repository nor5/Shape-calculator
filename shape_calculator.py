class Rectangle:
  def __init__(self, width , height):
    self.width = width
    self.height = height
  def set_width(self , width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
   area = self.width * self.height
   return area
  
  def get_perimeter (self):
    perimeter = self.width *2 + self.height *2
    return perimeter
  def get_diagonal(self):
    diagonal = (sel.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture (self):
    picture = ""
    if self.width >50 and self.height > 50:
      return "Too big for picture"
    else:
      for i in range (0, self.height):
        for j in range (0, self.width):
          
          picture += "*"
        picture += "\n"
      #ure))  
      return picture
  
  def __str__(self):
    rectangle = "Rectangle(width="+ str(self.width)+", height="+str(self.height)+")"
    return  rectangle
    
  def get_amount_inside(self, shape):
    
    return 


#class Square:
