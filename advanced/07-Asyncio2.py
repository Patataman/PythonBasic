import asyncio

# definition of a coroutine
async def coroutine(i):
    print('coroutine_{} is active on the event loop'.format(i))

    print('coroutine_{} yielding control. Going to be blocked for 4 seconds'.format(i))
    await asyncio.sleep(4)

    print('coroutine_{} resumed. coroutine_1 exiting'.format(i))
    
    # Podemos devolver cosas en los async
    return i


# this is the event loop
loop = asyncio.get_event_loop()

# schedule both the coroutines to run on the event loop
res = loop.run_until_complete(asyncio.gather(*[coroutine(i) for i in range(5)]))

# la variable "res" va a ser una lista con los resultados de las llamadas
print(res)

# buenas prácticas
loop.close()
