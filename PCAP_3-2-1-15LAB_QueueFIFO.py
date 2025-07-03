class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__qlist = []

    def put(self, elem):
        self.__qlist.append(elem)
        
    def get(self):
        if len(self.__qlist) > 0:
            val = self.__qlist[0]
            del self.__qlist[0]
            return val
        else:
            raise QueueError()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
