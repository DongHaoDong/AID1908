import asyncio

async def fun1():
    print("start1")
    # 设置跳转阻塞点
    await asyncio.sleep(2)
    print("end2")

async def fun2():
    print("start2")
    await asyncio.sleep(3)
    print("end2")
# 生成协程对象
cor1 = fun1()
cor2 = fun2()
tasks = [asyncio.ensure_future(cor1),asyncio.ensure_future(cor2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))