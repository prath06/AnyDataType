def bubbleSort(inputData):
    for el in range(len(inputData)-1,0,-1):
        for i in range(el):
            if inputData[i] > inputData[i+1]:
                temp = inputData[i]
                inputData[i] = inputData[i+1]
                inputData[i+1] = temp

nlist = []     
noi = int(input("How many numbers?"))
for a in range(noi):
    print("Enter %dth int number:" %a, end="")
    nlist.append(int(input()))

bubbleSort(nlist)
print(nlist)

slist = []     
noi = int(input("How many Names?"))
for a in range(noi):
    print("Enter %dth name:" %a, end="")
    slist.append(input())

bubbleSort(slist)
print(slist)

flist = []     
noi = int(input("How many Float numbers?"))
for a in range(noi):
    print("Enter %dth Float number:" %a, end="")
    flist.append(float(input()))

bubbleSort(flist)
print(flist)
