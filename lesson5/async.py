import asyncio


async def print_num():
    num = 1
    while True:
        print(f'{num=}')
        num += 1
        await asyncio.sleep(0.1)


async def print_time():
    time = 0
    while True:
        print(f'{time=}')
        time += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_num())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task1)


asyncio.run(main())
