import random
import multiprocessing

data = [[random.randint(0,99) for _ in range(12)] for _ in range(12)]
with open("data.txt", "w") as f:
    for row in data:
        f.write(" ".join(map(str, row)) + "\n")

def create_mapping(manager_list):
    # Process A: read data from file into shared list
    with open('data.txt', 'r') as f:
        array = [list(map(int, line.split())) for line in f]
    manager_list[:] = array

def sort_array(manager_list):
    # Process B: sort the array
    flattened = [item for sublist in manager_list for item in sublist]
    flattened.sort()
    manager_list[:] = [flattened[i:i+12] for i in range(0, len(flattened), 12)]

def display_array(manager_list):
    # Process C: display the array
    for i in range(12):
        for j in range(12):
            print(f"{manager_list[i][j]:>2}", end=" ")
        print()

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        manager_list = manager.list()
        
        p1 = multiprocessing.Process(target=create_mapping, args=(manager_list,))
        p2 = multiprocessing.Process(target=sort_array, args=(manager_list,))
        p3 = multiprocessing.Process(target=display_array, args=(manager_list,))

        p1.start()
        p1.join() 
        p2.start()
        p2.join() 
        p3.start()
        p3.join() 
