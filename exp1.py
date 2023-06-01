total_banana = int(input("Total Bananas = "))
distance = int(input("Total Distance to cover = "))
load = int(input("Maximum load capacity = "))

banana_lost = 0
x = total_banana

for i in range(distance) :
    while x>0 :
        x-=load
        if x==1 :
            banana_lost-=1
        banana_lost+=2
    banana_lost-=1
    x=total_banana-banana_lost
    if x==0 :
        print("Not a single can be transferred")
        break
print("Total banana delivered = " + str(x))