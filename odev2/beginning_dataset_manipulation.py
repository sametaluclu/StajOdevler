import pandas as pd

data = pd.read_csv(r"C:/Users/azate/PycharmProjects/project-1/odev2/Iris.csv",)

data.loc[data['species'] == 'Iris-setosa', 'species'] = 'apple'
data.loc[data['species'] == 'Iris-versicolor', 'species'] = 'cherry'
data.loc[data['species'] == 'Iris-virginica', 'species'] = 'blueberry'

data.to_excel(r"C:/Users/azate/PycharmProjects/project-1/odev2/Dataset.xlsx")