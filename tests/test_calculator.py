import py.test
from calculator import calculator as c

def test_calculator_is_initiated():
    calc = c.Calculator() 
    assert calc.result == 0
    
def test_basic_calculator_functionality():
    calc = c.Calculator() 
    calc.add(5)
    assert calc.result == 5
    calc.subtract(15)
    assert calc.result == -10
    calc.multiply_by(-5)
    assert calc.result == 50
    calc.divide_by(5)
    assert calc.result == 10
    
    calc.reset()
    assert calc.result == 0
    calc.reset(to=100)
    assert calc.result == 100
    
    calc.sqrt()
    assert calc.result == 10
    calc.exponentiate(3)
    assert calc.result == 1000
    

def test_calculator_inputs():
    calc = c.Calculator() 
    # input is str insead of float:
    with py.test.raises(TypeError):
        calc.add("a")
    # too many args:
    with py.test.raises(TypeError):
        calc.add(1, 2)
