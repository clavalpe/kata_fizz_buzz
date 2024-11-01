class FizzBuzz:
    def execute(self, number) -> str:
        if self._is_fizz(number) and self._is_buzz(number):
            return "FizzBuzz"

        if self._is_fizz(number):
            return "Fizz"
        
        if self._is_buzz(number):
            return "Buzz"
        
        return str(number)

    def _is_fizz(self, number) -> bool:
        return number % 3 == 0
    
    def _is_buzz(self, number) -> bool:
        return number % 5 == 0