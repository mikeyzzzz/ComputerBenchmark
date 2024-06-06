import BenchmarkThreading
import matplotlib.pyplot as plt
import numpy as np
import statistics


class BenchmarkData:

    def __init__(self):
        self.oneThreadFlops = []
        self.twoThreadFlops = [[],[],[],[]]
        self.fourThreadFlops = [[],[],[],[]]
        self.eightThreadFlops = [[],[],[],[]]
        self.oneThreadIops = []
        self.twoThreadIops = [[],[],[],[]]
        self.fourThreadIops = [[],[],[],[]]
        self.eightThreadIops = [[],[],[],[]]
 
    def printData(self):
        print(self.oneThreadFlops)
        print(self.twoThreadFlops)
        print(self.fourThreadFlops)
        print(self.eightThreadFlops)
        print(self.oneThreadFlops)
        print(self.twoThreadFlops)
        print(self.fourThreadFlops)
        print(self.eightThreadFlops)

    def calculateAverageForEachOperationOfThread(array):
        averageForEachOperation = []

        average = np.average(array[0])
        averageForEachOperation.append(average)

        average = np.average(array[1])
        averageForEachOperation.append(average)

        average = np.average(array[2])
        averageForEachOperation.append(average)

        average = np.average(array[3])
        averageForEachOperation.append(average)

        return averageForEachOperation

    def calculateAverageFLOPSMatrix(self):
        averageFLOPSMatrix = [[],[],[],[]]
                    
        averageFLOPSMatrix[0] = self.oneThreadFlops
        averageFLOPSMatrix[1] = BenchmarkData.calculateAverageForEachOperationOfThread(self.twoThreadFlops)
        averageFLOPSMatrix[2] = BenchmarkData.calculateAverageForEachOperationOfThread(self.fourThreadFlops)
        averageFLOPSMatrix[3] = BenchmarkData.calculateAverageForEachOperationOfThread(self.eightThreadFlops)

        return averageFLOPSMatrix

    def calculateAverageIOPSMatrix(self):
        averageIOPSMatrix = [[],[],[],[]]
                    
        averageIOPSMatrix[0] = self.oneThreadFlops
        averageIOPSMatrix[1] = BenchmarkData.calculateAverageForEachOperationOfThread(self.twoThreadIops)
        averageIOPSMatrix[2] = BenchmarkData.calculateAverageForEachOperationOfThread(self.fourThreadIops)
        averageIOPSMatrix[3] = BenchmarkData.calculateAverageForEachOperationOfThread(self.eightThreadIops)

        return averageIOPSMatrix
    
    def createFLOPSGraph(self):

        operation = ("Add", "Subtract", "Multiplication", "Division")
    
        onethread = BenchmarkData.calculateAverageFLOPSMatrix(self)[0]
        twothread = BenchmarkData.calculateAverageFLOPSMatrix(self)[1]
        fourthread = BenchmarkData.calculateAverageFLOPSMatrix(self)[2]
        eightthread = BenchmarkData.calculateAverageFLOPSMatrix(self)[3]

        thread = {
            '1 Thread': (onethread),
            '2 Thread': (twothread),
            '4 Thread': (fourthread),
            '8 Thread': (eightthread)
        }

        x = np.arange(len(operation))  # the label locations
        width = 0.21  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in thread.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GigaFlops')
        ax.set_title('Benchmark - Floating Point Operations Per Second (GigaFlops 10^9)')
        ax.set_xticks(x + width / 2, operation)
        ax.legend(loc='upper left', ncols=4)
        ax.set_ylim(0, .4)

        plt.show()

    def createIOPSGraph(self):

        operation = ("Add", "Subtract", "Multiplication", "Division")
    
        onethread = BenchmarkData.calculateAverageIOPSMatrix(self)[0]
        twothread = BenchmarkData.calculateAverageIOPSMatrix(self)[1]
        fourthread = BenchmarkData.calculateAverageIOPSMatrix(self)[2]
        eightthread = BenchmarkData.calculateAverageIOPSMatrix(self)[3]

        thread = {
            '1 Thread': (onethread),
            '2 Thread': (twothread),
            '4 Thread': (fourthread),
            '8 Thread': (eightthread)
        }

        x = np.arange(len(operation))  # the label locations
        width = 0.21  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in thread.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GigaFlops')
        ax.set_title('Benchmark - Integer Operations Per Second (GigaIOPS 10^9)')
        ax.set_xticks(x + width / 2, operation)
        ax.legend(loc='upper left', ncols=4)
        ax.set_ylim(0, .4)

        plt.show()

    def calculateOverallFLOPSAverageGraph(benchmark1,benchmark2,benchmark3):

        oneThreadAverages = []
        twoThreadAverages = []
        fourThreadAverages = []
        eightThreadAverages = []
        overallThreadAverages = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for i in range(3):
            if (i==0):
                oneThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[3])
            if (i==1):
                oneThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[3])
            if (i==2):
                oneThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[3])

        overallThreadAverages[0][0] = ((oneThreadAverages[0][0] + oneThreadAverages[1][0] + oneThreadAverages[2][0]) / 3)
        overallThreadAverages[0][1] = ((oneThreadAverages[0][1] + oneThreadAverages[1][1] + oneThreadAverages[2][1]) / 3)
        overallThreadAverages[0][2] = ((oneThreadAverages[0][2] + oneThreadAverages[1][2] + oneThreadAverages[2][2]) / 3)
        overallThreadAverages[0][3] = ((oneThreadAverages[0][3] + oneThreadAverages[1][3] + oneThreadAverages[2][3]) / 3)

        overallThreadAverages[1][0] = ((twoThreadAverages[0][0] + twoThreadAverages[1][0] + twoThreadAverages[2][0]) / 3)
        overallThreadAverages[1][1] = ((twoThreadAverages[0][1] + twoThreadAverages[1][1] + twoThreadAverages[2][1]) / 3)
        overallThreadAverages[1][2] = ((twoThreadAverages[0][2] + twoThreadAverages[1][2] + twoThreadAverages[2][2]) / 3)
        overallThreadAverages[1][3] = ((twoThreadAverages[0][3] + twoThreadAverages[1][3] + twoThreadAverages[2][3]) / 3)

        overallThreadAverages[2][0] = ((fourThreadAverages[0][0] + fourThreadAverages[1][0] + fourThreadAverages[2][0]) / 3)
        overallThreadAverages[2][1] = ((fourThreadAverages[0][1] + fourThreadAverages[1][1] + fourThreadAverages[2][1]) / 3)
        overallThreadAverages[2][2] = ((fourThreadAverages[0][2] + fourThreadAverages[1][2] + fourThreadAverages[2][2]) / 3)
        overallThreadAverages[2][3] = ((fourThreadAverages[0][3] + fourThreadAverages[1][3] + fourThreadAverages[2][3]) / 3)

        overallThreadAverages[3][0] = ((eightThreadAverages[0][0] + eightThreadAverages[1][0] + eightThreadAverages[2][0]) / 3)
        overallThreadAverages[3][1] = ((eightThreadAverages[0][1] + eightThreadAverages[1][1] + eightThreadAverages[2][1]) / 3)
        overallThreadAverages[3][2] = ((eightThreadAverages[0][2] + eightThreadAverages[1][2] + eightThreadAverages[2][2]) / 3)
        overallThreadAverages[3][3] = ((eightThreadAverages[0][3] + eightThreadAverages[1][3] + eightThreadAverages[2][3]) / 3)

        operation = ("Add", "Subtract", "Multiplication", "Division")
    
        thread = {
            '1 Thread': (overallThreadAverages[0]),
            '2 Thread': (overallThreadAverages[1]),
            '4 Thread': (overallThreadAverages[2]),
            '8 Thread': (overallThreadAverages[3])
        }

        x = np.arange(len(operation))  # the label locations
        width = 0.21  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in thread.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GigaFlops')
        ax.set_title('Benchmark Overall Average Float Operations Per Second (GigaIOPS 10^9)')
        ax.set_xticks(x + width / 2, operation)
        ax.legend(loc='upper left', ncols=4)
        ax.set_ylim(0, .4)

        plt.show()

    def calculateOverallIOPSAverageGraph(benchmark1,benchmark2,benchmark3):

        oneThreadAverages = []
        twoThreadAverages = []
        fourThreadAverages = []
        eightThreadAverages = []
        overallThreadAverages = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for i in range(3):
            if (i==0):
                oneThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[3])
            if (i==1):
                oneThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[3])
            if (i==2):
                oneThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[3])

       
        overallThreadAverages[0][0] = ((oneThreadAverages[0][0] + oneThreadAverages[1][0] + oneThreadAverages[2][0]) / 3)
        overallThreadAverages[0][1] = ((oneThreadAverages[0][1] + oneThreadAverages[1][1] + oneThreadAverages[2][1]) / 3)
        overallThreadAverages[0][2] = ((oneThreadAverages[0][2] + oneThreadAverages[1][2] + oneThreadAverages[2][2]) / 3)
        overallThreadAverages[0][3] = ((oneThreadAverages[0][3] + oneThreadAverages[1][3] + oneThreadAverages[2][3]) / 3)

        overallThreadAverages[1][0] = ((twoThreadAverages[0][0] + twoThreadAverages[1][0] + twoThreadAverages[2][0]) / 3)
        overallThreadAverages[1][1] = ((twoThreadAverages[0][1] + twoThreadAverages[1][1] + twoThreadAverages[2][1]) / 3)
        overallThreadAverages[1][2] = ((twoThreadAverages[0][2] + twoThreadAverages[1][2] + twoThreadAverages[2][2]) / 3)
        overallThreadAverages[1][3] = ((twoThreadAverages[0][3] + twoThreadAverages[1][3] + twoThreadAverages[2][3]) / 3)

        overallThreadAverages[2][0] = ((fourThreadAverages[0][0] + fourThreadAverages[1][0] + fourThreadAverages[2][0]) / 3)
        overallThreadAverages[2][1] = ((fourThreadAverages[0][1] + fourThreadAverages[1][1] + fourThreadAverages[2][1]) / 3)
        overallThreadAverages[2][2] = ((fourThreadAverages[0][2] + fourThreadAverages[1][2] + fourThreadAverages[2][2]) / 3)
        overallThreadAverages[2][3] = ((fourThreadAverages[0][3] + fourThreadAverages[1][3] + fourThreadAverages[2][3]) / 3)

        overallThreadAverages[3][0] = ((eightThreadAverages[0][0] + eightThreadAverages[1][0] + eightThreadAverages[2][0]) / 3)
        overallThreadAverages[3][1] = ((eightThreadAverages[0][1] + eightThreadAverages[1][1] + eightThreadAverages[2][1]) / 3)
        overallThreadAverages[3][2] = ((eightThreadAverages[0][2] + eightThreadAverages[1][2] + eightThreadAverages[2][2]) / 3)
        overallThreadAverages[3][3] = ((eightThreadAverages[0][3] + eightThreadAverages[1][3] + eightThreadAverages[2][3]) / 3)

        operation = ("Add", "Subtract", "Multiplication", "Division")
    
        thread = {
            '1 Thread': (overallThreadAverages[0]),
            '2 Thread': (overallThreadAverages[1]),
            '4 Thread': (overallThreadAverages[2]),
            '8 Thread': (overallThreadAverages[3])
        }

        x = np.arange(len(operation))  # the label locations
        width = 0.21  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in thread.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GigaFlops')
        ax.set_title('Benchmark Overall Average Integer Operations Per Second (GigaIOPS 10^9)')
        ax.set_xticks(x + width / 2, operation)
        ax.legend(loc='upper left', ncols=4)
        ax.set_ylim(0, .4)

        plt.show()

    def calculateOverallFLOPSStandardDeviationGraph(benchmark1,benchmark2,benchmark3):

        oneThreadAverages = []
        twoThreadAverages = []
        fourThreadAverages = []
        eightThreadAverages = []
        overallThreadStandardDeviation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for i in range(3):
            if (i==0):
                oneThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark1)[3])
            if (i==1):
                oneThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark2)[3])
            if (i==2):
                oneThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageFLOPSMatrix(benchmark3)[3])

        overallThreadStandardDeviation[0][0] = statistics.stdev([oneThreadAverages[0][0],oneThreadAverages[1][0],oneThreadAverages[2][0]])
        overallThreadStandardDeviation[0][1] = statistics.stdev([oneThreadAverages[0][1],oneThreadAverages[1][1],oneThreadAverages[2][1]])
        overallThreadStandardDeviation[0][2] = statistics.stdev([oneThreadAverages[0][2],oneThreadAverages[1][2],oneThreadAverages[2][2]])
        overallThreadStandardDeviation[0][3] = statistics.stdev([oneThreadAverages[0][3],oneThreadAverages[1][3],oneThreadAverages[2][3]])

        overallThreadStandardDeviation[1][0] = statistics.stdev([twoThreadAverages[0][0],twoThreadAverages[1][0],twoThreadAverages[2][0]])
        overallThreadStandardDeviation[1][1] = statistics.stdev([twoThreadAverages[0][1],twoThreadAverages[1][1],twoThreadAverages[2][1]])
        overallThreadStandardDeviation[1][2] = statistics.stdev([twoThreadAverages[0][2],twoThreadAverages[1][2],twoThreadAverages[2][2]])
        overallThreadStandardDeviation[1][3] = statistics.stdev([twoThreadAverages[0][3],twoThreadAverages[1][3],twoThreadAverages[2][3]])

        overallThreadStandardDeviation[2][0] = statistics.stdev([fourThreadAverages[0][0],fourThreadAverages[1][0],fourThreadAverages[2][0]])
        overallThreadStandardDeviation[2][1] = statistics.stdev([fourThreadAverages[0][1],fourThreadAverages[1][1],fourThreadAverages[2][1]])
        overallThreadStandardDeviation[2][2] = statistics.stdev([fourThreadAverages[0][2],fourThreadAverages[1][2],fourThreadAverages[2][2]])
        overallThreadStandardDeviation[2][3] = statistics.stdev([fourThreadAverages[0][3],fourThreadAverages[1][3],fourThreadAverages[2][3]])

        overallThreadStandardDeviation[3][0] = statistics.stdev([eightThreadAverages[0][0],eightThreadAverages[1][0],eightThreadAverages[2][0]])
        overallThreadStandardDeviation[3][1] = statistics.stdev([eightThreadAverages[0][1],eightThreadAverages[1][1],eightThreadAverages[2][1]])
        overallThreadStandardDeviation[3][2] = statistics.stdev([eightThreadAverages[0][2],eightThreadAverages[1][2],eightThreadAverages[2][2]])
        overallThreadStandardDeviation[3][3] = statistics.stdev([eightThreadAverages[0][3],eightThreadAverages[1][3],eightThreadAverages[2][3]])


        operation = ("Add", "Subtract", "Multiplication", "Division")
    
        thread = {
            '1 Thread': (overallThreadStandardDeviation[0]),
            '2 Thread': (overallThreadStandardDeviation[1]),
            '4 Thread': (overallThreadStandardDeviation[2]),
            '8 Thread': (overallThreadStandardDeviation[3])
        }

        x = np.arange(len(operation))  # the label locations
        width = 0.21  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in thread.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GigaFlops (Standard Deviation)')
        ax.set_title('Benchmark Standard Deviation Float Operations Per Second (GigaIOPS 10^9)')
        ax.set_xticks(x + width / 2, operation)
        ax.legend(loc='upper left', ncols=4)
        ax.set_ylim(0, .025)

        plt.show()
        
    def calculateOverallIOPSStandardDeviationGraph(benchmark1,benchmark2,benchmark3):
        
        oneThreadAverages = []
        twoThreadAverages = []
        fourThreadAverages = []
        eightThreadAverages = []
        overallThreadStandardDeviation = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for i in range(3):
            if (i==0):
                oneThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark1)[3])
            if (i==1):
                oneThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark2)[3])
            if (i==2):
                oneThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[0])
                twoThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[1])
                fourThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[2])
                eightThreadAverages.append(BenchmarkData.calculateAverageIOPSMatrix(benchmark3)[3])

        overallThreadStandardDeviation[0][0] = statistics.stdev([oneThreadAverages[0][0],oneThreadAverages[1][0],oneThreadAverages[2][0]])
        overallThreadStandardDeviation[0][1] = statistics.stdev([oneThreadAverages[0][1],oneThreadAverages[1][1],oneThreadAverages[2][1]])
        overallThreadStandardDeviation[0][2] = statistics.stdev([oneThreadAverages[0][2],oneThreadAverages[1][2],oneThreadAverages[2][2]])
        overallThreadStandardDeviation[0][3] = statistics.stdev([oneThreadAverages[0][3],oneThreadAverages[1][3],oneThreadAverages[2][3]])

        overallThreadStandardDeviation[1][0] = statistics.stdev([twoThreadAverages[0][0],twoThreadAverages[1][0],twoThreadAverages[2][0]])
        overallThreadStandardDeviation[1][1] = statistics.stdev([twoThreadAverages[0][1],twoThreadAverages[1][1],twoThreadAverages[2][1]])
        overallThreadStandardDeviation[1][2] = statistics.stdev([twoThreadAverages[0][2],twoThreadAverages[1][2],twoThreadAverages[2][2]])
        overallThreadStandardDeviation[1][3] = statistics.stdev([twoThreadAverages[0][3],twoThreadAverages[1][3],twoThreadAverages[2][3]])

        overallThreadStandardDeviation[2][0] = statistics.stdev([fourThreadAverages[0][0],fourThreadAverages[1][0],fourThreadAverages[2][0]])
        overallThreadStandardDeviation[2][1] = statistics.stdev([fourThreadAverages[0][1],fourThreadAverages[1][1],fourThreadAverages[2][1]])
        overallThreadStandardDeviation[2][2] = statistics.stdev([fourThreadAverages[0][2],fourThreadAverages[1][2],fourThreadAverages[2][2]])
        overallThreadStandardDeviation[2][3] = statistics.stdev([fourThreadAverages[0][3],fourThreadAverages[1][3],fourThreadAverages[2][3]])

        overallThreadStandardDeviation[3][0] = statistics.stdev([eightThreadAverages[0][0],eightThreadAverages[1][0],eightThreadAverages[2][0]])
        overallThreadStandardDeviation[3][1] = statistics.stdev([eightThreadAverages[0][1],eightThreadAverages[1][1],eightThreadAverages[2][1]])
        overallThreadStandardDeviation[3][2] = statistics.stdev([eightThreadAverages[0][2],eightThreadAverages[1][2],eightThreadAverages[2][2]])
        overallThreadStandardDeviation[3][3] = statistics.stdev([eightThreadAverages[0][3],eightThreadAverages[1][3],eightThreadAverages[2][3]])


        operation = ("Add", "Subtract", "Multiplication", "Division")
    
        thread = {
            '1 Thread': (overallThreadStandardDeviation[0]),
            '2 Thread': (overallThreadStandardDeviation[1]),
            '4 Thread': (overallThreadStandardDeviation[2]),
            '8 Thread': (overallThreadStandardDeviation[3])
        }

        x = np.arange(len(operation))  # the label locations
        width = 0.21  # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in thread.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('GigaFlops (Standard Deviation)')
        ax.set_title('Benchmark Standard Deviation Integer Operations Per Second (GigaIOPS 10^9)')
        ax.set_xticks(x + width / 2, operation)
        ax.legend(loc='upper left', ncols=4)
        ax.set_ylim(0, .025)

        plt.show()

       



                
                
                
                
                

        


        

        
            



