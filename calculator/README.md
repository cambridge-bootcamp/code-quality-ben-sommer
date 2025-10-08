# Reverse Polish Notation calculator

The file `rpn_calculator.py` contains an example calculator app that demonstrates [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) calculations.

It has several methods that are used in the `main()` function to provide an interactive RPN calculator.

The code is very poorly written, with inconsistent type hint usage and very bad formatting.

You can check the code works, despite these issues. An example of a RPN calculation would be `6 7 *` (or `6 * 7` in the more usual infix notation), which should give `42`.


## Linting

Try using `pylint rpn_calculator.py` to find issues in the calculator app, and then fix them.

Review the code after getting `pylint` passing; does it look perfect to you? There is a trade-off for linting tools between being broadly useful, and being opinionated.
Most tools will focus on catching problematic behaviour, but still allow inconsistent coding styles.


## Type Hints

To ensure everything is typed, use `mypy --disallow-untyped-defs rpn_calculator.py`. 

See if you can understand the typing of the `add` function, and convince yourself that the type checker is correct to allow it to be used in `token_map`.


## Extensions

The `pylint` default checks are quite forgiving of code style.

There are other tools that can enforce stricter code styles, `flake8` and `ruff` (specifically `flake8 filename.py` and `ruff check filename.py`), that you could try.
Tools like `ruff format` can even automatically fix many simple style issues, to help keep code consistent and reduce the effort to read it across a large codebase.
