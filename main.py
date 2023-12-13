# from ShapeFactory import ShapeFactory
# from shapes import Circle, Square, Triangle, Rectangle
# from DrawingProgram import DrawingProgram
# # r = ShapeFactory.create_shape("Rectangle", length=3, width=5)
# # print(r.length)
#
#
# def dp_test():
#     dp = DrawingProgram()
#
#     # add Shape
#     # dp.add_shape(Circle(2))
#     # print(dp)
#     dp.add_shape(ShapeFactory.create_shape("Rectangle", 3, 4))
#     dp.add_shape(ShapeFactory.create_shape("Triangle", 2, 4, 3))
#     dp.add_shape(ShapeFactory.create_shape("Square", 3))
#     # dp.add_shape(ShapeFactory.create_shape("Triangle", 3,3)
#     dp.add_shape(ShapeFactory.create_shape("Circle", 5))
#     # dp.add_shape("Square", 2)
#     # print(dp.get_name(0))
#     # # print(dp.print_shape("Circle"))
#     # # dp.remove_shape("Circle")
#     # dp.set_shape(2,"Rectangle", 3,4)
#     print(dp)
#     # dp.clear_all_shapes()
#     dp.get_shape(3)

# bool_a = False
# bool_b = False
# results = bool_a and bool_b
#
# print(results)

import random

list = ["V", "H", "P", ""]

results = random.sample(list, 3)
# print(results)
for value in results:
    if value == "V":
        print("v")
    if value == "H":
        print("H")
    if value == "P":
        print("P")


#
# dp_test()
#
# # TESTS
# # my_fun_program = DrawingProgramMain()
# # my_fun_program.run_program()
#
# # d = DrawingProgram()
# # d.add_shape(ShapeFactory.create_shape("rectangle", length = 5, width=6))
# # d.add_shape(ShapeFactory.create_shape("circle", radius = 5))
# # print(d)
#
#
# # creating each shape's array to "sort" them
# # list_rec = []
# # list_sq = []
# # list_cir = []
# # list_tri = []
# # # print(self.name)
# #
# # #looping through list and placing Shape objects into their specific array
# # for shape in self.list_shapes:
# #     if shape.get_name() == "Circle":
# #         list_cir.append(shape)
# #     if shape.get_name() == "Rectangle":
# #         list_rec.append(shape)
# #     if shape.get_name() == "Square":
# #         list_sq.append(shape)
# #     if shape.get_name() == "Triangle":
# #         list_tri.append(shape)
# #
# # #looping through the arrays to put into a string. Need more conditions
# # #to check for empty arrays. This code will probably not be the final code
# # for shape in list_cir:
# #     self.string += str(shape) + ", "
# # self.string += "\n"
# # for shape in list_rec:
# #     self.string += str(shape) + ", "
# # for shape in list_sq:
# #     self.string += str(shape) + ", "
# # self.string += "\n"
# # for shape in list_tri:
# #     self.string += str(shape) + ", "
# # self.string += "\n"
# # return f"{self.string}"
#
# # class ShapeFactory:
# #     @staticmethod
# #     def create_shape(shape_name, *args):
# #         if shape_name == "Circle":
# #             return Circle(*args)
# #         # Add conditions for Square, Rectangle, Triangle
# #         else:
# #             raise ValueError("Unknown shape type")
#
# # self.__list_shapes.sort(key=lambda x: (x.name, x.area()))

doors
        checking for southdoor and eastdoor
    door cannot be east if col

