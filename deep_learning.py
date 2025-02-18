import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from keras import layers, models
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def read_and_train(csv_file, output_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    # Extract feature data and labels
    X = data.iloc[:, 1:-1].values  # Extract all columns except the first and last one as feature data
    y = data.iloc[:, -1].values  # Extract the last column as labels

    # Split the dataset into training, validation, and testing sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Define the neural network model
    num_features = X_train.shape[1]
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(num_features,)),
        layers.Dropout(0.5),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    # Make predictions on the testing set
    y_pred_prob = model.predict(X_test)
    y_pred = (y_pred_prob > 0.5).astype(int)  # Convert probabilities to class labels

    # Calculate the confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Plot the heatmap of the confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

    # Evaluate the model
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print('Accuracy:', test_acc)

    # Write the accuracy to the specified file
    with open(output_file, 'a') as f:
        f.write(f"Accuracy: {test_acc}\n")

# Let the user choose to read a single file or multiple files
choice = input("Enter '1' to read a single file, '2' to read multiple files: ")

if choice == '1':
    csv_file = input("Please enter the location and name of the CSV file: ")
    output_file = input("Please enter the location and name of the output file: ")
    read_and_train(csv_file, output_file)
elif choice == '2':
    csv_file = input("Please enter the location and prefix (without '_number') of the CSV file: ")
    output_file = input("Please enter the location and name of the output file: ")
    for i in range(10):
        read_and_train(f'{csv_file}_{i}.csv', output_file)
else:
    print("Invalid choice. Please enter '1' or '2'.")
