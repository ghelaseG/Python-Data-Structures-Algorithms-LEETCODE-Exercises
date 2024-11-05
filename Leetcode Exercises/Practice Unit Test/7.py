"""
Write a Python unit test program to check if a function handles multi-threading correctly.
"""

import unittest
import threading

def perform_task():
    result = 0

    #simulate a task, summing nr till 99999
    for i in range(1, 100000):
        result += i
    
    return result

class TestMultiThreading(unittest.TestCase):
    def test_multi_thread(self):
        num_threads = 10
        threads = []

        for _ in range(num_threads):
            #create a thread, specifying the target function 'perform_task'
            t = threading.Thread(target=perform_task)
            #append the thread to the 'threads' list
            threads.append(t)
            #start the thread execution
            t.start()
        
        #wait for all threads to finish
        for t in threads:
            t.join()

        #assert that all threads have completed successfully
        for t in threads:
            self.assertFalse(t.is_alive())

if __name__ == '__main__':
    unittest.main()