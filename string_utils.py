def split_before_uppercases(formula):
    """
    פיצול לפני כל אות גדולה, כשהאות הגדולה נשארת בתחילת המקטע.
    דוגמאות:
      "NaCl"     -> ["Na", "Cl"]
      "C6H12O6B" -> ["C6", "H12", "O6", "B"]
      "water"    -> ["water"]
      ""         -> []
    """
    if not formula:
        return []

    parts = []
    current = formula[0]

    for ch in formula[1:]:
        # תחילת אטום חדש כאשר מופיעה אות גדולה
        if ch.isupper():
            parts.append(current)
            current = ch
        else:
            current += ch

    parts.append(current)
    return parts


def split_at_digit(formula):
    """
    פיצול במפגש הספרה הראשונה:
    מחזיר (prefix, count), לדוגמה:
      "H22"   -> ("H", 22)
      "NaCl"  -> ("NaCl", 1)
      "123"   -> ("", 123)
    """
    if not formula:
        return "", 1

    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])

    return formula, 1  # אין ספרות


def count_atoms_in_molecule(molecular_formula):
    """
    מקבלת נוסחה מולקולרית ומחזירה מילון של כמות האטומים.
