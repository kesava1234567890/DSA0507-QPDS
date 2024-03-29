import matplotlib.pyplot as plt
x =['Java','Python','PHP','JS','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity,color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n"+"Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-', linewidth='0.5',color='red')
# Customize the minor grid
plt.grid(which='minor',linestyle=':', linewidth='0.5',color='black')
plt.show()
