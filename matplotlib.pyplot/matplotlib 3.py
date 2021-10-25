#make a piechart with 6 of your daily life activities along with
#no of hours spend doing it  and label each one accordingly
import matplotlib.pyplot as plt
import numpy as np
x=np.array([9,8,2,1,2,2])
labelss=["sleep","study","enjoy","workout","school work","reading"]
plt.pie(x,labels=labelss)
plt.show()