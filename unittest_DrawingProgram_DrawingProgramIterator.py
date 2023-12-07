"""
Name: Aqueno Nirasmi, Minna Chae, Sarah St. Albin
Assignment: Inheritance, Composition and More Patterns
Class: TCSS 502
"""
"""
This test case imports from shapes and Drawing Program 
to run the test cases. 
This is done instead of coding within Drawing Program to preserve debugging code
"""


from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
import unittest


class MyDrawingProgramTest(unittest.TestCase):
    def test_add_Shape(self):
        program = DrawingProgram()
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        program.add_shape(rectangle_add)
        self.assertIn(rectangle_add, program, "Not equal")

    def test_remove_shape(self):
        program = DrawingProgram()
        #creating Shapes
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_add = ShapeFactory.create_shape("Circle", 1)
        #Add Shapes
        program.add_shape(rectangle_add)
        program.add_shape(circle_add)
        #Removing Shapes
        remove_count=0
        remove_count += program.remove_shape("Rectangle")
        remove_count += program.remove_shape("Circle")
        #check if rectangle is not in program

        self.assertNotIn(rectangle_add, program)
        self.assertNotIn(circle_add, program)
        self.assertEqual(remove_count, 1, "Not equal")

    def test_sort_empty_list(self):
        #sorting empty list will raise indexError
        program = DrawingProgram()
        with self.assertRaises(IndexError):
            program.sort_shapes()

    def test_sort_one_shape(self):
        # Sorting 1 shape
        #creating Shapes
        program = DrawingProgram()
        rectangle_add = ShapeFactory.create_shape("Rectangle", 2, 3)
        #Add Shapes
        program.add_shape(rectangle_add)
        program.sort_shapes()
        self.assertIn(rectangle_add, program, "Not equal")


    def test_sort_shapes_asce(self):
        # Sort multiple shapes ascending order
        #creating Shapes
        program = DrawingProgram()
        # creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)
        # Add Shapes
        program.add_shape(circle_one)
        program.add_shape(circle_two)
        program.add_shape(rectangle_one)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(square_two)
        program.add_shape(triangle_one)
        program.add_shape(triangle_two)

        expected_order = [circle_one, circle_two, rectangle_one, rectangle_two, square_one,
                          square_two, triangle_one, triangle_two]
        # stringShape = [str(shape) for shape in expected_order]
        # "\n".join(stringShape) + "\n"
        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        # sort shape
        program.sort_shapes()
        self.assertEqual(program.__str__(), expected_string, "Not equal")

    def test_sort_shapes_desc(self):
        # Sort multiple shapes descending order
        program = DrawingProgram()
        # creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)

        # Add Shapes
        program.add_shape(circle_one)
        program.add_shape(circle_two)
        program.add_shape(rectangle_one)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(square_two)
        program.add_shape(triangle_one)
        program.add_shape(triangle_two)

        expected_order = [circle_one, circle_two, rectangle_one, rectangle_two, square_one,
                          square_two, triangle_one, triangle_two]

        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        # sort shape
        program.sort_shapes()
        self.assertEqual(program.__str__(), expected_string, "Not equal")


    def test_sort_shapes_random(self):
        # Sort multiple shapes in random order
        program = DrawingProgram()
        # creating Shapes
        rectangle_one = ShapeFactory.create_shape("Rectangle", 1, 2)
        rectangle_two = ShapeFactory.create_shape("Rectangle", 2, 3)
        circle_one = ShapeFactory.create_shape("Circle", 1)
        circle_two = ShapeFactory.create_shape("Circle", 2)
        triangle_one = ShapeFactory.create_shape("Triangle", 1, 2, 3)
        triangle_two = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        square_one = ShapeFactory.create_shape("Square", 1)
        square_two = ShapeFactory.create_shape("Square", 2)

        # Add Shapes
        program.add_shape(rectangle_one)
        program.add_shape(square_two)
        program.add_shape(triangle_two)
        program.add_shape(rectangle_two)
        program.add_shape(square_one)
        program.add_shape(circle_two)
        program.add_shape(triangle_one)
        program.add_shape(circle_one)

        expected_order = [circle_one, circle_two, rectangle_one, rectangle_two, square_one,
                          square_two, triangle_one, triangle_two]

        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        # sort shape
        program.sort_shapes()
        self.assertEqual(program.__str__(), expected_string, "Not equal")

    def test_print_shapes(self):
        # Test print shapes
        program = DrawingProgram()
        circle_small = ShapeFactory.create_shape("Circle", 1)
        circle_large = ShapeFactory.create_shape("Circle", 5)
        square_small = ShapeFactory.create_shape("Square", 1)
        square_large = ShapeFactory.create_shape("Square", 5)
        rectangle = ShapeFactory.create_shape("Rectangle", 2, 3)
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)

        program.add_shape(circle_small)
        program.add_shape(circle_large)
        program.add_shape(square_small)
        program.add_shape(square_large)
        program.add_shape(rectangle)
        program.add_shape(triangle)

        print_shape = program.print_shape("Circle")

        expected_string = str(circle_small) + "\n" + str(circle_large) + "\n"

        self.assertEqual(print_shape, expected_string, "Not equal")


    def test_get_shape(self):
        #test get shape
        program = DrawingProgram()
        circle = ShapeFactory.create_shape("Circle", 1)
        program.add_shape(circle)

        get_shape = program.get_shape(0)
        self.assertEqual(get_shape, circle)

    def test_set_shape(self):
        #Test set shape
        program = DrawingProgram()
        circle_small = ShapeFactory.create_shape("Circle", 1)
        circle_large = ShapeFactory.create_shape("Circle", 5)
        square_small = ShapeFactory.create_shape("Square", 1)
        square_large = ShapeFactory.create_shape("Square", 5)
        rectangle = ShapeFactory.create_shape("Rectangle", 2, 3)
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)

        program.add_shape(circle_small)
        program.add_shape(circle_large)
        program.add_shape(square_small)
        program.add_shape(square_large)
        program.add_shape(rectangle)
        program.add_shape(triangle)

        adding_shape = ShapeFactory.create_shape("Triangle", 3,6,9)
        program.set_shape(0, adding_shape)

        expected_order = [adding_shape, circle_large, square_small, square_large, rectangle,
                          triangle]

        expected_string = ""
        for shape in expected_order:
            expected_string += str(shape) + "\n"

        self.assertEqual(program.__str__(), expected_string, "Not equal")


class MyDrawingProgramIteratorTest(unittest.TestCase):
# •	DrawingProgramIterator class functionality
# o	use of for loop as shown above demonstrates this class works
# o	be sure and use it with a DrawingProgram object that has no shapes, one shape, then maybe 5 shapes

    def test_iter_with_many_shapes(self):
        # Test Iterator iterating through many shapes
        # print("---------------Testing iter class for many shapes---------------")
        program = DrawingProgram()
        circle_small = ShapeFactory.create_shape("Circle", 1)
        circle_large = ShapeFactory.create_shape("Circle", 5)
        square_small = ShapeFactory.create_shape("Square", 1)
        square_large = ShapeFactory.create_shape("Square", 5)
        rectangle = ShapeFactory.create_shape("Rectangle", 2, 3)
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)

        program.add_shape(circle_small)
        program.add_shape(circle_large)
        program.add_shape(square_small)
        program.add_shape(square_large)
        program.add_shape(rectangle)
        program.add_shape(triangle)


        #tests for next function in the iteration protocol
        for i in program:
            self.assertRaises(StopIteration)

        iter_string=""

        for shape in program:
            iter_string += str(shape) +"\n"

        self.assertEqual(program.__str__(), iter_string, "Not equal")

    def test_iter_without_shapes(self):
        #Tests the iter function with no shapes where inter returns an IndexError

        program = DrawingProgram()
        with self.assertRaises(IndexError):
            for shape in program:
                print(shape)

    def test_iter_one_shape(self):
        # Test Iterator iterating through one shape

        program = DrawingProgram()
        circle_one = ShapeFactory.create_shape("Circle", 1)
        program.add_shape(circle_one)

        for i in program:
            self.assertRaises(StopIteration)

        iter_string=""

        for shape in program:
            iter_string += str(shape) +"\n"

        self.assertEqual(program.__str__(), iter_string, "Not equal")

if __name__ == '__main__':
    unittest.main()