#!/usr/bin/python3

import os

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            
        return True


def count_primes_in_range(start, end):
    total = 0
    print(start)
    print(end)
    for x in range(start, end):
        if is_prime(x):
            total += 1
    return total

def main():
    # Declare variables, retrieve num of threads, find range of numbers for each thread
    global num_primes
    num_primes = 0
    process_count = int(input("How many processes?\n"))
    start = 1000
    end = 100000
    process_distribution = int((end - start) / process_count)
    fork_pids = []

    # Assign range of numbers to traverse for each thread
    next_loop_start = 0
    this_process_start = 0
    this_process_end = 0
    for x in range(process_count):
        ret = os.fork()
        if ret == 0:
            this_process_start = x * process_distribution + start
            this_process_end = (x + 1) * process_distribution + start
            next_loop_start = next_loop_start + process_distribution
            print(count_primes_in_range(this_process_start, this_process_end))
            return

        else:
            #append value of pid to the lists
            fork_pids.append(ret)
            print("Parent process")

    for pid in fork_pids:
        print("Waiting on pid in fork_pids")
        os.waitpid(pid, 0)
        print(num_primes)


if __name__ == "__main__":
    main()
