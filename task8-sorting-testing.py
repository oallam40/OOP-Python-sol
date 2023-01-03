import random
import time

def selection_sort(data):
    # # Iterate over the entire list
    # for i in range(len(lst) - 1):
    #     # Find the index of the minimum element
    #     min_index = i
    #     for j in range(i + 1, len(lst)):
    #         if lst[j] < lst[min_index]:
    #             min_index = j
        
    #     # Swap the minimum element with the first element
    #     lst[i], lst[min_index] = lst[min_index], lst[i]
     pass

def bubble_sort(lst):
    # # Iterate over the entire list
    # for i in range(len(lst) - 1):
    #     # Iterate over the list up to the i-th element
    #     for j in range(len(lst) - 1 - i):
    #         # Swap adjacent elements if they are out of order
    #         if lst[j] > lst[j + 1]:
    #             lst[j], lst[j + 1] = lst[j + 1], lst[j]
     pass

def merge_sort(lst):
    # Base case: if the list is of length 1, it is already sorted
    if len(lst) == 1:
        return lst
    
    # Split the list into two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    
    # Recursively sort both halves
    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left_half_sorted) and right_index < len(right_half_sorted):
        if left_half_sorted[left_index] < right_half_sorted[right_index]:
            merged.append(left_half_sorted[left_index])
            left_index += 1
        else:
            merged.append(right_half_sorted[right_index])
            right_index += 1
    # Add any remaining elements from the left or right halves
    merged.extend(left_half_sorted[left_index:])
    merged.extend(right_half_sorted[right_index:])
    
    return merged
     
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
            for i in range(10):
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
