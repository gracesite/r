import matplotlib.pyplot as mp
from matplotlib import style

style.use('ggplot')
a = [5,7,12]
b = [11,15,16]

ab = [5,3,13]
cd = [4,14,8]
# plot a line of 3 points (5,11) (7,15) (12,16)
mp.plot(a,b, label='x coord', linewidth=2, color='red')
# plot a line of 3 points (5,4) (3,14) (13,8)
mp.plot(ab,cd, label='x coord', linewidth=2, color='blue')

mp.title('My Plot')
mp.ylabel('Y coord')
mp.xlabel('x coord')
mp.legend()
mp.show()

