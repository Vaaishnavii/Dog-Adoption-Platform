import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load the Expanded Dataset
df = pd.read_csv("D:\\S7\\Full Stack\\FINAL PROJECT\\final\\furevermate\\models\\data.csv")

# Step 2: Feature Encoding
features = ['Time Dedication', 'Living Space', 'Grooming', 'Children', 'Activity Level', 'Dog Size']
X = df[features]
y = df['Suitable Dog']

# One-Hot Encode Categorical Features
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')  # Added handle_unknown='ignore'
X_encoded = encoder.fit_transform(X)

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate the Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Step 6: Save the Model and Encoder
joblib.dump(model, "expanded_fixed_breeds_model.pkl")
joblib.dump(encoder, "expanded_fixed_breeds_encoder.pkl")

# Step 7: Predict Suitable Dog for New User Input
def predict_suitable_dog(user_input):
    # Load the Model and Encoder
    model = joblib.load("expanded_fixed_breeds_model.pkl")
    encoder = joblib.load("expanded_fixed_breeds_encoder.pkl")
    
    # Encode User Input
    user_data = encoder.transform([user_input])
    prediction = model.predict(user_data)
    return prediction[0]

# Example: Predict Suitable Dog for New User
new_user = ['3-4 hours', 'House with small yard', 'Yes', 'Yes, under 10 years old', 'Very active', 'Large']
predicted_dog = predict_suitable_dog(new_user)
print(f"Suitable Dog for the User: {predicted_dog}")
