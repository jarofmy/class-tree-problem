## The Problem
Suppose we have the following fictitious series of classes where prerequisites
are dependencies:
 
Calculus 1 has no prerequisites

Calculus 2 has a prerequisite of Calculus 1

Calculus 3 has a prerequisite of Calculus 2

Linear Algebra has a prerequisite of Calculus 2

Discrete Math has a prerequisite of Calculus 2

Differential Equations has a prerequisite of Calculus 3

Advanced Machine Learning has prerequisites of Differential Equations, Linear Algebra, and Algorithm Analysis

Programming 1 has no prerequisites

Programming 2 has a prerequisite of Programming 1

Algorithm Analysis has prerequisites of Programming 2 and Discrete Math 
 
Further suppose we use the following abbreviations:
 
Calculus 1 = C1

Calculus 2 = C2

Calculus 3 = C3

Linear Algebra = LA

Discrete Math = DM

Differential Equations = DE

Advanced Machine Learning = AML

Programming 1 = P1

Programming 2 = P2

Algorithm Analysis = AA
 
We can now list the sets of dependencies. On the left hand side of the
equations below we have a course. On the right hand side we have the course's
corresponding set of dependencies (prerequisites).

``` 
  C1 = {}
  C2 = {C1}
  C3 = {C2}
  LA = {C2}
  DM = {C2}
  DE = {C3}
  AML = {DE, LA, AA}
  P1 = {}
  P2 = {P1}
  AA = {P2, DM}
 ```
 
Given the list of dependency sets we would like to produce a valid order in
which to take the classes. There may be numerous valid orderings, but our goal
shall be to identify and list only one.
 
For example, one valid ordering is:
`[C1, P1, P2, C2, DM, C3, DE, LA, AA, AML]`
 
Another valid ordering would be:

`[C1, P1, C2, P2, DM, C3, DE, LA, AA, AML]`
 
Either of the above alone, or any other valid ordering, would be sufficient as
a solution to our problem of finding a single valid ordering.
 
Let us now represent these same dependencies as a data structure that will
serve as input to a function.

 ```
  dependencies = {
    "C1": [],
    "C2": ["C1"],
    "C3": ["C2"],
    "LA": ["C2"],
    "DM": ["C2"],
    "DE": ["C3"],
    "AML": ["DE", "LA", "AA"],
    "P1": [],
    "P2": ["P1"],
    "AA": ["P2", "DM"]
  }
 ```

Your goal is to write a function with the following signature:
 
```
def find_ordering(dependencies): # Your code here
```
 
This function takes an object containing the dependencies and returns any
single valid ordering.
 
For example, using the object above:

```
print(find_ordering(dependencies))
['C1', 'P1', 'P2', 'C2', 'DM', 'C3', 'DE', 'LA', 'AA', 'AML']
```