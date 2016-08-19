import pytest
import sympy
from sympy.core.expr import AtomicExpr

import solver


@pytest.fixture
def eq(request):
    equation = solver.Equation('F', 'a*m')
    return equation


class TestEquation:
    def test_init(self):
        # Should be F = m*a
        lhs = 'F'
        rhs = 'a*m'

        eq = solver.Equation(lhs, rhs)

        assert isinstance(eq.lhs, sympy.Symbol)
        assert isinstance(eq.rhs, sympy.Mul)
        assert eq.lhs.name == lhs
        assert str(eq.rhs) == rhs
        assert eq.description == ''

    def test_solve(self, eq):
        # Solve F = ma, given m=2 (kg), a = 4 (m/s^2)
        F = sympy.symbols('F')
        should_be = [{F: 8}]
        solution = eq.solve(a=4, m=2)
        assert solution == should_be

    def test_solve_throws_for_invalid_number_of_variables(self, eq):
        with pytest.raises(ValueError):
            eq.solve(a=4)

        with pytest.raises(ValueError):
            eq.solve(F=1, m=4, a=3)


