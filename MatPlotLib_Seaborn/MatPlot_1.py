import matplotlib.pyplot as plt
import numpy as np

plt.style.use("fivethirtyeight")
dev_x = np.arange(25,36)
dev_y = range(38500,78650,3650)
python_y = range(38500,95150,5150)
width = 0.25

plt.bar(dev_x,dev_y,width=width,label="All Devs")
plt.bar(dev_x+width,python_y,width=width,label="Python Devs")
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title("Salaries for developers by age (USD)")
plt.tight_layout()
plt.legend()
plt.show()