from tqdm import tqdm

import asyncio
import requests

# definition of a coroutine
async def coroutine(i):
    print('coroutine_{} is active on the event loop'.format(i))

    print('coroutine_{} yielding control. Going to be blocked for 4 seconds'.format(i))
    res = await loop.run_in_executor(
        None,
        requests.get,
        'http://googles.es/'
    )
    
    # With arguments
    # res = await loop.run_in_executor(
    #     None,
    #     functools.partial(requests.get,
    #             url='https://google.es'
    #     )
    # )

    print('coroutine_{} resumed. coroutine_1 exiting'.format(i))
    return res


# this is the event loop
loop = asyncio.get_event_loop()

tasks2 = [coroutine(i) for i in range(5)]

import pdb; pdb.set_trace()
res = []
for i in tqdm(asyncio.as_completed(tasks2), total=5):
    res.append(loop.run_until_complete(i))
print("pepe", res)

loop.close()
