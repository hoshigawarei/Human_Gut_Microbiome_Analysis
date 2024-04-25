import pandas as pd
from sklearn.model_selection import train_test_split
import keras
from keras import layers, models
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def read_and_train(csv_file, output_file):
    # 读取CSV文件
    data = pd.read_csv(csv_file)
    # 提取特征数据和标签
    X = data.iloc[:, 1:-1].values  # 提取除了第一列和最后一列以外的所有列作为特征数据
    y = data.iloc[:, -1].values  # 提取最后一列作为标签

    # 划分训练集、验证集和测试集
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # 定义神经网络模型
    num_features = X_train.shape[1]
    model = models.Sequential([
        layers.Dense(128, activation='relu', input_shape=(num_features,)),
        layers.Dropout(0.5),
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])

    # 编译模型
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # 训练模型
    history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    # 在测试集上进行预测
    y_pred_prob = model.predict(X_test)
    y_pred = (y_pred_prob > 0.5).astype(int)  # 将概率转换为类别标签

    # 计算混淆矩阵
    conf_matrix = confusion_matrix(y_test, y_pred)

    # 绘制混淆矩阵热图
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

    # 评估模型
    test_loss, test_acc = model.evaluate(X_test, y_test)
    print('Accuracy:', test_acc)


    # 将准确率写入到指定文件中
    with open(output_file, 'a') as f:
        f.write(f"Accuracy: {test_acc}\n")

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