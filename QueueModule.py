#   Created by Roshan Jayswal on 31/05/2020.
#   Copyright © 2021. All rights reserved.

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())
