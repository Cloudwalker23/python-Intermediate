import sys
import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([3,8,1,10])

#horizontal 
plt.barh(x,y,height=0.5)

#vertical 
#plt.bar(x,y,color="#087695")

#width with bar, height with barh
#plt.bar(x,y,color="#087695",width=0.5)

plt.show()



