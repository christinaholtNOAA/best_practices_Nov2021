'''
Pytests for common triangle utilities.

To run the tests, type the following:

    python -m pytest

'''
import math

import pytest

import solve_triangle_linted as solve_triangle

def test_pythagorean_thm():

    ''' Test PT solver under a variety of boundary conditions. '''


    arg_list = [
            {'input': {
                'hypotenuse': 5,
                'leg_a': None,
                'leg_b': 4,
                },
             'output': 3},
            {'input': {
                'hypotenuse': 5,
                'leg_a': 3,
                'leg_b': None,
                },
             'output': 4},
            {'input': {
                'hypotenuse': None,
                'leg_a': 3,
                'leg_b': 4,
                },
             'output': 5},
        ]
    for args in arg_list:
        answer = solve_triangle.apply_pythagorean_theorem(
            **args.get('input'))
        assert answer == args.get('output')

def test_apply_trig_functions():

    ''' Test Trig function solver under a variety of boundary
    conditions. '''

    answer = solve_triangle.apply_trig_functions(
            unknown='hypotenuse',
            opposite=3,
            theta=math.radians(45),
            )
    assert answer == pytest.approx(4.24264)

    answer = solve_triangle.apply_trig_functions(
            unknown='theta',
            adjacent=7,
            hypotenuse=12,
            )
    assert answer == 0.947969



