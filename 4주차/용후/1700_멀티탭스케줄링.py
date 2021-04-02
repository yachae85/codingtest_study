import collections
import heapq

hole, n = map(int, input().split())
devices = list(map(int, input().split()))
d = collections.defaultdict(collections.deque)
plugged = collections.defaultdict(int)

heap = []
MAX = 999
for i, dev in enumerate(devices):
    d[dev].append(i)
for queue in d.values():
    if queue:
        queue.popleft()

result = 0
space = hole
for dev in devices:
    # unplug
    if space == 0 and plugged[dev] == 0:
        while True:
            up = heapq.heappop(heap)
            if plugged[up[1]] == 1:
                plugged[up[1]] = 0
                result += 1
                space += 1
                break

    # plug
    if plugged[dev] == 0:
        plugged[dev] = 1
        space -= 1

    if not d[dev]:  # 더 쓸일 없는것
        heapq.heappush(heap, [-MAX, dev])
    else:
        next = d[dev].popleft()
        heapq.heappush(heap, [-next, dev])

print(result)
