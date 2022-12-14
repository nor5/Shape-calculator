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
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture (self):
    picture = ""
    if self.width >50 or self.height > 50:
      return "Too big for picture."
    else:
      for i in range (0, self.height):
        for j in range (0, self.width):
          
          picture += "*"
        picture += "\n"
      #ure))  
      return picture
  
  def __str__(self):
    rectangle = f"Rectangle(width={str(self.width)}, height={str(self.height)})"
    return  rectangle
 
   
  def get_amount_inside(self, shape):
    nbr_shape = 0
    if self.width > shape.width  and self.height > shape.height :
      nbr_shape = ( self.width // shape.width )* (self.height // shape.height)
     
   # elif shape.width == 0 or shape.height == 0 or shape. width == None or shape.height == None or self.width == 0 or self.height==0:
   #  nbr_shape = 0
     
    #elif self.width == None or self.height == None or self.width == 0 or self.height==0:
    # nbr_shape = 0
     
    return nbr_shape


class Square(Rectangle):
  def __init__(self, side):
        
        super().__init__(side, side)
        self.side = side
    

  def set_side(self, side):
    
    self.side = side
    super().set_width(side)
    super().set_height(side)
  
  def set_width(self,side):
    self.set_side(side)
  def set_height(self,side):
    self.set_side(side)
  def __str__(self):
    return f"Square(side={self.side})"
