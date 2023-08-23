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
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item :
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

# entry point coroutine
async def main():
    # create the share queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all item to be processed
    await queue.join()

#start the asyncio program
asyncio.run(main())


## Result
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class8-asyncio/4-queue-task-done.py
# Wed Aug 23 14:35:28 2023 Consumer: Running
# Wed Aug 23 14:35:28 2023 Producer: Running
# Wed Aug 23 14:35:28 2023 > got 0.4883787524485994
# Wed Aug 23 14:35:29 2023 > got 0.08191629146140167
# Wed Aug 23 14:35:29 2023 > got 0.011565998726162041
# Wed Aug 23 14:35:29 2023 > got 0.7369873762069207
# Wed Aug 23 14:35:30 2023 > got 0.6351278436104207
# Wed Aug 23 14:35:30 2023 > got 0.3935909463185744
# Wed Aug 23 14:35:31 2023 > got 0.7132450175473164
# Wed Aug 23 14:35:32 2023 > got 0.8919511287928448
# Wed Aug 23 14:35:32 2023 Producer: Done
# Wed Aug 23 14:35:32 2023 > got 0.2799060614639729
# Wed Aug 23 14:35:33 2023 > got 0.13619265853765472