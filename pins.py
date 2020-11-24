'''
Given a set of pins with attributes (pin id, height), write a function that takes the argument 'k'
(determining the number of columns) and inserts the pins such that every pin goes into a column with least consumed height.
If there is a tie then insert into the left most column. (What would be the best way to solve this? I used a priority queue)
'''


from collections import defaultdict
from random import randint

class Pins:

    def __init__(self, num_queues):
        self.queue = defaultdict(list)
        self.queue_length = defaultdict()

        for queue_num in range(1, num_queues+1):
            self.queue[queue_num] = []
            self.queue_length[queue_num] = 0

    def additem(self, id, height):
        sorted_lengths =  sorted(self.queue_length.items(), key=lambda x: (x[1],x[0]))
        self.queue[sorted_lengths[0][0]].append(id)
        self.queue_length[sorted_lengths[0][0]] += height
        print(self.queue)
        print(self.queue_length)

    def printQueues(self):
        print(self.queue)



p = Pins(2)
p.additem('A', 3)
p.additem('B', 5)
p.additem('C', 1)
p.printQueues()
