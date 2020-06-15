#!/usr/bin/python3

from multiprocessing import Process

global num_primes

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True

def count_primes_in_range(start, end):
    total = 0
    for x in range(start, end):
        if is_prime(x):
            total += 1
    return total

def run(begin, end):
    global num_primes
    num_primes += count_primes_in_range(begin, end)
    print("begin: {0} end: {1}".format(begin, end))



def main():

    # Declare variables, retrieve num of threads, find range of numbers for each thread
    global num_primes
    num_primes = 0
    thread_count = int(input("How many processes?\n"))
    start = 0
    end = 20000
    processes_distribution = int((end - start) / thread_count)

    # Assign range of numbers to traverse for each thread
    next_loop_start = 0
    for x in range(thread_count):
        this_thread_start = next_loop_start + x
        this_thread_end = next_loop_start + processes_distribution + x
        next_loop_start = next_loop_start + processes_distribution

        if this_thread_end > end:
            this_thread_end = this_thread_end - x
        processes = Process(target=run, args=(this_thread_start, this_thread_end))
        processes.start()
        print(processes)

    for x in range(thread_count):
        processes.join()

    print(num_primes)

if __name__ == "__main__":
    main()

#!/usr/bin/python3

from threading import Thread

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True

def count_primes_in_range(start, end):
    total = 0
    for x in range(start, end):
        if is_prime(x):
            total += 1
    return total

def run(begin, end):
    global num_primes
    x = count_primes_in_range(begin, end)
    num_primes += x
    print("begin: {0} end: {1}".format(begin, end))

def main():

    # Declare variables, retrieve num of threads, find range of numbers for each thread
    global num_primes
    num_primes = 0
    thread_count = int(input("How many threads?\n"))
    start = 0
    end = 20000
    processes_distribution = int((end - start) / thread_count)

    # Assign range of numbers to traverse for each thread
    next_loop_start = 0
    for x in range(thread_count):
        this_thread_start = next_loop_start + x
        this_thread_end = next_loop_start + processes_distribution + x
        next_loop_start = next_loop_start + processes_distribution

        if this_thread_end > end:
            this_thread_end = this_thread_end - x
        processes = Process(target=run, args=(this_thread_start, this_thread_end))
        processes.start()
        print(processes)

    for x in range(thread_count):
        processes.join()

    print(num_primes)

if __name__ == "__main__":
    main()