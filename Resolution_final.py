import re
import sympy as sp

def insert_multiplication_signs(expr):
    # Ajoute * entre un chiffre et une lettre (ex: 2x -> 2*x)
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
    # Ajoute * entre une lettre et une parenthèse ouvrante (ex: x(x+1) -> x*(x+1))
    expr = re.sub(r'([a-zA-Z])\(', r'\1*(', expr)
    # Ajoute * entre une parenthèse fermante et une lettre (ex: )(x+1) -> )*(x+1))
    expr = re.sub(r'\)([a-zA-Z])', r')*\1', expr)
    return expr

def parse_equation(equation):
    # Remplace le caractère ² par ^2
    equation = equation.replace('²', '^2')
    # Nettoyage et standardisation
    equation = equation.replace(' ', '').replace('**', '^')
    # Trouve le comparateur
    match = re.search(r'(<=|>=|=|<|>)', equation)
    if not match:
        raise ValueError("Aucun comparateur trouvé dans l'équation.")
    comp = match.group()
    left, right = equation.split(comp)
    expr = f"({left})-({right})"
    expr = insert_multiplication_signs(expr)
    expr = expr.replace('^', '**')
    # Détection automatique de la variable
    variables = sorted(list(set(re.findall(r'[a-zA-Z]', expr))))
    if not variables:
        raise ValueError("Aucune variable détectée.")
    var = sp.symbols(variables[0])
    poly = sp.sympify(expr)
    poly = sp.expand(poly)
    return poly, var, comp

def solve_any_degree(equation):
    poly, var, comp = parse_equation(equation)
    degree = sp.degree(poly, gen=var)
    if comp == '=':
        solutions = sp.solve(poly, var)
        return f"Solutions: {solutions}"
    else:
        # Inéquation
        if comp == '<':
            ineq = poly < 0
        elif comp == '<=':
            ineq = poly <= 0
        elif comp == '>':
            ineq = poly > 0
        elif comp == '>=':
            ineq = poly >= 0
        else:
            raise ValueError("Comparateur inconnu.")
        sol = sp.solve_univariate_inequality(ineq, var, relational=False)
        # Affiche R si la solution est tout l'ensemble des réels
        if sol == sp.Interval(-sp.oo, sp.oo):
            return "Ensemble solution : R"
        return f"Ensemble solution : {sol}"

if __name__ == "__main__":
    eq = input("Entrez une équation ou inéquation (ex: 2x²-3x+1>=0, x^3-2x=0, 5x-7<0) : ")
    print(solve_any_degree(eq))