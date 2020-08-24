arr = list(map(int, input("Enter array: ").split()));
key = int(input("Enter search key: "));

def linearsearch(arr, key):
    length = len(arr);
    for i in range(0, length):
        if(arr[i] == key):
            return i;
    return -1;

search = linearsearch(arr, key);
if(search == -1):
    print('Key doesnt exists in array');
else:
    print("Key exists in index ", search);