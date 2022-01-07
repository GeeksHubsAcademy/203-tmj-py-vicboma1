import pytest
import unittest   # The test framework
import math 

from kata import apply

class Test_kata(unittest.TestCase):
    
    def test_apply_1(self):
        expected =  1.0
        result = apply(12, 0)
        assert(expected == result)

    def test_apply_2(self):
        expected =  math.pow(1.7,308)
        result = apply(0, 12)
        assert(expected == result)

    def test_apply_3(self):
        expected =  math.pow(1.7,308)
        result = apply(0, -1)
        assert(expected == result) 

    def test_apply_4(self):
        expected =  1.0
        result = apply(-12, 0)
        assert(expected == result)

    def test_apply_5(self):
        expected =  1.0
        result = apply(10, 0)
        assert(expected == result)

    def test_apply_6(self):
        expected =  1e-05
        result = apply(10, -5)
        assert(expected == result)

    def test_apply_7(self):
        expected =  1.0
        result = apply(1, 120)
        assert(expected == result)

    def test_apply_8(self):
        expected =  1.0
        result = apply(-1, 120)
        assert(expected == result) 

    def test_apply_9(self):
        expected =  1.0e10
        result = apply(10, 10)
        assert(expected == result)
    def test_apply_10(self):
        expected =  169.0
        result = apply(-13, 2)
        assert(expected == result)

    def test_apply_11(self):
        expected =  248832.0
        result = apply(12, 5)
        assert(expected == result) 

    def test_apply_12(self):
        expected =  -62748517.0
        result = apply(-13, 7)
        assert(expected == result) 

    def test_apply_13(self):
        expected =   0.008
        result = apply(5, -3)
        assert(expected == result) 

    def test_apply_14(self):
        expected =  0.25
        result = apply(-2, -2)
        assert(expected == result) 

    def test_apply_15(self):
        expected =  0.03125
        result = apply(2, -5)
        assert(expected == result) 

    def test_apply_16(self):
        expected =  -0.0078125
        result = apply(-2, -7)
        assert(expected == result) 

    def test_apply_17(self):
        expected =  1.0
        result = apply(0, 0)
        assert(expected == result) 
    

if __name__ == '__main__':
	unittest.main()