from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def train_model():
    data = pd.read_csv("data.csv")

    X = data[["temperature", "humidity", "soil_moisture"]]
    y = data["crop"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model
