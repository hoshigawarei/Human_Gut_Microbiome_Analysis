import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def read_and_train(csv_file, output_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Extract feature data and labels
    X = data.iloc[:, 1:-1].values  # Extract all columns except the last one as feature data
    y = data.iloc[:, -1].values  # Extract the last column as labels

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build the gradient boosting tree model
    gbt = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

    # Train the model on the training set
    gbt.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = gbt.predict(X_test)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Calculate the confusion matrix
    conf_matrix = confusion_matrix(y_test, y_pred)

    # Plot the heatmap of the confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

    # Write the accuracy to the specified file
    with open(output_file, 'a') as f:
        f.write(f"Accuracy: {accuracy}\n")

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
