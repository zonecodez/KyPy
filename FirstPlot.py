####################################LINEGRAPH###################################################
#import pyplot as plt from the matplotlib module
from matplotlib import pyplot as plt

#create variables to hold lists of data for x and y axis
years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.4,5979.6,10289.1,14958.4]

#create pyplot line chart
plt.plot(years, gdp, color = 'green', marker ='o', linestyle='solid')

#give chart title
plt.title('Nominal GDP')

#give x-axis title
plt.ylabel('Gross Domestic Product (GDP)')
#give y-axis title
plt.xlabel('Years')
#show chart
plt.show()
