# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

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
        #print(f'{time.ctime()} Producer: put {value}')
    # send an akk done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
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
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class8-asyncio/1-queue.py
# Wed Aug 23 14:29:11 2023 Producer: Running
# Wed Aug 23 14:29:11 2023 Consumer: Running
# Wed Aug 23 14:29:12 2023 >got 0.8288273415261124
# Wed Aug 23 14:29:13 2023 >got 0.7196383466535774
# Wed Aug 23 14:29:13 2023 >got 0.04694743642498034
# Wed Aug 23 14:29:13 2023 >got 0.006067979532255796
# Wed Aug 23 14:29:13 2023 >got 0.34877000976508044
# Wed Aug 23 14:29:14 2023 >got 0.5098964703968981
# Wed Aug 23 14:29:15 2023 >got 0.8440378851272796
# Wed Aug 23 14:29:15 2023 >got 0.9065104574595605
# Wed Aug 23 14:29:16 2023 >got 0.4178169601026551
# Wed Aug 23 14:29:17 2023 Producer: Done
# Wed Aug 23 14:29:17 2023 >got 0.9227940345184535
# Wed Aug 23 14:29:17 2023 Consumer: Done