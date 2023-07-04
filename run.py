import threading
from concurrent import futures
import time

start = time.perf_counter()


def do_something(second):
    print(f'Sleeping {second} second...')
    time.sleep(second)
    return f'Done sleeping in {second} second...'


secs = [5, 4, 3, 2, 1]
# OLD WAYS
# threads = []
# results = []
# for sec in secs:
#     t = threading.Thread(target=lambda: results.append(do_something(sec)))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# for result in results:
#     print(result)


# NEW WAYS
with futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in futures.as_completed(results):
        print(f.result())
        
    # OR
    
    # results = executor.map(do_something, secs)
    
    # for result in results:
    #     print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')
