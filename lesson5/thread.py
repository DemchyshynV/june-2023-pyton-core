import threading
import time

#
# def show(n):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#         time.sleep(0.5)
#
#
# thread = threading.Thread(target=show, args=(10,))
# thread1 = threading.Thread(target=show, args=(10,))
# thread.start()
# thread.join()
# thread1.start()
# thread1.join()
#
# print('Hello')
#
# for i in range(5):
#     print(threading.current_thread().name)
#     time.sleep(0.5)
#     print(i)
#
# print(threading.current_thread().name)

# count = 0
# lock = threading.Lock()


# def inc():
#     with lock:
#         global count
#         count += 1
#         print(count)
#
#
# threads = []
#
# for _ in range(1000):
#     thread = threading.Thread(target=inc)
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
