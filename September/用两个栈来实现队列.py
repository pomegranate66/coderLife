class CQueue:

    def __init__(self):
        self.a ,self.b = [],[] 

    def appendTail(self, value: int) -> None:
        self.a.append(value)


    def deleteHead(self) -> int:
        if self.b:
            return self.b.pop()
        if not self.a : return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()