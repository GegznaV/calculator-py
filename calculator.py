class Calculator:
    def __init__(self, initial_value=0.0) -> None:
        self.result = initial_value
        
    def add(self, value: float) -> None:
        self.result += value
        
    def subtract(self, value: float) -> None:
        self.result -= value
        
    def multiply_by(self, value: float) -> None:
        self.result *= value
        
    def divide_by(self, value: float) -> None:
        self.result /= value
        
    def exponentiate(self, value: float) -> None:
        self.result = self.result**value
        
    def take_n_root(self, n: float = 2) -> None:
        self.result = self.result**(1/n)
        
    def sqrt(self) -> None:
        self.result = self.take_n_root(n=2)
        
    def reset(self) -> None:
        self.result = 0.0
        
