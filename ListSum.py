
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

def reverseArray(array):
    return array[::-1]

def main():

    print("Input each number of your array followed by the Enter key(input END to stop inputting numbers)")
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