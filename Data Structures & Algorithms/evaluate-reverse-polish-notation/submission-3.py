class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def safe_div(a: int, b: int) -> int:
            if b == 0:
                return 0  # Or handle as required by the platform / spec
            return int(a / b)
        operator = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': safe_div,
        }
        stack = []
        for token in tokens:
            if token in operator:
                a = stack.pop()
                b = stack.pop()
                stack.append(operator[token](b,a))
            else:
                stack.append(int(token))
            
        return stack[0] if stack else 0

        