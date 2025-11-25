from string_utils import parse_chemical_reaction, count_atoms_in_reaction
from equation_utils import build_equations, my_solve

def balance_reaction(reaction):
    """
    מאזנת תגובה כימית ומחזירה רשימת מקדמים.
    לדוגמה: "Fe2O3 + H2 -> Fe + H2O"
    """
    
    # 1. Parse reaction
    reactants, products = parse_chemical_reaction(reaction)

    reactant_atoms = count_atoms_in_reaction(reactants)
    product_atoms = count_atoms_in_reaction(products)

    # 2. Build symbolic equations
    equations, coeff_vars = build_equations(reactant_atoms, product_atoms)

    # 3. Solve the equations
    solved = my_solve(equations, coeff_vars)

    if solved is None:
        raise ValueError("Could not solve the system (reaction might be invalid).")

    # 4. Add final product coefficient = 1 (as enforced in build_equations)
    coefficients = solved + [1]

    return coefficients
