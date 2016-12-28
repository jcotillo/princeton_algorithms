from stack_with_array import Stack

# Implementation of Dijkstra's two-stack algorithm, which
# utilizes stacks to compute arithmetic expressions.
# Only supports addition and multiplication in this example.
class Evaluate:
    def __init__(self, string):
        self.numbers = Stack()
        self.operators = Stack()
        self.operation = string

    def result(self):
        for i in range(len(self.operation)):
            item = self.operation[i]
            if item == "(":
                pass
            elif item == "+":
                self.operators.push(item)
            elif item == "*":
                self.operators.push(item)
            elif item == ")":
                op = self.operators.pop()
                if op == "+":
                    result = int(self.numbers.pop()) + int(self.numbers.pop())
                elif op == "*":
                    result = int(self.numbers.pop()) * int(self.numbers.pop())
                self.numbers.push(result)
            else:
                self.numbers.push(item)

        return int(self.numbers.pop())

evaluator = Evaluate("(1+(2*6))")
print evaluator.result()
