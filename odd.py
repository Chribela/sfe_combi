class OddNumbers:
    def compute_odds(self, nums: list[int]) -> list[int]:
        odd_numbers = [num for num in nums if num % 2 != 0]
        sum_odd_numbers = sum(odd_numbers)
        print(f"Sum of odd numbers : {sum_odd_numbers}")
        