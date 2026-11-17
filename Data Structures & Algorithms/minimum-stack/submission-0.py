class MinStack:

    def __init__(self):
        self.__stack: List = []
        self.__min_tracker = []

    def push(self, val: int) -> None:
        self.__stack.append(val)
        if not self.__min_tracker or val <= self.__min_tracker[-1]:
            self.__min_tracker.append(val)
        
    def pop(self) -> None:
        popped = self.__stack.pop()
        if popped == self.__min_tracker[-1]:
            self.__min_tracker.pop()

    def top(self) -> int:
        return self.__stack[-1]
        

    def getMin(self) -> int:
        return self.__min_tracker[-1]
        
