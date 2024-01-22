<br /><br />
<div align="center">
<h1 align="center">Implementing a Decision Tree Algorithm for an Anime Dataset
</h1>
</div>
<br />
<br />

This project was implemented for the [Cmpe 480 - Introduction to Artificial Intelligence](https://www.cmpe.boun.edu.tr/tr/courses/cmpe480) course I took in the Fall 2023 semester at [Bogazici University](https://bogazici.edu.tr/en_US). 

## Assignment Description
Implement the decision tree learning algorithm with entropy. Run your algorithm in a dataset you download from the web. 
Apply 5-fold cross-validation. Submit a single PDF file that includes:
* Information about the dataset.
* Discuss the use of 5-fold cross-validation.
* Provide error plots for training, validation, and test datasets.
* Draw the final/best decision tree.
* Include your source code with comments.


## Implementation Details:

### Dataset Preparation
Initially, I loaded the dataset using the pandas library. Then, I applied some data preparation steps, such as removing certain data columns and converting some data columns to a more suitable data format.
For instance, for the `eps_avg_duration_in_min` data column, I clustered the episode durations into discrete values: 5, 15, 25, and 30.

### Representing the Nodes
I implemented a `NodeQuestion` class to store a question, which splits the dataset into two subsets. The class records the index of the corresponding data column and a threshold value.
Such a question for the integer data columns is in the following format: "Is eps_duration >= 25?", and for the string data columns: "Is source == Manga?". The `match` function of this class checks whether a certain data row gives the output `True` or `False` for the corresponding question. 

Moreover, I implemented a `DecisionTreeNode` to represent every single node of the tree. Nodes can be either a Decision or a Leaf Node. The field `is_leaf` determines the type of the Node.
A Decision Node includes a question (an instance of the class `NodeQuestion`), and two child nodes. A Leaf node classifies data. It contains a dictionary of the format `label -> count` in the `predictions` field.

### Building the Tree
Finally, the `DecisionTreeSolver` class consists of all the utility functions. It takes two parameters upon initialization:
* `min_samples_split`: determines the number of samples a leaf node can have in minimum. 
* `max_depth`: limits the depth of the tree.

The `train_decision_tree` function takes the training X and Y datasets and initiates an instance of the `DecisionTreeSolver` class, 
then calls the class's `fit` function. This function executes the `build_tree` function of the class and returns the root of the built tree.

### Applying 5-Fold Cross-Validation
K-fold cross-validation is a technique for evaluating predictive models. For this implementation, I took k = 5. 
I divided the dataset into 5 subsets and trained and evaluated the model 5 times, using a different fold as the validation set each time. 
Then, I took the best (aka highest accuracy) model out of the 5 I trained. 

## Report
The [report](https://github.com/ebrarkiziloglu/My-AI-Projects/blob/decision-tree/Decision-Tree-Algorithm/Cmpe480_Assignment4_report.pdf) elaborates on the dataset used and then explains the usage of 5-fold cross-validation. 
It also includes the error plots for training, validation, and test datasets, the best final decision tree, and the [source code](https://github.com/ebrarkiziloglu/My-AI-Projects/blob/decision-tree/Decision-Tree-Algorithm/Cmpe_480_Decision_Tree_Learning.ipynb).

## Best / Final Decision Tree
![tree](https://github.com/ebrarkiziloglu/My-AI-Projects/blob/main/Decision-Tree-Algorithm/decision-tree.jpg)
 
