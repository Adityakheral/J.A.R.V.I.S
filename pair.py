class priorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority
class priorityQueue:
    def __init__(self):
        self.pq = []
    def getSize(self):
        return len(self.pq)
    def isEmpty(self):
        return self.getSize()==0
    def getMin():
        if self.isEmpty():
            return None 
        return self.pq[0].value
    def __parcolateUp(self):
        childIndex = self.getsize()-1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            if self.pq[childIndex].priority < self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex] = self.pq[parentIndex],self.pq[childIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,value,priority):
        pqNode = priorityQueueNode(value,priority) 
        self.pq.append(pqNode)
        self.__percolateUp()
    def __percolateDown(self):
        parentIndex = 0 
        leftchildIndex = 2*parentIndex+1
        rightchildIndex = 2*parentIndex +2
        while leftchildIndex < self.getSize():
            minIndex = parentIndex
            if (self.pq [minIndex .priorty] > self.pq[leftchildIndex].priority):
                minIndex = leftchildIndex
            if (rightchildIndex < self.getSize() and  self.pq[minIndex].priority > self.pq[rightchildIndex].priority):
                minIndex = rightchildIndex
            if minIndex != parentIndex:
                self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
                parentIndex = minIndex
                leftchildIndex = 2*parentIndex+1
                rightchildIndex = 2 *parentIndex+2               
        else:
            break
    def removeMin(self):
        if self.isEmpty():
            return None
        ele = self.pq[0]
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele.value
        
        
pp = priorityQueue()  
pq.insert("A",10)
pq.insert("C",5)
pq.insert("B",19)
pq.insert("D",4)
for i in range(4):
    print(pq.removedMin())
  