"""
A package that allows you to solve equations from their string representation
and a number of known values.
"""
import sympy


# A set of pre-defined equations in the form (LHS, RHS)
EQUATIONS = {
    'newton II': ('F', 'm*a'),
    'cos rule': ('a**2', 'b**2 + c**2 - 2*b*c*cos(theta)')
    }

# Turn the equations into their sympified form
_EQUATIONS = {key: Equation(*value)
        for key, value in EQUATIONS.items()}



class Equation:
    """
    Representation of an equation.
    """
    def __init__(self, lhs, rhs, description=''):
        self.lhs = sympy.sympify(lhs)
        self.rhs = sympy.sympify(rhs)
        self.description = description

    def __repr__(self):
        return '<{}: "{} = {}">'.format(
                self.__class__.__name__,
                self.lhs,
                self.rhs)

    def __str__(self):
        return '{} = {}'.format(self.lhs, self.rhs)

    def solve(self, **variables):
        # Get it in the form 0 = f(a, b, ...)
        equation = self.lhs - self.rhs

        free_variables = equation.free_symbols

        # Go through the equation and the variables provided, checking to
        # see which variables we weren't given
        not_given = set()
        for variable in free_variables:
            if variable.name not in variables:
                not_given.add(variable)

        if len(not_given) > 1:
            raise ValueError('Solver can only solve things if there is 1 unknown, '
                            'unknown variables: "{}"'.format(not_given))
        elif len(not_given) < 1:
            raise ValueError('No variables to solve for.')

        # Do the actual solving
        solution = solvers.solve(equation.subs(variables), *not_given, dict=True)
        return solution


def solve(eqn, **variables):
    # Get it in the form 0 = f(a, b, ...)
    equation = eqn.lhs - eqn.rhs

    free_variables = equation.free_symbols

    # Go through the equation and the variables provided, checking to
    # see which variables we weren't given
    not_given = set()
    for variable in free_variables:
        if variable.name not in variables:
            not_given.add(variable)

    if len(not_given) > 1:
        raise ValueError('Solver can only solve things if there is 1 unknown, '
                         'unknown variables: "{}"'.format(not_given))
    elif len(not_given) < 1:
        raise ValueError('No variables to solve for.')

    # Do the actual solving
    solution = solvers.solve(equation.subs(variables), *not_given, dict=True)
    return solution
