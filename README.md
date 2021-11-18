# NOAA GSL Best Practices Practical Session Repository
This repository is meant to facility code reviews of examples provided
by Practical Session participants of the Nov 2021 Best Practices
Workshop.

# Warning
Code contained within this repository is not meant for use as a robust
tool. It is meant only for demonstration purposes.

# Requirements
This code is python-based. Exercises for the learning module require:

- python 3.6+
- pylint
- pytest

# Hands-on session.
As a group, we did some live commenting on the code proposed in PR #2
and PR #3. Check out the comments and changes made in each of those.

The final product now lives in the main branch.

The code is **not** production-worthy code. Feel free to open
additional Pull Requests to build it out to what it should be. Those
additions can certainly be used as future learning examples.


# Existing code
The code here is meant to provide a very basic example of how to begin
making your code modular, linting with pylint, and writing test cases
with pytest.

## Pylint
Run the pylint tool:

```
pylint solve_triangle.py
```

## Pytest
From the top level of the repository:

```
python -m pytest
```
