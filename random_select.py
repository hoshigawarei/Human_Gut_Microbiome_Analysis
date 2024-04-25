import pandas as pd
import random

# 从原始CSV文件中加载数据
csv_file=input('Please enter the address of the csv file that needs to be processed:')
data = pd.read_csv(csv_file)
row = [int(0) for i in range(30)]
j=0;
while(1):
    row[j] = int(input(f'Please enter the starting number of rows for the {j/3}th group of people to filter(Enter -1 to stop):'))
    if(row[j]==-1):
        break;
    row[j+1] = int(input(f'Please enter the ending number of rows for the {j/3}th group of people to filter:'))
    row[j+2] = int(input(f'Please enter the number n of rows to be filtered out for the {j/3}th category of people:'))
    j=j+3;
j=j-3;
out_file = input('Please enter the path to save the sub-file:')
for i in range(10):
    new_data = pd.DataFrame()  # 创建一个空的 DataFrame 用于存储新的数据
    k = 0
    first_row = data.iloc[0]
    while k <= j:
        random_samples = random.sample(range(row[k], row[k + 1]), row[k + 2])
        selected_rows = data.iloc[random_samples]  # 从原始数据中选取随机行
        if k == 0:
            new_data = pd.concat([first_row.to_frame().T, selected_rows])  # 将第一行和选定的行连接起来
        elif k > 0:
            new_data = pd.concat([new_data, selected_rows])  # 将新的选定的行连接到已有的数据后面
        k += 3
        # 保存合并后的数据到新的CSV文件中
    new_data.to_csv(f"{out_file}_{i}.csv", index=False)


