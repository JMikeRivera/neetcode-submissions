class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        res = 0
        operators = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                nums.append(int(tokens[i]))
            elif tokens[i] in operators:
                if tokens[i] == "+":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    nums.append(num1 + num2)
                elif tokens[i] == "-":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    nums.append(num2 - num1)
                elif tokens[i] == "*":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    nums.append(num1 * num2)
                elif tokens[i] == "/":
                    num1 = nums.pop()
                    num2 = nums.pop()
                    nums.append(int(num2 / num1))
        
        return (nums[0])