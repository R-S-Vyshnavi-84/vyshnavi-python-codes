'''
q=[]*4
q.append(10)
print(q)
q.append(20)
print(q)
q.append(30)
print(q)
q.append(40)
print(q)
q.append(50)
print(q)
i=0
q.pop(i)
print(q)
i=0
q.pop(i)
print(q)
i=0
q.pop(i)
print(q)
'''

from collections import deque
lq=deque(maxlen=4)
print(lq)
lq.append(10)
print(lq)
lq.append(20)
print(lq)
lq.append(30)
print(lq)
lq.append(40)
print(lq)
lq.append(50)
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)






