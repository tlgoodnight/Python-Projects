class Protected1:
    def __init__(self):
        self._protectedVar=0

obj = Protected1()
obj._protectedVar = 47
print(obj._protectedVar)

class Private1:
    def __init__(self):
        self.__privateVar = 50

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Private1()
obj.getPrivate()
obj.setPrivate(32)
obj.getPrivate()
