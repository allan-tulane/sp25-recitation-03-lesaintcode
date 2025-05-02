from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(9), BinaryNumber(11)) == 99
    assert quadratic_multiply(BinaryNumber(14), BinaryNumber(2)) == 28
    assert quadratic_multiply(BinaryNumber(13), BinaryNumber(13)) == 169
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(123)) == 123
    assert quadratic_multiply(BinaryNumber(5), BinaryNumber(20)) == 100
