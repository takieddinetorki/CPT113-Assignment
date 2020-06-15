#import the required modules
import numpy as np
from statistics import mode
import matplotlib.pyplot as plt

calorie = [1417, 1611, 1483, 1651, 1333, 1368, 1359, #CY
            1390, 1381,  652, 1390,  352, 1381, 1390, #Taki
            1060, 1205 ,1210 ,1020,  940,  880,  940, #Fasihah
            1701,1170.5,1627.5,2456,1221.5,1294,1044, #Islahiah
             934, 1095, 1196, 1310,  980,  984, 1249] #Atifah

print("Maximum calorie intake:",max(calorie))

print("\nMinimum calorie intake:",min(calorie))

print("\nMode calorie intake:", mode(calorie))

print("\nFrequency of mode:",calorie.count(mode(calorie)))

print("\nMean calorie intake:", np.mean(calorie))

print("\nVariance:",np.var(calorie))

print("\nStandard deviation:",np.std(calorie))

plt.title('Boxplot for calorie intake') 
plt.boxplot(calorie)
plt.show()

plt.title('Histogram for calorie intake') 
plt.hist(calorie)
plt.show()
