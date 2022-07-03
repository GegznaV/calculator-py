# Simple Calculator in Python

> Python class for basic math operations.

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]

`calculator` is a Python class that performs simple mathematical calculations. 


Attributes:

- `.result` -- contains a numeric value of current result.
   Initial default value is 0.


Mehods:

- `.add()`, `.subtract()`, `.divide_by()`, `.multiply_by()`, `.exponentiate()`, `.take_n_root()` -- These functions perform indicated mathematical operations on `.result` with `value` indicated in appropriate function and saves the result as , `.result`.
- `.reset()` -- resets the `.result` to 0.


## Installation

```sh
pip install calculator
```


## Usage

Simple calculations

```python
>>> from calculator import Calculator
>>> calculator = Calculator()
>>> calculator.set_value(35)
>>> calculator.result
35
>>> caltulator.reset()
>>> calculator.result
0
>>> calculator.subtract(10)
>>> calculator.result
-10
>>> calculator.add(46).take_n_root(n=2)
>>> calculator.result
6
>>> caltulator.reset()
>>> calculator.result
0
```

`caltulator.reset()` sets value of `.result` to 0.


## Development setup

```sh
$ python -m venv env-calculator
$ . env-calculator/bin/activate
$ make deps
$ tox
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/???
[pypi-url]: https://pypi.org/project/???/

[build-image]: https://github.com/GegznaV/calculator-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/GegznaV/calculator-py/actions/workflows/build.yml

[coverage-image]: https://codecov.io/gh/GegznaV/calculator-py/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/GegznaV/calculator-py

