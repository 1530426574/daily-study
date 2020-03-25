import itertools
import heapq

pq = []
entry_finder = {}
REMOVED = '<removed-task>'
counter = itertools.count()
print(1, counter, type(counter))
print(2, next(counter))
print(3, next(counter))
print(4, next(counter))


# 关键在哪呢，每个任务映射一个优先级，优先级放在堆里，自动会排成序
def add_task(task, priority=0):
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def pop_task():
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('HAHH')
