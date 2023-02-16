
def arrSum(array):
    totalSum = 0
    for i in array:
        totalSum += i
    return totalSum

def arrMult(array):
    totalMult = 1
    for i in array:
        totalMult *= i
    return totalMult

def main():

    print("Enter each number of your array(enter END to stop entering numbers)")
    arr = []
    while(True):
        x = input()
        if(x == "END"):
            break
        arr.append(int(x))
    
    print("Total of array: " + str(arrSum(arr)))
    print("Total of array elements multiplied: " + str(arrMult(arr)))

if __name__ == "__main__":
    main()