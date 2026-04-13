from model import train_model

model = train_model()

print("🌱 GaiaNet Crop Recommendation System")

temp = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
soil = float(input("Enter soil moisture: "))

prediction = model.predict([[temp, humidity, soil]])

print("🌾 Recommended Crop:", prediction[0])