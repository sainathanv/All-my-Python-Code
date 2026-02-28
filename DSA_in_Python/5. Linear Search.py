# Let us perform a linear search algorithm which parses through the list and checks for the search element. 
# If it is found, it returns the index of the element. If it is not found, it returns a message that the search element is not found.

a = [23, 11, 19, 26, 7, 8, 2, 14, 25]
K = int(input("Search Element: "))

def search(a, K):
    i = 0
    while i<len(a) and a[i] != K:
        i = i + 1
    if i < len(a):
        print("Search eLement found!")
        print("Found at index: ", i + 1)
    else:
        print("Search element not found!")

search(a, K)