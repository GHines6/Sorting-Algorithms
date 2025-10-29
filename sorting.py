def bubblesort(list):
    sorted = False
    while not sorted:
        sorted = True
        for num in range(len(list) - 1):
            if list[num] > list[num + 1]:
                sorted = False
                list[num], list[num+1] = list[num+1], list[num]
    return list
#bubble sorting


def selectionsort(list):
    indexing_length = range(0, len(list)-1)
    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_value]:
                min_value = j
        if min_value != i:
            list[i], list[min_value] = list[min_value], list[i]
    return list
#selection sorting


numbers = input("Enter numbers separated by commas: ")
#getting the numbers the user wants to sort

print() #empty space separating the output

typeofsort = input("What type of sorting?\n1 - Bubble\n2 - Selection\n")
#asking what type of sorting algorithm the user wants to use

dosort = True
numlist = []
#setting variables

for char in numbers.split(","):
    if char:
        numlist.append(int(char))
#creating a list of the numbers eliminating the commas

if typeofsort == "1":
    mysort = bubblesort(numlist)
    typeofsort = "Bubble"
elif typeofsort == "2":
    mysort = selectionsort(numlist)
    typeofsort = "Selection"
else:
    print()
    print("Invalid input")
    dosort = False
#calling the methods to solve the algorithm depending on the type of sort the user wanted

if dosort:
    print()
    print(f"{typeofsort} Sorted list: {mysort}")
#prints the type of algorithm used with the sorted list
