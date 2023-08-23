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
    print(f'{time.ctime()} Producer d: Done')

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
    # all done
    print(f'{Ptime.ctime} Consumer: Done')

# entry point coroutine
async def main():
    # create the share queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for all item to be processed
    await queue.join()

#start the asyncio program
asyncio.run(main())


##  Reslut
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class8-asyncio/5-queue-limit.py
# Wed Aug 23 14:39:55 2023 Consumer: Running
# Wed Aug 23 14:39:55 2023 Producer: Running
# Wed Aug 23 14:39:55 2023 Producer: Running
# Wed Aug 23 14:39:55 2023 Producer: Running
# Wed Aug 23 14:39:55 2023 Producer: Running
# Wed Aug 23 14:39:55 2023 Producer: Running
# Wed Aug 23 14:39:56 2023 > got 0.1742085202643927
# Wed Aug 23 14:39:56 2023 > got 0.2527230159484215
# Wed Aug 23 14:39:56 2023 > got 0.3187700539991032
# Wed Aug 23 14:39:56 2023 > got 0.39049533549903925
# Wed Aug 23 14:39:57 2023 > got 0.4489225782373254
# Wed Aug 23 14:39:57 2023 > got 0.6802130936088394
# Wed Aug 23 14:39:58 2023 > got 0.14128181327401523
# Wed Aug 23 14:39:58 2023 > got 0.29022023601416314
# Wed Aug 23 14:39:58 2023 > got 0.21918037208487273
# Wed Aug 23 14:39:59 2023 > got 0.2808412442987369
# Wed Aug 23 14:39:59 2023 > got 0.05561932441764894
# Wed Aug 23 14:39:59 2023 > got 0.8089473741272057
# Wed Aug 23 14:40:00 2023 > got 0.060898057248565896
# Wed Aug 23 14:40:00 2023 > got 0.030707168523835815
# Wed Aug 23 14:40:00 2023 > got 0.04229017942620583
# Wed Aug 23 14:40:00 2023 > got 0.1533485565871916
# Wed Aug 23 14:40:00 2023 > got 0.5075010829955783
# Wed Aug 23 14:40:01 2023 > got 0.8161982841154948
# Wed Aug 23 14:40:01 2023 > got 0.4949078763944178
# Wed Aug 23 14:40:02 2023 > got 0.21399599654740264
# Wed Aug 23 14:40:02 2023 > got 0.3219985001607396
# Wed Aug 23 14:40:02 2023 > got 0.3917617736159007
# Wed Aug 23 14:40:03 2023 > got 0.3585129960961595
# Wed Aug 23 14:40:03 2023 > got 0.7626690448854031
# Wed Aug 23 14:40:04 2023 > got 0.1229161339220366
# Wed Aug 23 14:40:04 2023 > got 0.6629110866156528
# Wed Aug 23 14:40:05 2023 > got 0.5097033070695506
# Wed Aug 23 14:40:05 2023 > got 0.5152273613755871
# Wed Aug 23 14:40:06 2023 > got 0.8173179986433833
# Wed Aug 23 14:40:07 2023 > got 0.48891095909631477
# Wed Aug 23 14:40:07 2023 > got 0.635484982575746
# Wed Aug 23 14:40:08 2023 > got 0.4157611505752108
# Wed Aug 23 14:40:08 2023 > got 0.9356153370431637
# Wed Aug 23 14:40:09 2023 > got 0.3897435742013611
# Wed Aug 23 14:40:10 2023 > got 0.3551019933735605
# Wed Aug 23 14:40:10 2023 > got 0.48682428380608456
# Wed Aug 23 14:40:10 2023 > got 0.03384896085182587
# Wed Aug 23 14:40:10 2023 > got 0.0803710570077999
# Wed Aug 23 14:40:11 2023 > got 0.9859618954383385
# Wed Aug 23 14:40:12 2023 > got 0.9280599352291954
# Wed Aug 23 14:40:12 2023 > got 0.7399216539671414
# Wed Aug 23 14:40:13 2023 > got 0.5349717321296003
# Wed Aug 23 14:40:13 2023 Producer: Done
# Wed Aug 23 14:40:14 2023 > got 0.9490159685775565
# Wed Aug 23 14:40:14 2023 Producer: Done
# Wed Aug 23 14:40:15 2023 > got 0.34956432094581624
# Wed Aug 23 14:40:15 2023 > got 0.5899575388199375
# Wed Aug 23 14:40:15 2023 Producer: Done
# Wed Aug 23 14:40:16 2023 > got 0.9237156741089296
# Wed Aug 23 14:40:17 2023 > got 0.17293670027469688
# Wed Aug 23 14:40:17 2023 Producer: Done
# Wed Aug 23 14:40:17 2023 > got 0.6343729782785077
# Wed Aug 23 14:40:17 2023 Producer: Done
# Wed Aug 23 14:40:17 2023 > got 0.33554082979825206
# Wed Aug 23 14:40:18 2023 > got 0.49718862683954557