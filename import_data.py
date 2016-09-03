import pandas as pd 
import math

data = pd.read_csv("./test.csv")

#lets fill in empty age fields with 29.7 the avergage age

for index, value in enumerate(data["Age"]):
	if math.isnan(value):
		data["Age"][index] = 29.7

# print data.info()

#lets drop the cabin column
data.drop("Cabin", axis=1, inplace=True)

data.drop("PassengerId", axis=1, inplace=True)
# print data.info()

#drop the two rows where this is not a field for embarked
data = data[pd.notnull(data['Embarked'])]
# print data.info()

#export modified data frame as cleaned.csv
data.to_csv("clean.csv")




