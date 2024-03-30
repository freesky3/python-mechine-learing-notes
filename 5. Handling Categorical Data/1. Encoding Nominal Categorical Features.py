# Import libraries
import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
# Create feature
feature = np.array([["Texas"],
["California"],
["Texas"],
["Delaware"],
["Texas"]])
# Create one-hot encoder
one_hot = LabelBinarizer()
# One-hot encode feature
print(one_hot.fit_transform(feature))

# View feature classes
print(one_hot.classes_)

# Import library
import pandas as pd
# Create dummy variables from feature
print(pd.get_dummies(feature[:,0]))

print("{:=^50}".format("Split Line"))

# Create multiclass feature
multiclass_feature = [("Texas", "Florida"),
("California", "Alabama"),
("Texas", "Florida"),
("Delware", "Florida"),
("Texas", "Alabama")]
# Create multiclass one-hot encoder
one_hot_multiclass = MultiLabelBinarizer()
# One-hot encode multiclass feature
print(one_hot_multiclass.fit_transform(multiclass_feature))
# View classes
print(one_hot_multiclass.classes_)