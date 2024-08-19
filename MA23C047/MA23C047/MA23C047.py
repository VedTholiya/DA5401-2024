#Required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#importing image data
data = pd.read_csv("Cat data.csv")
np.array(data.iloc[0])
#plotting the image
plt.figure()
sns.scatterplot(x= data['X'], y = data['Y'])
#after 90 degree rotation
plt.figure(figsize=(4,6))
sns.scatterplot(x= data['Y'], y = data['X'])
plt.xlabel('X')
plt.ylabel('Y')
#2nd rotation
plt.figure()
sns.scatterplot(x=data['X'],y=data['Y'])
plt.gca().invert_yaxis()
plt.show()