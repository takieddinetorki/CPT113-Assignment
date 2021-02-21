import matplotlib.pyplot as plt
from scipy import stats

"Create a linear function of the linear regression to return the y-axis values of the linear regression"
def linear_func(slope,intercept,x):
    return slope * x + intercept

"Create a function to plot the linear regression graph"
def linear_regression(x,y):
    #Assign values to slope and intercept accroding to the values of x and y
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    #Calculate the y-axis values of the linear regression
    regression = [linear_func(slope,intercept,x) for x in x]
    #Plot the graph of y against x
    plt.scatter(x,y)
    #Plot the graph of linear regression
    plt.plot(x, regression)
    #Displat the graphs
    plt.show()

calorie = [10222,7936,7255,10514.5,7748]
weight = [47,80,46,85,63]
phy = [1869,1869,1869,1869,2040]

# Correlation between the calorie intakes and the weights of students
plt.title('Correlation between the calorie intakes and the weights of students')
plt.xlabel('Calories intake (kcal)')
plt.ylabel('Weight (kg)')
linear_regression(calorie, weight)

# Correlation between the physical activities and the weights of students
plt.title('Correlation between the physical activities and the weights of students')
plt.xlabel('Physical activity (kcal)')
plt.ylabel('Weight (kg)')
linear_regression(phy, weight)

# Correlation between the physical activities and the calorie intakes of students 
plt.title('Correlation between the physical activities and the calorie intakes of students')
plt.xlabel('Physical activity (kcal)')
plt.ylabel('Calorie intake (kcal)')
linear_regression(phy, calorie)
