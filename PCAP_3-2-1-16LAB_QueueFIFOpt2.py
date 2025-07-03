class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.qlist = []

    def put(self, elem):
        self.qlist.append(elem)
        
    def get(self):
        if len(self.qlist) > 0:
            val = self.qlist[0]
            del self.qlist[0]
            return val
        else:
            raise QueueError()

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        if len(self.qlist) == 0:
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
