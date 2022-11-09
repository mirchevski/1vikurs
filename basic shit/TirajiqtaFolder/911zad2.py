# 2. napravete funkciq, koqto priema argument spisuk, precenqva dali e monotonno namalqvashta, uveli4avashta ili ne moje da opredeli

def check(arr):
    N = len(arr)
    inc = True
    dec = True

    # Loop to check if array is increasing
    for i in range(0, N-1):

        # To check if array is not increasing
        if arr[i] > arr[i+1]:
            inc = False

    # Loop to check if array is decreasing
    for i in range(0, N-1):

       # To check if array is not decreasing
        if arr[i] < arr[i+1]:
            dec = False

    # Pick one whether inc or dec
    return inc or dec

# Driver code
arr = [6,5,4,3,2,21]

    # Function call
ans = check(arr)
if ans == True:
        print("Yes")
else:
        print("No")
