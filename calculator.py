class Calculator:
    """Class which works as a simple calculator.

    The class performs basic math operations with the value of attribute
    `.result` (its `initial_value` is 0) saves the result as a new value 
    of `.result`.

    To reset `.result` value to 0, use `.reset()` method.
    """

    def __init__(self, initial_value: float =0.0) -> None:
        self.result = initial_value

    def add(self, value: float) -> None:
        """Addition

        Add `value` to `.result` and save the result as `.result`.

        ```
        .result = .result + value
        ```

        Parameters
        ----------
        value: float :
            The value that is added to `.result`.


        Returns
        -------
        Noting. Updates the value of attribute `.result` with the result
        of performed mathematical operation.
        """
        self.result += value

    def subtract(self, value: float) -> None:
        """Subtraction

        From `.result` subtract `value` and save the result as `.result`.
        ```
        .result = .result - value
        ```

        Parameters
        ----------
        value: float :
            The value that is subtracted from `.result`.

        Returns
        -------
        Noting. Updates the value of attribute `.result` with the result
        of performed mathematical operation.

        """
        self.result -= value

    def multiply_by(self, value: float) -> None:
        """Scalar multiplication

        Multiply `.result` by `value` and save the result as `.result`.

        Parameters
        ----------
        value: float :
            The value that `.result` is multipied by.
        ```
        .result = .result * value
        ```

        Returns
        -------
        Noting. Updates the value of attribute `.result` with the result
        of performed mathematical operation.

        """
        self.result *= value

    def divide_by(self, value: float) -> None:
        """Division

        Divide  `.result` by `value` and save the result as `.result`.
        ```
        .result = .result / value
        ```


        Parameters
        ----------
        value: float :
            Divisor.

        Returns
        -------
        Noting. Updates the value of attribute `.result` with the result
        of performed mathematical operation.

        """
        self.result /= value

    def exponentiate(self, n: float) -> None:
        """Exponentiation

        Exponentiote `.result` by `n` (`.result^n`, or in Python `.result**n`) 
        and save the result as `.result`.
        ```
        .result = .result ** n
        ```


        Parameters
        ----------
        n: float :
            exponent


        Returns
        -------
        Noting. Updates the value of attribute `.result` with the result
        of performed mathematical operation.

        """
        self.result = self.result**n

    def take_n_root(self, n: float = 2) -> None:
        """Take n-th root

        Take n-th root of atribute.

        Parameters
        ----------
        n: float :
             Degree of the root.
             (Default value = 2)

        Returns
        -------
        Noting. Updates the value of attribute `.result` with the result
        of performed mathematical operation.

        """
        self.result = self.result**(1/n)

    def sqrt(self) -> None:
        """Square root

        Takes a square root of attribute `.result` and updates its value with
        the result of mathematical operation. It is a convenience method
        wrapped arround `.take_n_root()` with value `n=2`.
        """
        self.take_n_root(n=2)

    def reset(self) -> None:
        """Reset the value of attribute `.result` to 0"""
        self.result = 0.0
