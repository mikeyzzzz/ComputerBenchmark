import threading
import time
import sys
import os
from tabulate import tabulate
from BenchmarkData import *
import math

class BenchmarkThread(threading.Thread):
    
    numberOfOperations = 10000000 #Choose the total number of operations that will be used to base the benchmark off of (10,000,000 = about 1 min | 100,000,000 = about 5+ min)

    def __init__(self,threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID + 1 

    def createMultipleThreads(numberOfThreads):
        threads = []

        for thread in range(numberOfThreads):
            t=BenchmarkThread(thread)
            threads.append(t)

        return threads
    
    def startThreads(listOfThreads,benchmark):
        numberOfThreads = len(listOfThreads)
       
        for thread in listOfThreads:
            thread.run()
               
            if numberOfThreads == 1:
                benchmark.oneThreadFlops.append(BenchmarkThread.AdditionFLOPS(thread,numberOfThreads))
                benchmark.oneThreadFlops.append(BenchmarkThread.SubtractionFLOPS(thread,numberOfThreads))
                benchmark.oneThreadFlops.append(BenchmarkThread.MultiplicationFLOPS(thread,numberOfThreads))
                benchmark.oneThreadFlops.append(BenchmarkThread.DivisionFLOPS(thread,numberOfThreads))
                benchmark.oneThreadIops.append(BenchmarkThread.AdditionIOPS(thread,numberOfThreads))
                benchmark.oneThreadIops.append(BenchmarkThread.SubtractionIOPS(thread,numberOfThreads))
                benchmark.oneThreadIops.append(BenchmarkThread.MultiplicationIOPS(thread,numberOfThreads))
                benchmark.oneThreadIops.append(BenchmarkThread.DivisionIOPS(thread,numberOfThreads))
            elif numberOfThreads == 2:
                benchmark.twoThreadFlops[0].append(BenchmarkThread.AdditionFLOPS(thread,numberOfThreads))
                benchmark.twoThreadFlops[1].append(BenchmarkThread.SubtractionFLOPS(thread,numberOfThreads))
                benchmark.twoThreadFlops[2].append(BenchmarkThread.MultiplicationFLOPS(thread,numberOfThreads))
                benchmark.twoThreadFlops[3].append(BenchmarkThread.DivisionFLOPS(thread,numberOfThreads))
                benchmark.twoThreadIops[0].append(BenchmarkThread.AdditionIOPS(thread,numberOfThreads))
                benchmark.twoThreadIops[1].append(BenchmarkThread.SubtractionIOPS(thread,numberOfThreads))
                benchmark.twoThreadIops[2].append(BenchmarkThread.MultiplicationIOPS(thread,numberOfThreads))
                benchmark.twoThreadIops[3].append(BenchmarkThread.DivisionIOPS(thread,numberOfThreads))

            elif numberOfThreads == 4:
                benchmark.fourThreadFlops[0].append(BenchmarkThread.AdditionFLOPS(thread,numberOfThreads))
                benchmark.fourThreadFlops[1].append(BenchmarkThread.SubtractionFLOPS(thread,numberOfThreads))
                benchmark.fourThreadFlops[2].append(BenchmarkThread.MultiplicationFLOPS(thread,numberOfThreads))
                benchmark.fourThreadFlops[3].append(BenchmarkThread.DivisionFLOPS(thread,numberOfThreads))
                benchmark.fourThreadIops[0].append(BenchmarkThread.AdditionIOPS(thread,numberOfThreads))
                benchmark.fourThreadIops[1].append(BenchmarkThread.SubtractionIOPS(thread,numberOfThreads))
                benchmark.fourThreadIops[2].append(BenchmarkThread.MultiplicationIOPS(thread,numberOfThreads))
                benchmark.fourThreadIops[3].append(BenchmarkThread.DivisionIOPS(thread,numberOfThreads))

            elif numberOfThreads == 8:
                benchmark.eightThreadFlops[0].append(BenchmarkThread.AdditionFLOPS(thread,numberOfThreads))
                benchmark.eightThreadFlops[1].append(BenchmarkThread.SubtractionFLOPS(thread,numberOfThreads))
                benchmark.eightThreadFlops[2].append(BenchmarkThread.MultiplicationFLOPS(thread,numberOfThreads))
                benchmark.eightThreadFlops[3].append(BenchmarkThread.DivisionFLOPS(thread,numberOfThreads))
                benchmark.eightThreadIops[0].append(BenchmarkThread.AdditionIOPS(thread,numberOfThreads))
                benchmark.eightThreadIops[1].append(BenchmarkThread.SubtractionIOPS(thread,numberOfThreads))
                benchmark.eightThreadIops[2].append(BenchmarkThread.MultiplicationIOPS(thread,numberOfThreads))
                benchmark.eightThreadIops[3].append(BenchmarkThread.DivisionIOPS(thread,numberOfThreads))

              
            
           
        print( (str)(numberOfThreads) + " thread(s) test complete")
                                                                                                           
    def AdditionFLOPS(self,numberOfThreads):
        self.addsum = 0.0

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.addsum += 1.0
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))

    def SubtractionFLOPS(self,numberOfThreads):
        self.subsum = sys.float_info.max

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.subsum -= 1.0
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))

    def MultiplicationFLOPS(self,numberOfThreads):
        self.product = 1.0

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.product *= 1.0
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))

    def DivisionFLOPS(self,numberOfThreads):
        self.quotient = sys.float_info.max

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.quotient /= 1.0
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))
    
    def AdditionIOPS(self,numberOfThreads):
        self.addsum = 0

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.addsum += 1
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))    

    def SubtractionIOPS(self,numberOfThreads):
        self.subsum = sys.maxsize

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.subsum -= 1
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))

    def MultiplicationIOPS(self,numberOfThreads):
        self.product = 1

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.product *= 1
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))

    def DivisionIOPS(self,numberOfThreads):
        self.quotient = sys.maxsize

        startTime = time.time()
        for i in range((int)(BenchmarkThread.numberOfOperations/numberOfThreads)):
            self.quotient /= 1
        endTime = time.time()

        return (((BenchmarkThread.numberOfOperations)/(endTime-startTime))/(math.pow(10,9)))
    
    def runBenchmark(benchmark):
        threadTest1 = BenchmarkThread.createMultipleThreads(1)
        BenchmarkThread.startThreads(threadTest1,benchmark)

        threadTest2 = BenchmarkThread.createMultipleThreads(2)
        BenchmarkThread.startThreads(threadTest2,benchmark)

        threadTest4 = BenchmarkThread.createMultipleThreads(4)
        BenchmarkThread.startThreads(threadTest4,benchmark)

        threadTest8 = BenchmarkThread.createMultipleThreads(8)
        BenchmarkThread.startThreads(threadTest8,benchmark)
    
    
        









        

    
