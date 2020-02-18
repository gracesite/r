import matplotlib.pyplot as mp

arr1, arr2 = [1,3,5,7,9], [40,30,60,70,10]
mp.bar(arr1,arr2,label="car", width=0.8)
mp.legend()
mp.legend()
mp.xlabel('Days')
mp.ylabel('distance (km)')
mp.title('My bar')
mp.show()
