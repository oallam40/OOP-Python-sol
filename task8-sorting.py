import random
import time

def selection_sort(data):
    # Your implementation of selection sort goes here
    print("Test Starts")    
    # prepare copy of input list
    array = data.copy()
    size = len(array)
    
    
    # iterate through the whole list
    for step in range(size):
        min_index = step
        
        # we iterate from the step index, because min values are already sorted from the left
        for i in range(step, size):
         
            # select the minimum element in each loop
            if array[i] < array[min_index]:
                min_index = i
         
        # put min at the correct position
        (array[step], array[min_index]) = (array[min_index], array[step])
        
#         # alternative way of swapping:
#         temp =  array[step]
#         array[step] = array[min_index]
#         array[min_index] = temp
    print("Task Complete")
    return

def bubble_sort(lst):
    # Your implementation of bubble sort goes here
    pass

def merge_sort(lst):
    # Your implementation of merge sort goes here
    pass

def evaluate_sorting_algorithm(algorithm, lst):
    # Make a copy of the list so we don't modify the original
    lst = lst.copy()
    
    # Time how long it takes to sort the list using the given algorithm
    start_time = time.perf_counter()
    algorithm(lst)
    end_time = time.perf_counter()
    
    return end_time - start_time

def compare_sorting_algorithms(algorithms, categories):
    # Create a dictionary to store the results
    results = {}
    
    # Iterate over each category (number of elements in the list)
    for n in categories:
        # Generate a random list of n elements
        lst = [random.randint(1, 100) for _ in range(n)]
        
        # Create a subdictionary for this category
        results[n] = {}
        
        # Evaluate the performance of each algorithm in this category
        for algorithm in algorithms:
            # Store the average time and standard deviation for this algorithm in this category
            results[n][algorithm.__name__] = {
                "avg_time": 0.0,
                "std_dev": 0.0
            }
            
            # Run the algorithm 100 times to get a good estimate of its performance
            times = []
            
            # change range(1) <----> range(100) or n-times and get a more accurate estimate of the algorithm performance.
            for i in range(1): # we can change to 100 or 1.. here
                t = evaluate_sorting_algorithm(algorithm, lst)
                times.append(t)
                
            # Calculate the average time and standard deviation for this algorithm in this category
            results[n][algorithm.__name__]["avg_time"] = sum(times) / len(times)
            results[n][algorithm.__name__]["std_dev"] = (sum((t - results[n][algorithm.__name__]["avg_time"]) ** 2 for t in times) / len(times)) ** 0.5
            
    return results

# Define the categories and the algorithms to compare
categories = [100, 1000, 10000, 100000]
algorithms = [selection_sort, bubble_sort, merge_sort, sorted]

# Compare the performance of the algorithms
results = compare_sorting_algorithms(algorithms, categories)

# Print the results
for n, data in results.items():
    print(f"Number of elements: {n}")
    for algorithm, stats in data.items():
        print(f"  {algorithm}:")
        print(f"    Average time: {stats['avg_time']:.6f} seconds")
        print(f"    Standard deviation: {stats['std_dev']:.6f} seconds")
