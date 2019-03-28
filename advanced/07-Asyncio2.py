import asyncio

# definition of a coroutine
async def coroutine(i):
    print('coroutine_{} is active on the event loop'.format(i))

    print('coroutine_{} yielding control. Going to be blocked for 4 seconds'.format(i))
    await asyncio.sleep(4)

    print('coroutine_{} resumed. coroutine_1 exiting'.format(i))


# this is the event loop
loop = asyncio.get_event_loop()

# schedule both the coroutines to run on the event loop
loop.run_until_complete(asyncio.gather(*[coroutine(i) for i in range(5)]))
