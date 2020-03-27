## The Problem

Solution method, `find_ordering(dependencies)`, is included in `solution.py`

This function takes an object containing the dependencies and returns any
single valid ordering as an array.

To run:

```
python driver.py
```

Solution was written under the assumption of 
"small inputs, no more than 10 items", and does 
not account for case sensitivity. The solution also 
assumes that there will always be at least one course 
with no dependencies (i.e. C1 = []).