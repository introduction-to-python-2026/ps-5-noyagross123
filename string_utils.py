def split_before_uppercases(formula):
    """
    פיצול לפני כל אות גדולה, כשהאות הגדולה נשארת בתחילת המקטע.
    דוגמאות:
      "NaCl"     -> ["Na", "Cl"]
      "C6H12O6B" -> ["C6", "H12", "O6", "B"]
      "water"    -> ["water"]
      ""         -> []
    """
    if formula == "":
        return []

    parts = []
    current = ""

    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch

    if current:
        parts.append(current)
    return parts


def split_at_digit(formula):
    """
    פיצול במפגש הספרה הראשונה:
    מחזיר (prefix, count) כאשר:
      - prefix: החלק לפני הספרה הראשונה (יכול להיות "" אם מתחיל בספרה)
      - count: כל רצף הספרות מהספרה הראשונה ועד הסוף כ-int
    אם אין ספרות כלל — מחזיר (formula, 1)
    """
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1


def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    counts = {}

    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        counts[atom_name] = counts.get(atom_name, 0) + atom_count

    return counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation string and returns reactants and products.
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")


def count_atoms_in_reaction(molecules_list):
    """Takes a list of formulas and returns a list of atom-count dictionaries."""
    return [count_atoms_in_molecule(molecule) for molecule in molecules_list]
