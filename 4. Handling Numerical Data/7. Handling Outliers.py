# Load library
import pandas as pd
# Create DataFrame
houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]

# Filter observations
# 方法一放弃数据
print(houses[houses['Bathrooms'] < 20])

print("{:=^50s}".format("Split Line"))

# 方法二标记异常值特征值
# Load library
import numpy as np
# Create feature based on boolean condition
houses["Outlier"] = np.where(houses["Bathrooms"] < 20, 0, 1)
# Show data
print(houses)

print("{:=^50s}".format("Split Line"))

# 方法三变换特征降低异常值影响
# Log feature
houses["Log_Of_Square_Feet"] = [np.log(x) for x in houses["Square_Feet"]]
# Show data
print(houses)