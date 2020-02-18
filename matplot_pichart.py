import matplotlib.pyplot as mp

weeks = [3,2,4,2,6]
running = [1,3,5,12,14]
dancing = [1,2,3,5,4]
swimming = [3,4,5,6,7]
drawing = [9,2,3,4,13]
slices = [3,23,32,34]

activities = ['running', 'dancing', 'swimming', 'drawing']
cols = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

mp.pie(slices, labels=activities, colors=cols, startangle=80, 
       shadow=True, explode=(0,0.1,0,0), autopct='%1.1f%%')
mp.title('Pie Chart')
mp.show()
