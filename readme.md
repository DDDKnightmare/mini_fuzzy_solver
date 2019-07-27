
# Mini Fuzzy Solver

This package implements a simple normalized fuzzy solver

## Classes

---

### FuzzyVar

- Retains info about the fuzzy variables
  - List of linguistic values
  - Meaning function for each linguistic value

---

### Operators

- Define the operators and parameters used in each operator(minimum, maximum, union, intersect, etc)

### How to use

1. Define your fuzzy variables

   __a)__ Base variables
   __b)__ Linguistic values
   __c)__ Meaning functions

2. Decide on wich operators to use for each operator(and, or, union, intersection, etc) in your logic

3. Use __fuzzyRule.py__ computeRules function

---

### How to define rules

The rules are executed from left to right.
> A and B or C -> [ [A, B, C], [and, or] ]
>
> A or B and C -> [ [ [A, B], C], [or, and] ]
>
> A and B or C and D -> [ [ [A, B], [C, D]], [and, or, and] ]
>
> A and (B or C) -> [ [A, [B, C] ], [and, or]]
>
> A and (B or C or D) and D -> [ [A, [B, C, D], D], [and, or, or, and] ]
>

---

### Definition Example

```python
BASE_VARIABLES = List[float]
MEANING = List[Dict[str,float]]
FUZZY_VARS = List[FuzzyVar]
FUZZY_RULES = List[Tuple[List[Any '''float or list'''], List[Callable[[float,float], float]]]]
```
