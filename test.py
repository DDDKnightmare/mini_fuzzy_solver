from fuzzyVar import FuzzyVar
from math import pi, sin, cos
from typing import Dict, List, Tuple, Any, Callable, NoReturn
from fuzzyRule import compute_rule 
from operators import Operators



# type definitions
BASE_VALUES = List[float] # variable base values 
MEANING = List[Dict[str, float]] # variable meaning values
FUZZY_VARS = List[FuzzyVar] # FuzzyVarObjects
FUZZY_RULES = List[Tuple[List[Any],List[Callable[[float, float], float]]]] # list [([var1,[var2_1,var2_2], var3], [op1_2, op2, op2_3])]
VAR_DICT = Dict[str,int] # dictionary of fuzzy variable names to meaning/fuzzyVar/baseValue index
OP = Operators

VAR_DICT = {
    "A": 0.,
    "B": 1.
}        

BASE_VALUES = [4,56]

MEANING = [
    {
        "low":0.,
        "high":0.
    },{
        "none":0.,
        "some":0.,
        "every":0.
    }
]

FUZZY_VARS = [
    FuzzyVar(["low", "high"], {
        "low": lambda x: 20 - x**3/2, 
        "high": lambda x: x**3/5. 
        }
    ),
    FuzzyVar(["none", "some", "every"], {
        "none": lambda x: 1. if x <= 0. else 0.,
        "some": lambda x: cos(x * pi) * sin(x * pi),
        "every": lambda x: 1. if x == 1. else 0.
    })
]

OP = Operators(0.5,0.5,0.5)

def calculate_base_meaning(meaning_list:List[Dict[str,float]]) -> NoReturn:
    for idx, var in enumerate(FUZZY_VARS):
        for name in var.values:
            meaning_list[idx][name] = var.get_meaning(name, BASE_VALUES[idx])

calculate_base_meaning(MEANING)
# print(MEANING)

A = VAR_DICT["A"]
B = VAR_DICT["B"]

FUZZY_RULES = [
    ([A,B,[B,A]], [OP.bounded_difference, OP.bounded_sum, OP.drastic_product]),
    ([A,B,[B,A]], [OP.drastic_sum, OP.dubois_prade_intersection, OP.einstein_product]),
    ([A,B,[B,A]], [OP.einstein_sum, OP.hamacher_product, OP.hamacher_sum]),
    ([A,B,[B,A]], [OP.hamacher_union, OP.maximum, OP.minimum]),
    ([A,B,[B,A]], [OP.union, OP.yaeger_intersection, OP.yaeger_union])
]

for x, y in FUZZY_RULES:
    # print(x, y)
    compute_rule(x, y)