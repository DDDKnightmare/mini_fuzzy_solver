from typing import List, Callable, Any, Tuple

'''
examples of rules: 
- from left to right
- no precedence

rule:A and B or C
variables: [A,B,C]
operators: [and,or]

rule: A or B and C
variables: [A,[B,C]]
operators: [or, and]

rule: A and B or (B and C)
variables: [A,B,[B,C]]
operators: [and,or,and]

rule: A and (B or C and A) or C and D
variables: [A,[B,[C,A]],[C,D]]
operators: [and, or, and, or, and]

'''

def compute_rule(variables:List[any], operators:List[Callable[[float, float], float]]) -> float:
    val = compute_parenthesis(variables, operators, 0)[1]
    # print(len(operators), op_idx)
    return val

def compute_parenthesis(variables:List[Any], operators:List[Callable[[float, float], float]], curr_idx: int) -> Tuple[int, float]:
    tmp = variables[0]
    if tmp is list:
        curr_idx, tmp = compute_parenthesis(tmp, operators, curr_idx)
    for var in variables[1:]:
        if type(var) is list:
            tmp_idx = curr_idx
            curr_idx += 1
            curr_idx, aux = compute_parenthesis(var, operators, curr_idx)
        else:
            aux = var
            tmp_idx = None
        if tmp_idx is not None:
            tmp = operators[tmp_idx](tmp, aux)
            tmp_idx = None
        else:
            tmp = operators[curr_idx](tmp, aux)
            curr_idx += 1
    return curr_idx, tmp