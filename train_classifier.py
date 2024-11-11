import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import numpy as np

# Load data
data_dict = pickle.load(open('./cleaned_data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize RandomForestClassifier model
model = RandomForestClassifier()

# Train the model
model.fit(x_train, y_train)

# Predict on test data
y_predict = model.predict(x_test)

# Calculate scores
score = accuracy_score(y_predict, y_test)
score2 = precision_score(y_predict, y_test, average='macro')  # Using 'macro' for multiclass
score3 = recall_score(y_predict, y_test, average='macro')     # Using 'macro' for multiclass

# Print results
print('{}% accuracy of samples were classified correctly'.format(score * 100))
print('{}% precision of samples were classified correctly'.format(score2 * 100))
print('{}% recall of samples were classified correctly'.format(score3 * 100))

# Print classification report
print("Classification_report:\n", classification_report(y_test, y_predict))

# Save the model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)