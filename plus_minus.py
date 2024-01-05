from numpy import double
def plusMinus(arr):
    # Write your code here
    m = {}
    n = len(arr)
    for i in range(n):
        if arr[i]>0:
            m.setdefault("positive", 0)
            m["positive"]+=1
        elif arr[i]<0:
            m.setdefault("negative", 0)
            m["negative"] += 1
        else:
            m.setdefault("zero", 0)
            m["zero"] += 1
    positive = 0
    zero = 0
    negative = 0
    for key, value in m.items():
        if key == "positive":
            positive = double(value / n)
        elif key == "negative":
            negative = double(value / n)
        else:
            zero = double(value / n)

    print(positive)
    print(negative)
    print(zero)

arr=[1,1,0,-1,-1]
plusMinus(arr)