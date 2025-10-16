import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def generate_model():
  data = pd.read_csv('./data/Fish.csv')

  X = data.drop('Species', axis=1)  # Features
  y = data['Species']  # Target variable

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  y_pred = model.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)
  print(f'Accuracy: {accuracy}')

  new_data = pd.DataFrame({'Weight': [300], 'Length1': [25], 'Length2': [27], 'Length3': [32], 'Height': [13], 'Width': [4.5]})
  prediction = model.predict(new_data)
  print(f'Predicted Species: {prediction}')

  joblib.dump(model, 'fish_classification.pkl')


if __name__ == '__main__':
    generate_model()