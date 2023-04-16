#Degree rotations test
#Jeffrey McCullough
#This project runs tests on the degree rotations function.
#March 7, 2023

import unittest
from degreeRotation import degRot

class DegreesTestCase(unittest.TestCase):
 
    def test_past_degree_rotation(self):
        result = degRot(460)
        self.assertEqual(result, 100)

    def test_not_past_degree_rotation(self):
        result = degRot(100)
        self.assertEqual(result, 100)
        

if __name__ == "__main__":
    unittest.main()