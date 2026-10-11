print("===========================================================")
print('                  WELCOME TO RIDE BUILDER            ')
print("===========================================================")

print("PLS CHOOSE-1=BIKE AND 2=CAR")

choice=int(input('enter 1/2:'))

if choice==1:
    print("1=scooty and 2=mountain bike")
    bike=int(input('enter 1/2:'))
    if bike==1:
        print('scooty-80km/h')
    else:
        print("mountain bike-40km/h")    
elif choice==2:
    print("1=sedan and 2=SUV")
    car=int(input('enter 1/2:'))
    if car==1:
        print("sedan-5 passengers-family trips")
    else:
        print('SUV-7 PASSENGERS-ROAD ADVENTURES')    
else:
    print("INVALID CHOICE,choose 1/2")        

print("===========================================================")
print('                 CUSTOM RIDE IS READY!                     ')
print("===========================================================")