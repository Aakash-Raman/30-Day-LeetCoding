def numSquareSum(n): 
    squareSum = 0; 
    while(n): 
        squareSum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return squareSum; 
  
def isHappynumber(n): 
    slow = n; 
    fast = n; 
    while(True): 
        slow = numSquareSum(slow); 
        fast = numSquareSum(numSquareSum(fast)); 
        if(slow != fast): 
            continue; 
        else: 
            break; 
    return (slow == 1); 
     
class Solution:
    def isHappy(self, n: int) -> bool:
        if (isHappynumber(n)): 
            return True
        else: 
            return False
