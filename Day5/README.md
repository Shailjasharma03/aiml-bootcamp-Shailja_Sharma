# student_utils

Small, typed helpers for analysing a student's marks: average, highest, lowest,
pass rate and a one-call summary. Refactored from my Day 2 notebook.

## Functions

- `average(marks)`: the mean mark, or `None` for an empty list
- `highest(marks)` and `lowest(marks)`: the top and bottom mark, or `None` for an empty list
- `pass_rate(marks, passing=40)`: the percentage of marks at or above the pass mark (a mark equal to the pass mark passes), or 0.0 for an empty list
- `summarise(marks, passing=40)`: a dict with `count`, `average`, `highest`, `lowest` and `pass_rate`

## Example

    from student_utils import summarise

    print(summarise([88, 92, 79, 40]))
    # {'count': 4, 'average': 74.75, 'highest': 92, 'lowest': 40, 'pass_rate': 100.0}

## Setup (Python 3.10 or newer)

From the repository root (on Mac or Linux, activate with `source .venv/bin/activate`):

    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    pre-commit install

## Run the tests

    cd Day5
    pytest -v

## Check code quality

    black --check .
    ruff check . --extend-exclude "*.ipynb"
    mypy .
