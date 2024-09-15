import time

# def slow_task(name, delay):
#     print(f"Starting task {name}: {time.strftime('%X')}")
#     time.sleep(delay)
#     print(f"Finished task {name}: {time.strftime('%X')}")

# def main():
#     slow_task("Task 1", 3)
#     slow_task("Task 2", 7)
#     print("All tasks finished")

# main()


# import asyncio


# async def slow_task(name, delay):
#     print(f"Starting task {name}: {time.strftime('%X')}")
#     await asyncio.sleep(delay)
#     print(f"Finished task {name}: {time.strftime('%X')}")

# async def main():
#     await slow_task("Task 1", 1)
#     await slow_task("Task 2", 10)
#     print("All tasks finished")

# asyncio.run(main())



import asyncio
#import time

async def slow_task(name, delay):
    print(f"Starting task {name}: {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(f"Finished task {name}: {time.strftime('%X')}")

async def main():
    print(f"Starting: {time.strftime('%X')}")

    task1 = asyncio.create_task(slow_task("Task 1", 3))
    print(f"Created task 1: {time.strftime('%X')}")

    task2 = asyncio.create_task(slow_task("Task 2", 7))
    print(f"Created task 2: {time.strftime('%X')}")

    await task1
    print(f"Awaited task 1: {time.strftime('%X')}")

    await task2
    print(f"Awaited task 2: {time.strftime('%X')}")

asyncio.run(main())