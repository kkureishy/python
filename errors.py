def main():
    flowerList = []
    flower = ""
    count =1
    while flower != "done":
        flower = (input("Enter flower name: "))
        flowerList.append(flower)
        flowerList.sort()
    flowerList.remove("done")
    for i in flowerList:
        print(str(count) + ". " + i.capitalize())
        count +=1
    x = int(input("Enter number to access flower: "))
    for j in range(len(flowerList)):
        if (x-1) == j:
            print("Flower found:" + flowerList[j])

main()