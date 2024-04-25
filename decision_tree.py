import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def read_and_train(csv_file, output_file):
    # 读取CSV文件
    data = pd.read_csv(csv_file)
    # 提取特征数据和标签
    X = data.iloc[:, 1:-1].values  # 提取除了最后一列以外的所有列作为特征数据
    y = data.iloc[:, -1].values  # 提取最后一列作为标签

    # 将数据集分为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 构建决策树模型
    clf = DecisionTreeClassifier()

    # 在训练集上训练模型
    clf.fit(X_train, y_train)

    # 在测试集上进行预测
    y_pred = clf.predict(X_test)

    # 计算模型的准确性
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # 计算混淆矩阵
    conf_matrix = confusion_matrix(y_test, y_pred)

    # 绘制混淆矩阵热图
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

    # 将准确率写入到指定文件中
    with open(output_file, 'a') as f:
        f.write(f"Accuracy: {accuracy}\n")


# 让用户选择读取单个文件还是多个文件
choice = input("Enter '1' to read a single file, '2' to read multiple files: ")

if choice == '1':
    csv_file = input("Please enter the location and name of the csv file: ")
    output_file = input("Please enter the location and name of the output file: ")
    read_and_train(csv_file, output_file)
elif choice == '2':
    csv_file = input("Please enter the location and Prefix (without '_number') of the csv file: ")
    output_file = input("Please enter the location and name of the output file: ")
    for i in range(10):
        read_and_train(f'{csv_file}_{i}.csv', output_file)
else:
    print("Invalid choice. Please enter '1' or '2'.")