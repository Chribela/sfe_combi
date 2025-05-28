
class Solution: 
  def summation(self, nums :list[int])->list[int]: 

      for i in range(10):
          number = int(input(f"Enter number {i+1} (consecutive number): "))
          nums.append(number)

      #Compute the sum of all the numbers
      sum_all_numbers = sum(nums)
      print(f"\nSum of all numbers: {sum_all_numbers}")
    
sol= Solution();

sol.summation([])