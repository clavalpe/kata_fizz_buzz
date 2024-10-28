from fizz_buzz import FizzBuzz


class TestFizzBuzz:
    def test_it_converts_1_to_1(self):
        assert "1" == FizzBuzz().execute(1)

    def test_it_converts_2_to_2(self):
        assert "2" == FizzBuzz().execute(2)

    def test_it_converts_3_to_fizz(self):
        assert "Fizz" == FizzBuzz().execute(3)

    def test_it_converts_5_to_buzz(self):
        assert "Buzz" == FizzBuzz().execute(5)

    def test_it_converts_15_to_fizz_buzz(self):
        assert "FizzBuzz" == FizzBuzz().execute(15)