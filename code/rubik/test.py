import torch
import unittest
from rubik import encode, twist_right, rotate_right, flip_away, RUBIKS_CUBE

class RubiksCubeTests(unittest.TestCase):

    def test_encode(self):
        expected = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        assert encode(RUBIKS_CUBE) == expected, 'encode test failed!'
    
    def test_flip_away(self):
        desired_result = torch.tensor([[[ 7,  8,  9],
                                        [15, 16, 17],
                                        [24, 25, 26]],
        
                                       [[ 4,  5,  6],
                                        [13,  0, 14],
                                        [21, 22, 23]],
        
                                       [[ 1,  2,  3],
                                        [10, 11, 12],
                                        [18, 19, 20]]])
        assert encode(flip_away(RUBIKS_CUBE)) == encode(desired_result), 'flip away test failed!'
 
    def test_twist_right(self):
        desired_result = torch.tensor([[[ 7,  4,  1],
                                        [ 8,  5,  2],
                                        [ 9,  6,  3]],
        
                                       [[10, 11, 12],
                                        [13,  0, 14],
                                        [15, 16, 17]],
        
                                       [[18, 19, 20],
                                        [21, 22, 23],
                                        [24, 25, 26]]])
        assert encode(twist_right(RUBIKS_CUBE)) == encode(desired_result), 'twist right test failed!'
    
    def test_rotate_right(self):
        desired_result = torch.tensor( [[[ 7,  4,  1],
                                         [ 8,  5,  2],
                                         [ 9,  6,  3]],
                                
                                        [[15, 13, 10],
                                         [16,  0, 11],
                                         [17, 14, 12]],
                                
                                        [[24, 21, 18],
                                         [25, 22, 19],
                                         [26, 23, 20]]])
        assert encode(rotate_right(RUBIKS_CUBE)) == encode(desired_result), 'rotate right test failed!'
    
            
if __name__ == "__main__":
    unittest.main() # run all tests