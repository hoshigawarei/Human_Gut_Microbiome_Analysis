
# Human Gut Microbiome Analysis
This is a Python-based project for analyzing the gut microbiota of different populations. Its aim is to analyze the distribution of gut microbiota content among various populations and to classify populations using machine learning based on gut microbiota.
## Prerequisites

Before you continue, ensure you have met the following requirements:

* You have installed Python 3.9 or a higher version.
* We recommend using the Windows operating system. MacOS and Linux systems have not been tested yet, and compatibility issues may arise.

## How to Install this Project
### 1. Clone this project to your local machine

```
git clone https://github.com/hoshigawarei/MSM.git
```
### 2. Install the required libraries
Libraries required to run `class.py` and `query.py`: pandas

```
pip install pandas
pip install openpyxl
```
Libraries required to run `draw.py`: openpyxl, numpy, matplotlib

```
pip install openpyxl
pip install numpy
pip install matplotlib
```
Libraries required to run `random_select.py`: pandas, random

```
pip install pandas
pip install random
```
Libraries required to run `logistic_regression.py`, `svm.py`, `decision_tree.py`, `random_forest.py`, and `gradient_boosting_trees.py`: pandas, matplotlib, seaborn, scikit-learn

```
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
```
Libraries required to run `deep_learning.py`: pandas, matplotlib, seaborn, scikit-learn, TensorFlow, Keras
```
pip install pandas
pip install matplotlib
pip install seaborn
pip install scikit-learn
pip install tensorflow
pip install keras
```
##  Usage Instructions
### 1. Query bacteria names based on line numbers
**Usage Instructions for `query.py`**


**Input:** Path to the Excel file containing the target bacteria species, and the line number.

**Output:** The name of the target bacteria species.

**Example Usage (Using data.xlsx from the project directory):**

```
python query.py
path_to_excel_file.xlsx   // input\data.xlsx
line_number   //12  
line_number   //34 
...
n      //Input 'n' to exit the program
```
Replace `path_to_excel_file.xlsx `with the actual path to your Excel file and`line_number ` with the specific line number where the target bacteria species is located.
 
### 2.  Analyze the distribution of gut microbiota content among various populations
**Required Python Files: `classify.py`, `draw.py`**

#### (1) classify.py:

**Input**: Path to the Excel file needing classification; Path to the .txt file containing classification guidelines; Path to save the new Excel file.

**Output**: Excel file classified according to the guidelines.

**Usage Example (Using `data.xlsx`, `MSM_batch1.txt` from the project directory):**

```
python classify.py
path_to_excel_file.xlsx   //input\data.xlsx 
path_to_classification_guidelines.txt   //input\MSM_batch1.txt 
path_to_save_new_excel_file.xlsx  //output\MSM_batch1.xlsx 
```

Replace `path_to_excel_file.xlsx` with the actual path to your Excel file, `path_to_classification_guidelines.txt` with the path to the .txt file containing classification guidelines, and `path_to_save_new_excel_file.xlsx` with the desired path to save the new Excel file.


#### (2) draw.py:

**Input**: Path to the Excel file for analysis, or input 'AM' to display the index x of 'Mat[x]'.

**Output**: Visualized analysis results; a .txt file storing detailed analysis results.

**Usage Example (Using `MSM_b1` from the project directory)**:
```
python draw.py
path_to_excel_file.xlsx    //input\MSM_batch1.xlsx
path_to_saved_txt_file.txt    //output\detailed_information.txt
```

Or:

```
python draw.py 
AM
```

Replace `path_to_excel_file.xlsx` with the actual path to your Excel file.Then, replace `path_to_saved_txt_file.txt` with the actual path that you want to save the detailed information.


**Explanation of Output:**

* Input 'AM'
  * Output:
  \
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/1051850dcfdc4b36bb8d346da5466cab.png#pic_center)
\
The numbers in the squares represent the index of Mat."

* Input the address of the Excel file for analysis:
  * Output:
  
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/22eb06a11f95435ab99c580eda4fe4bb.png#pic_center)
\
X-axis represents: Proportion of a certain type of bacteria in the human intestinal flora.Y-axis represents: Proportion of patients carrying a certain type of bacteria in the overall population.The number in each square represents the number of bacterial species in that region.
\
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/6d5543758000417584eb7c2250e629d8.png#pic_center)
\
The `mat_output` stores the specific line numbers containing bacterial species in each Mat (which can be converted into the names of the bacterial species using `query.py`).

### 3. Machine Learning: Classifying populations based on microbiome data
#### (0) Data Preparation

A CSV table containing data is required, with the first column being sample IDs, the last column being labels, and the first row being the names of various bacterial species (if the original data table has sample IDs in the first row and bacterial species names in the first column, you can transpose it in Excel first).

Run `random_select.py` to randomly select n rows within the specified range and put them into a new table. The aim is to select an equal number of samples from each population to avoid the influence of population size ratio on the training results.

**Input**: Path to the CSV file containing the data to be randomly selected.

**Output**: Ten sub-CSV files after random selection.

**Usage Example (Using `all.csv` from the project directory)**:

```
py random_select.py
path_to_csv_file.csv     //input\all.csv 
2   //The starting number of rows for the x th group of people to filter
159   //The ending number of rows for the x th group of people to filter
31   //The number n of rows to be filtered out for the x th category of people
160   //The starting number of rows for the x th group of people to filter
191   //The ending number of rows for the x th group of people to filter
31   //The number n of rows to be filtered out for the x th category of people
-1    //Enter -1 to stop
path_to_saved_sub-csv_file.csv   //output\t_all  
```
Replace `path_to_csv_file.csv` with the actual path to your CSV file, and replace `path_to_saved_sub-csv_file.csv` with the actual path you want to save your ten sub-CSV file.
#### (1) Logistic Regression
**Required Python file:** `logistic_regression.py`

Using the model `LogisticRegression()` for classification through reinforcement learning.

**Input:** Select mode, "1" for analyzing a single file, "2" for batch analysis of files; Input the file address and name (excluding the prefix '_number').

**Output:** Accuracy of the classification results and confusion matrix.

**Usage Example (Using `all.csv` and `t_all_{i}` for `i` in the range [0, 9] from the project directory):**
* Analyzing a single file:
```
python logistic_regression.py
1   //mode
path_to_csv_file.csv    //input\all.csv  
path_to_save_accuracy_file    //output\a1
```
Replace `path_to_csv_file.csv` with the actual path to your CSV file, and replace `path_to_save_accuracy_file` with the actual path of the file you want to save your accuracy data.

*  Analyzing batch of files:
```
python logistic_regression.py
2    //mode
path_to_csv_file.csv     //input\t_all    //Input the file path and the prefix without '_number'.
path_to_save_accuracy_file    //output\a2
```
Replace `path_to_csv_file.csv` with the actual path to your CSV file and prefix without '_number', and replace `path_to_save_accuracy_file` with the actual path of the file you want to save your accuracy data.

Subsequent calls to other machine learning programs will be similar, requiring only modifications to the program names being called.
#### (2) Support Vector Machines, SVM
**Required Python file:** `svm.py`

Using the model `SVC(kernel="rbf", gamma=0.5, C=1.0)` for classification through reinforcement learning.

 #### (3)Decision Tree
**Required Python file:** `decision_tree.py`

Using the model `DecisionTreeClassifier()` for classification through reinforcement learning.

 #### (4) Random Forest
**Required Python file:** `random_forest.py`

Using the model `RandomForestClassifier(n_estimators=100, random_state=42)` for classification through reinforcement learning.

 #### (5) Gradient Boosting Trees
**Required Python file:** `gradient_boosting_trees.py`

Using the model `GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)` for classification through reinforcement learning.

 #### (6) Deep Learning
**Required Python file:** `deep_learning.py`

Using the model:
```
 models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(num_features,)),
    layers.Dropout(0.5),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])
```
for classification through reinforcement learning.
