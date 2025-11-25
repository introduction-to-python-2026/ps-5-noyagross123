from string_utils import parse_chemical_reaction, count_atoms_in_reaction
from equation_utils import build_equations, my_solve
from math import gcd
from functools import reduce


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_list(lst):
    return reduce(lcm, lst, 1)


def balance_reaction(reaction):  # "Fe2O3 + H2 -> Fe + H2O"
    # 1. Parse reaction
    reaction = reaction.replace(" ", "")
    reactants, products = parse_chemical_reaction(reaction)

    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. Build equation system
    equations, coefficients = build_equations(reactant_atoms, product_atoms)

    # 3. Solve the linear system
    solution = my_solve(equations, coefficients)

    # מוסיפים "1" אחרון כפי שעשית בקוד המקורי
    solution = solution + [1]

    # 4. הפיכה למקדמים שלמים בלבד
    # נניח שהפתרון מכיל שברים מסוג Fraction
    denominators = [coef.denominator if hasattr(coef, "denominator") else 1
                    for coef in solution]

    lcm_val = lcm_list(denominators)

    integer_solution = [int(coef * lcm_val) for coef in solution]

    return integer_solution
