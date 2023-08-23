from random import random
import asyncio
import time

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
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
# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        try:
            #retrive the get() awaitable
            get_await = queue.get()
            # awair the awaitable with a timeout
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: give up waiting...')
            continue
        # checl for stop
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print('Consumer: Done')

# entry point coroutine
async def main():
    # create the share queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

#start the asyncio program
asyncio.run(main())


## Result
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class8-asyncio/3-queue-waitfor.py
# Producer: Running
# Wed Aug 23 14:30:05 2023 Consumer: Running
# Wed Aug 23 14:30:05 2023 Consumer: give up waiting...
# Wed Aug 23 14:30:06 2023 >got 0.6818989298131369
# Wed Aug 23 14:30:06 2023 >got 0.17261114451082227
# Wed Aug 23 14:30:06 2023 >got 0.31017095702421926
# Wed Aug 23 14:30:07 2023 Consumer: give up waiting...
# Wed Aug 23 14:30:07 2023 >got 0.9489325808596548
# Wed Aug 23 14:30:07 2023 >got 0.04238164766312502
# Wed Aug 23 14:30:07 2023 >got 0.1674170826207474
# Wed Aug 23 14:30:08 2023 Consumer: give up waiting...
# Wed Aug 23 14:30:08 2023 >got 0.586473014936612
# Wed Aug 23 14:30:08 2023 >got 0.4645359680718346
# Wed Aug 23 14:30:08 2023 >got 0.16069069162567018
# Wed Aug 23 14:30:09 2023 Producer: Done
# Wed Aug 23 14:30:09 2023 >got 0.21798982114385512
# Consumer: Done