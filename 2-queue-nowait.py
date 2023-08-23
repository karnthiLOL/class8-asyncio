from random import random
import asyncio
import time

# Coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to queue
        await queue.put(value)
    # send an akk done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queue):
    print(f'Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # checl for stop
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the share queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

#start the asyncio program
asyncio.run(main())


## Result
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class8-asyncio/2-queue-nowait.py
# Wed Aug 23 14:29:37 2023 Producer: Running
# Consumer: Running
# Wed Aug 23 14:29:37 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:37 2023 >got 0.2855830612019945
# Wed Aug 23 14:29:37 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:38 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:38 2023 >got 0.884712370743805
# Wed Aug 23 14:29:38 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:39 2023 >got 0.5074076823070248
# Wed Aug 23 14:29:39 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:39 2023 >got 0.6995469825699685
# Wed Aug 23 14:29:39 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:40 2023 >got 0.5242868311049493
# Wed Aug 23 14:29:40 2023 >got 0.020781257584502222
# Wed Aug 23 14:29:40 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:41 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:41 2023 >got 0.7776505052864103
# Wed Aug 23 14:29:41 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:42 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:42 2023 >got 0.811591145676133
# Wed Aug 23 14:29:42 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:43 2023 >got 0.9158441512580949
# Wed Aug 23 14:29:43 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:43 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:29:43 2023 Producer: Done
# Wed Aug 23 14:29:44 2023 >got 0.9909704111552431
# Wed Aug 23 14:29:44 2023 Consumer: Done