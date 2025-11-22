def split_before_each_uppercases(formula):
    split_formula = []
    start = 0 
    for end in range(1, len(formula)):
        if formula[end].isupper():
            substring = formula[start:end]
            if substring:
                split_formula.append(substring)
            start = end
    if formula:
        split_formula.append(formula[start:])
    return split_formula

def split_at_first_digit(formula):
    digit_location = -1 
    for i in range(1, len(formula)):
        if formula[i].isdigit():
            digit_location = i
            break
    if digit_location == -1:
        return formula, 1
    else:
        prefix = formula[:digit_location]
        numeric_part_str = formula[digit_location:]
        numeric_part_int = int(numeric_part_str)
        return prefix, numeric_part_int

def count_atoms_in_molecule(molecular_formula):
    atoms_count_dict = {} 
    for atom in split_before_each_uppercases(molecular_formula):
        atom_name, atom_count = split_at_first_digit(atom)
        atoms_count_dict[atom_name] = atoms_count_dict.get(atom_name, 0) + atom_count
    return atoms_count_dict

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
