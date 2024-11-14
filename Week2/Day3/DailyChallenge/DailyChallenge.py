# import math as m
# import turtle as t

# class Circle:
#     circle_list = []
#     def __init__(self, radius=None , diameter=None):
#         self.radius = radius
#         self.diameter = diameter
        
#         if radius is not None:
#             self.radius = radius
#             self.diameter = radius * 2
#         elif diameter is not None: 
#             self.diameter = diameter
#             self.radius = diameter / 2 
#         else: 
#             raise ValueError("Soit le Radius soit le Diameter doivent etre spécifié")
        
#     def __str__(self):
#         return f"radius: {self.radius} diameter: {self.diameter}"
    
#     def __add__(self, other_circle):
#         if isinstance(other_circle, Circle):
#             new_radius = self.radius + other_circle.radius
#         else:
#             raise ValueError("u can only add an other object")
#         return Circle(new_radius)
        
#     def __gt__(self, other_circle):
#         if isinstance(other_circle, Circle):
#             if self.radius > other_circle.radius:
#                 return True
#             else:
#                 return False
#         else:
#             raise ValueError("u can only add an other object")
        
#     def __eq__(self, other_circle):
#         if isinstance(other_circle, Circle):
#             if self.radius == other_circle.radius:
#                 return True
#             else: 
#                 return False
#         else:
#             raise ValueError('u can only compare object')

#     def area_circle(self):
#         return f"area of the circle: {round(m.pi*self.radius**2, 1)}"
    
#     def add_to_list(self):
#        lst =  Circle.circle_list.append(self)


#     def draw_circle(self):
#         turtle = t.Turtle()
#         turtle.speed(1)
#         turtle.circle(self.radius)
    
        

#     @classmethod
#     def show_list(cls):
#         for circle in cls.circle_list:
#             print(circle)
        
        

    



# john_circle = Circle(150)
# yael_circle = Circle(100)
# print(john_circle.area_circle())
# print(john_circle + yael_circle)
# print(john_circle > yael_circle)
# print(yael_circle == john_circle)
# john_circle.add_to_list()
# yael_circle.add_to_list()
# Circle.show_list()
# john_circle.draw_circle()
# yael_circle.draw_circle()


