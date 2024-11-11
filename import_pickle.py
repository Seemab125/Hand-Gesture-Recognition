import pickle

# Load the data from the pickle file
with open('data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

# Print keys and lengths of the data for verification
print("Keys in data_dict:", data_dict.keys())
print("Length of data:", len(data_dict['data']))

# Check if all entries are lists of equal length (replace expected_length with your expected value)
expected_length = 42  # Replace this with the expected length (depends on how many landmarks you're using)

for i, entry in enumerate(data_dict['data']):
    if not isinstance(entry, list) or len(entry) != expected_length:
        print(f"Entry {i} has a problem: {entry}")

# If there are issues, filter out invalid entries
filtered_data = [entry for entry in data_dict['data'] if isinstance(entry, list) and len(entry) == expected_length]
filtered_labels = [label for i, label in enumerate(data_dict['labels']) if isinstance(data_dict['data'][i], list) and len(data_dict['data'][i]) == expected_length]

# Save the cleaned data
with open('cleaned_data.pickle', 'wb') as f:
    pickle.dump({'data': filtered_data, 'labels': filtered_labels}, f)

print("Filtered data and labels saved to cleaned_data.pickle.")