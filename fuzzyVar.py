from typing import Tuple, Dict, List, Callable, NoReturn

class FuzzyVar:
    # X, T, U, M
    # X = base_value -> accessed using its index
    # T = values -> list of different linguistic values for the variable
    # U = universe -> meaning range -> using [0.,1.]
    # M = meaning -> meaning of var with base_value x, for value t in T
    def __init__(self, values: List[float], meaning:Dict[str, Callable[[float], float]]) -> NoReturn:
        self.values:List[float] = values
        self.meaning:Dict[str, Callable[[float], float]] = meaning
    
    def get_meaning(self, value:float, base_value:float) -> float:
        meaning = self.meaning[value](base_value)
        if meaning < 0.:
            return 0.
        elif meaning > 1.:
            return 1.
        else:
            return meaning