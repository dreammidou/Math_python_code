import threading
import queue
import time
import random

class PrimeFinder(threading.Thread):
    def __init__(self, task_queue, result_queue):
        super().__init__()
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            n = self.task_queue.get()
            if n is None:
                self.task_queue.task_done()
                break
            is_prime = self.is_prime(n)
            self.result_queue.put((n, is_prime))
            self.task_queue.task_done()

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def main():
    NUM_WORKERS = 4
    NUM_TASKS = 20

    task_queue = queue.Queue()
    result_queue = queue.Queue()
    workers = [PrimeFinder(task_queue, result_queue) for _ in range(NUM_WORKERS)]

    for w in workers:
        w.start()

    numbers = [random.randint(10**5, 10**6) for _ in range(NUM_TASKS)]
    for n in numbers:
        task_queue.put(n)

    for _ in workers:
        task_queue.put(None)

    task_queue.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    results.sort()
    for n, is_prime in results:
        print(f"{n} is {'prime' if is_prime else 'not prime'}")

if __name__ == "__main__":
    main()