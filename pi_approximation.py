

import math
import sys
import random

def main(argv):
    is_verbose = True if '-v' in argv else False

    num_points = get_input_as_int("How many points should be generated? ")

    generate_pi(num_points, is_verbose)

def get_input_as_int(message: str, error_message: str = "Not an integer, try again") -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            print(error_message)
            continue

def generate_pi(num_points: int, is_verbose: bool) -> float:
    if is_verbose: print("Generating points...")

    num_points_in_circle = 0
    for _ in range(num_points):
        x,y = generate_point()
        in_circle = is_in_circle(x,y)

        if in_circle:
            num_points_in_circle += 1
        
        if is_verbose: print(f"Point ({x},{y}) generated! It is {'' if in_circle else 'NOT '}in the circle.")


def generate_point():
    return (random.uniform(-1,1), random.uniform(-1,1))

def is_in_circle(x, y):
    return math.sqrt(x*x + y*y) > 1

if __name__ == '__main__':
    main(sys.argv)