# Wordle

The file `wordle.py` contains a command-line representation of Wordle.
You will need to `cd` into this directory to run the commands below.

Try reading the code and running it to see how it works: `python wordle.py`.


## Linting

Linters can be used to find potential bugs and to keep code "clean". Try using `pylint wordle.py` to find issues in the code, and then fix them.

If you don't understand the meaning of the warnings and messages, searching the web and/or using a chatbot can help!


## Type Hints

Type hints are an improved form of documentation for code that, unlike docstrings and comments, cannot go out of date if they are regularly checked.
They make refactoring code safer, and help highlight potential bugs before the code is run.

mypy is designed to allow incremental type addition; un-typed methods/variables will be ingored.
To ensure everything is typed, use `mypy --disallow-untyped-defs wordle.py`.

Try and add the required type annotations by hand to start with. Afterwards, you could try asking a chatbot and comparing the generated annotations to your annotations.
Notice how in many places `mypy` can _infer_ the types without needing a specific annotation, only a few annotations allow coverage of the whole file.
