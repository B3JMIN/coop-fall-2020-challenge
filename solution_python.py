class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.time = 0
        self.history = []
        self.operand = []

    def add(self, num: int):
        self.value += num
        self.history.append(num)
        self.operand.append("1")
        self.time += 1

    def subtract(self, num: int):
        self.value -= num
        self.history.append(num)
        self.operand.append("-1")
        self.time += 1

    def undo(self):
        if self.operand[-1]== "1":
            self.value -= self.history[-1]

        else:
            self.value += self.history[-1]
        self.time -= 1
        # self.history.pop(-1)
        # self.operand.pop(-1)

    def redo(self):
        if len(self.history) > self.time :
            if self.operand[-1] == "1":
                self.value += self.history[-1]
            else:
                self.value -= self.history[-1]
            self.time += 1
        else:
            print("no redo avaible")

    def bulk_undo(self, steps: int):
        step = steps
        while step > 0:
            pos = step * -1
            if self.operand[pos] == "1":
                self.value -= self.history[pos]
            else:
                self.value += self.history[pos]
            self.time += 1

    def bulk_redo(self, steps: int):
        step = steps
        while step > 0:
            pos = step * -1
            if self.operand[pos] == "1":
                self.value += self.history[pos]
            else:
                self.value -= self.history[pos]
            self.time += 1
