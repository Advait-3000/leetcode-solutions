class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0
        queue = {s}
        while queue:
            valid_strings = [string for string in queue if isValid(string)]
            if valid_strings:return valid_strings
            next_queue=set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':next_queue.add(string[:i] + string[i+1:])
            queue=next_queue
        return [""]