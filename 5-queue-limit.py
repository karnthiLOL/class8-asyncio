from random import random
import asyncio
import time

# Coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer {id}: Running')

    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep((id+1)/10)
        # add to queue
        await queue.put(value)
    print(f'{time.ctime()} Producer {id}: Done')

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
    producers = [producer(queue,id_2) for id_2 in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for all item to be processed
    await queue.join()

#start the asyncio program
asyncio.run(main())

##  Reslut
# PS E:\00Lab\IOT\asyncio_exercise> & C:/Users/karnt/AppData/Local/Programs/Python/Python310/python.exe e:/00Lab/IOT/asyncio_exercise/class8-asyncio/5-queue-limit.py
# Wed Aug 23 15:08:20 2023 Consumer: Running
# Wed Aug 23 15:08:20 2023 Producer 0: Running
# Wed Aug 23 15:08:20 2023 Producer 1: Running
# Wed Aug 23 15:08:20 2023 Producer 2: Running
# Wed Aug 23 15:08:20 2023 Producer 3: Running
# Wed Aug 23 15:08:20 2023 Producer 4: Running
# Wed Aug 23 15:08:21 2023 > got 0.5584739295321552
# Wed Aug 23 15:08:21 2023 > got 0.7075094925872761
# Wed Aug 23 15:08:22 2023 > got 0.43274102380877943
# Wed Aug 23 15:08:22 2023 > got 0.10349851857858394
# Wed Aug 23 15:08:22 2023 > got 0.25400055186332293
# Wed Aug 23 15:08:23 2023 > got 0.8251376003928147
# Wed Aug 23 15:08:24 2023 > got 0.8508017812416889
# Wed Aug 23 15:08:24 2023 > got 0.49228376539701413
# Wed Aug 23 15:08:25 2023 > got 0.31677850013291076
# Wed Aug 23 15:08:25 2023 > got 0.11388414036588412
# Wed Aug 23 15:08:25 2023 > got 0.3403415724173169
# Wed Aug 23 15:08:26 2023 > got 0.2039393117584919
# Wed Aug 23 15:08:26 2023 > got 0.06050931625421052
# Wed Aug 23 15:08:26 2023 > got 0.34646317025002416
# Wed Aug 23 15:08:26 2023 > got 0.7484508406462261
# Wed Aug 23 15:08:27 2023 > got 0.7645736753023361
# Wed Aug 23 15:08:28 2023 > got 0.552347777798405
# Wed Aug 23 15:08:28 2023 > got 0.1408653379905973
# Wed Aug 23 15:08:29 2023 > got 0.983645709763564
# Wed Aug 23 15:08:30 2023 > got 0.4436516546827338
# Wed Aug 23 15:08:30 2023 > got 0.6644479529098927
# Wed Aug 23 15:08:31 2023 > got 0.5002753211157952
# Wed Aug 23 15:08:31 2023 > got 0.1246853475956089
# Wed Aug 23 15:08:31 2023 > got 0.8513564814895092
# Wed Aug 23 15:08:32 2023 > got 0.6037574521297621
# Wed Aug 23 15:08:33 2023 > got 0.8523510978687432
# Wed Aug 23 15:08:34 2023 > got 0.5083111477940979
# Wed Aug 23 15:08:34 2023 > got 0.46531787216410536
# Wed Aug 23 15:08:35 2023 > got 0.9919427563186884
# Wed Aug 23 15:08:36 2023 > got 0.3148454068741423
# Wed Aug 23 15:08:36 2023 > got 0.38754212239487185
# Wed Aug 23 15:08:36 2023 > got 0.7997651749842657
# Wed Aug 23 15:08:37 2023 > got 0.7109074978362916
# Wed Aug 23 15:08:38 2023 > got 0.6823095516829876
# Wed Aug 23 15:08:39 2023 > got 0.858418252524578
# Wed Aug 23 15:08:39 2023 > got 0.5021479014456145
# Wed Aug 23 15:08:40 2023 > got 0.7232417347273974
# Wed Aug 23 15:08:41 2023 > got 0.27259536091037095
# Wed Aug 23 15:08:41 2023 Producer 0: Done
# Wed Aug 23 15:08:41 2023 > got 0.3078718434501764
# Wed Aug 23 15:08:41 2023 > got 0.7347933463580008
# Wed Aug 23 15:08:42 2023 > got 0.5171061915921015
# Wed Aug 23 15:08:43 2023 > got 0.09591390356299023
# Wed Aug 23 15:08:43 2023 > got 0.9638396270701743
# Wed Aug 23 15:08:43 2023 Producer 1: Done
# Wed Aug 23 15:08:44 2023 > got 0.6320207471113146
# Wed Aug 23 15:08:44 2023 > got 0.4036290582496729
# Wed Aug 23 15:08:45 2023 > got 0.19212740526849237
# Wed Aug 23 15:08:45 2023 Producer 2: Done
# Wed Aug 23 15:08:45 2023 > got 0.15203301711617456
# Wed Aug 23 15:08:45 2023 Producer 3: Done
# Wed Aug 23 15:08:45 2023 > got 0.12183234528523712
# Wed Aug 23 15:08:45 2023 Producer 4: Done
# Wed Aug 23 15:08:45 2023 > got 0.005157577671135671
# Wed Aug 23 15:08:45 2023 > got 0.16401457012868192