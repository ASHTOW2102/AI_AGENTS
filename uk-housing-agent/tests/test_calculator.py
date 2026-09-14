from tools.calculator import _eval
import ast

def test_calculator():
    assert _eval(ast.parse("100 * 1.2", mode="eval")) == 120
