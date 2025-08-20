class Calculator:
    #sum()
    def sum(self, a, b):
        return a + b
    # sub()
    def sub(self, a, b):

        return a - b
    # divide()
    def div(self, a, b):
        if (b == 0):
            return "Error: Do not allowed to divide by 0"
        return a / b
    # multiplay()
    def multiplay(self, a, b):

        return a * b