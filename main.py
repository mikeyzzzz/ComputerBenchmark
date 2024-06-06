from BenchmarkThreading import BenchmarkThread
from BenchmarkData import BenchmarkData
import time
import matplotlib


print("Welcome to the benchmark program... you will frequently be asked  to press enter in order continue before and after each set of instructions and operations")
input("Press enter to continue")

print("\nYour CPU speed will be tested by calculating the time it takes to do a fixed amount of operations such as Addition, Subtraction, Multiplication, and Division using both decimal float values, and regular integers")
input("Press enter to continue")

print("\nThe benchmark will also take into account using 1, 2, 4, and 8 threads in order to see if dividing up the work load results in better FLOPs and IOPs results")
input("Press enter to continue")

print("\nThe FLOPS and IOPS results will be represented in GigaFlops and GigaIops representing 10^9 operations")
input("Press enter to continue")

print("\nThe benchmark will print out graphs between each round for FLOPS and IOPS. The benchmark will pause until you continue by exiting out the graphs to continue")
input("Press enter to continue")

print("\nThe benchmark will repeat a total of three rounds, and at the end 4 graphs will be displayed for total averages (2) and standard deviation (2) for all the FLOPS and IOPS results")
input("Press enter to continue")

print("\nAre you ready to begin the benchmark?")
input("Press enter to continue")

print("\nBenchmark beginning...")

print("-------------------------------------------------------------")
print("Round 1 started...")

benchmark1 = BenchmarkData()
BenchmarkThread.runBenchmark(benchmark1)

print("Round 1 complete...")
print("See graphs for results")

BenchmarkData.createFLOPSGraph(benchmark1)
BenchmarkData.createIOPSGraph(benchmark1)

print("-------------------------------------------------------------")
print("Round 2 started...")

benchmark2 = BenchmarkData()
BenchmarkThread.runBenchmark(benchmark2)

print("Round 2 complete...")
print("See graphs for results")

BenchmarkData.createFLOPSGraph(benchmark2)
BenchmarkData.createIOPSGraph(benchmark2)

print("-------------------------------------------------------------")
print("Round 3 started...")

benchmark3 = BenchmarkData()
BenchmarkThread.runBenchmark(benchmark3)

print("Round 3 complete...")
print("See graphs for results")

BenchmarkData.createFLOPSGraph(benchmark3)
BenchmarkData.createIOPSGraph(benchmark3)
print("-------------------------------------------------------------")
print("Calculating overall average and standard deviation graphs for FLOPS, IOPS")
time.sleep(3)

BenchmarkData.calculateOverallFLOPSAverageGraph(benchmark1,benchmark2,benchmark3)
BenchmarkData.calculateOverallIOPSAverageGraph(benchmark1,benchmark2,benchmark3)
BenchmarkData.calculateOverallFLOPSStandardDeviationGraph(benchmark1,benchmark2,benchmark3)
BenchmarkData.calculateOverallIOPSStandardDeviationGraph(benchmark1,benchmark2,benchmark3)

print("-------------------------------------------------------------")
print("Benchmark has completed")







