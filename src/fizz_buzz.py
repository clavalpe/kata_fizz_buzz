class FizzBuzz:
    def execute(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"

        if self._is_fizz(number):
            return "Fizz"
        
        if number % 5 == 0:
            return "Buzz"
        
        return str(number)

    def _is_fizz(self, number):
        return number % 3 == 0