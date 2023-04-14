import asyncio, time

start = time.time()

def blocking_io(num):
    print(f"Запуск `blocking_io({num})`: {time.strftime('%X')}")
    # Функция `time.sleep()` может быть заменена любой другой
    #  блокирующей операцией, например файловым вводом/выводом.
    time.sleep(10)
    print(f"Функция `blocking_io({num})` завершена: {time.strftime('%X')}")

async def main():
    print(f"Старт цикла событий: {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io,num=1),
    asyncio.to_thread(blocking_io,num=2))
        # asyncio.sleep(1))

    print(f"Завершение цикла событий: {time.strftime('%X')}")

asyncio.run(main())

end = time.time() - start
print(end)
