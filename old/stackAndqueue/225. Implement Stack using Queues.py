class MyStack(object):
#python 里面的队列是deque（）双向队列，如果只用队列的话，可以输入就直接输入，输出从队列1中
#往队列2弹出元素，直到队列1中只剩一个元素，将该元素输出，然后将2中的元素放回1.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.appendleft(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.popleft()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q
      