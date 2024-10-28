class FizzBuzz:
    def execute(self, number):
        if number % 3 == 0:
            return "Fizz"
        
        if number % 5 == 0:
            return "Buzz"
        
        return str(number)
