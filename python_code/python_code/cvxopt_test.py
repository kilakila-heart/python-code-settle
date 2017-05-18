from cvxopt import matrix, solvers
from cvxopt.modeling import op, dot, variable
import numpy as np


def solve_lp(a, b, c):
    """
    >>> a = matrix([[-5., 3., 1., 8., 1.],
    ...             [ 5., 5., 4., 6., 1.],
    ...             [-4., 6., 0., 5., 1.],
    ...             [-1.,-1.,-1.,-1., 0.],
    ...             [ 1., 1., 1., 1., 0.],
    ...             [-1., 0., 0., 0., 0.],
    ...             [ 0.,-1., 0., 0., 0.],
    ...             [ 0., 0.,-1., 0., 0.],
    ...             [ 0., 0., 0.,-1., 0.]])
    >>> b = matrix([0.,0.,0.,0.,1.])
    >>> c = matrix([0.,0.,0., 1.,-1.,0.,0.,0.,0.])
    >>> solve_lp(a, b, c)

    """
    variables = c.size[0]
    x = variable(variables, 'x')
    eq     =   (a*x == b)
    ineq   =   (x >= 0)
    lp = op(dot(c, x), [eq, ineq])
    lp.solve(solver='glpk')
    return (lp.objective.value(), x.value)
