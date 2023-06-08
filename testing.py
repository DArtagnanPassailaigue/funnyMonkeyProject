import os
print(os.getcwd()) # gets the Current Working Directory
folder = os.getcwd()
for i in range(1):
        # Team File Creation 
        listData = input("hi:")
        listData2 = input("why:")
        listData3 = input("NO!")
        fileName = folder + f"team{i}.txt"
        file = open(fileName,"w")
        print(file)     
        file.writelines(listData)
        file.writelines("\n")
        file.writelines(listData2)
        file.writelines("\n")
        file.writelines(listData)
        file.close  