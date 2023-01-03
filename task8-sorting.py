import random
import time

def selection_sort(lst):  
    # Iterate over the entire list
    for i in range(len(lst) - 1):
        # Find the index of the minimum element
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element
        lst[i], lst[min_index] = lst[min_index], lst[i]


def bubble_sort(lst):
    # Iterate over the entire list
    for i in range(len(lst) - 1):
        # Iterate over the list up to the i-th element
        for j in range(len(lst) - 1 - i):
            # Swap adjacent elements if they are out of order
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def merge_sort(lst):
    # Base case: if the list is of length 1, it is already sorted
    if len(lst) == 1:
        return lst
    
    # Split the list into two halves
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Merge the sorted halves
    merged = []
    i = 0
    j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1
            
    # Add any remaining elements from the left or right halves
    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])
    
    return merged


def evaluate_sorting_algorithm(algorithm, lst):
    # Making a copy of the list
    lst = lst.copy()
    
    # counting time for each algorithm 
    start_time = time.perf_counter()
    algorithm(lst)
    end_time = time.perf_counter()
    
    return end_time - start_time

def compare_sorting_algorithms(algorithms, categories):
    # Create a dictionary to store the results
    results = {}
    
    # Iterate over each category (number of elements in the list)
    for n in categories:
    
        ############### Generate a random list of n elements #################
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
            
            # Run the algorithm upto 100 times to get a good estimate of its performance
            times = []
            
            # change range(1) <----> range(100) or n-times and get a more accurate estimate of the algorithm performance.
            for i in range(1):          # we can change the number in the range here
                t = evaluate_sorting_algorithm(algorithm, lst)
                times.append(t)
                
            # Calculate the average time and standard deviation for this algorithm in this category
            results[n][algorithm.__name__]["avg_time"] = sum(times) / len(times)
            results[n][algorithm.__name__]["std_dev"] = (sum((t - results[n][algorithm.__name__]["avg_time"]) ** 2 for t in times) / len(times)) ** 0.5
            
    return results

# Defining the categories and the algorithms needed to be compared
categories = [100, 1000, 10000, 100000]
algorithms = [selection_sort, bubble_sort, merge_sort, sorted]

# Comparing the performance of the algorithms
results = compare_sorting_algorithms(algorithms, categories)

# Print the results
for n, data in results.items():
    print(f"Number of elements: {n}")
    for algorithm, stats in data.items():
        print(f"  {algorithm}:")
        print(f"    Average time: {stats['avg_time']:.6f} seconds")
        print(f"    Standard deviation: {stats['std_dev']:.6f} seconds")
