# Decision_Tree
Sample code on how to apply Decision tree
Decision trees are versatile and popular machine learning models that can be used for both classification and regression tasks. They are non-parametric models that learn simple decision rules based on the input features to make predictions.

The theory behind decision trees can be explained as follows:

Structure:
A decision tree is a hierarchical structure consisting of internal nodes, branches, and leaf nodes. Each internal node represents a decision based on a specific feature or attribute, and each branch represents the possible outcomes of that decision. The leaf nodes represent the final predicted outcome or class.

Splitting Criterion:
To build a decision tree, a splitting criterion is used to determine the optimal feature and threshold for each internal node. The most common splitting criteria include Gini impurity and information gain. Gini impurity measures the probability of incorrectly classifying a randomly chosen element in a node, while information gain measures the reduction in entropy (or uncertainty) achieved by splitting based on a particular feature.

Recursive Partitioning:
The process of building a decision tree involves recursively partitioning the dataset based on the selected splitting criterion. At each internal node, the dataset is split into subsets based on the chosen feature and threshold. This process continues until a stopping criterion is met, such as reaching a maximum depth, achieving a minimum number of samples in each leaf, or when no further improvement in the splitting criterion can be obtained.

Prediction:
To make predictions using a decision tree, a new instance is passed through the tree starting from the root node. At each internal node, the decision rule based on the selected feature is evaluated, and the instance is directed to the appropriate child node based on the outcome. This process continues until a leaf node is reached, and the predicted outcome or class associated with that leaf node is assigned to the instance.

Handling Categorical and Continuous Features:
Decision trees can handle both categorical and continuous features. For categorical features, all possible values create separate branches. For continuous features, various techniques are used to determine the optimal split point, such as binary search or selecting a threshold that minimizes impurity or maximizes information gain.

Decision trees offer several advantages, including interpretability, easy visualization, and the ability to handle both numerical and categorical data. However, they can be prone to overfitting, especially when the tree becomes too complex or the training data has noise or outliers. To mitigate overfitting, techniques such as pruning, setting maximum tree depth, and using ensemble methods like random forests or gradient boosting can be employed.

In summary, decision trees are versatile models that make predictions based on a series of hierarchical decisions. They are widely used in various domains due to their simplicity, interpretability, and ability to handle both classification and regression tasks.




Gini Impurity:The Gini impurity is a measure of impurity or disorder used in decision tree algorithms, particularly for evaluating the quality of a split in a decision tree node. It quantifies the probability of incorrectly classifying a randomly chosen element in a dataset if it were randomly labeled according to the distribution of classes in that node.

The Gini impurity for a node is calculated by summing the probabilities of each class squared, subtracted from 1. Mathematically, for a node with K classes, the Gini impurity (Gini index) is given by the following formula:

Gini Index = 1 - (p1^2 + p2^2 + ... + pK^2)

where p1, p2, ..., pK represent the probabilities of each class in the node.

The Gini impurity ranges from 0 to 1, where a Gini impurity of 0 indicates a node that is purely homogeneous (all elements belong to the same class), and a Gini impurity of 1 indicates a node that is maximally impure (elements are evenly distributed among all classes).

In the context of decision trees, the Gini impurity is used to assess the quality of a split. When considering a potential split, the Gini impurity is calculated for each resulting child node, and the weighted average of the impurities is computed. The split that minimizes the Gini impurity or maximizes the information gain (reduction in impurity) is chosen as the optimal split for that node.

By repeatedly evaluating and selecting splits based on the Gini impurity, decision trees recursively partition the dataset, aiming to create pure and homogeneous leaf nodes that correspond to specific classes.

In summary, the Gini impurity is a measure of impurity or disorder used in decision tree algorithms to assess the quality of splits. It quantifies the probability of misclassifying elements in a node and guides the decision tree in finding the most informative splits for classification tasks.


Information gain:
Information gain is another measure used in decision tree algorithms to assess the quality of a split at a particular node. It quantifies the amount of information gained by splitting the data based on a certain attribute.

Information gain is based on the concept of entropy, which is a measure of the disorder or randomness in a set of data. In the context of decision trees, entropy is calculated for a given node by considering the distribution of classes in that node. It measures the impurity of the node.

The formula for entropy is as follows:

Entropy = - (p1 * log2(p1) + p2 * log2(p2) + ... + pK * log2(pK))

where p1, p2, ..., pK represent the probabilities of each class in the node.

To calculate information gain, we compare the entropy of the parent node to the weighted average of the entropies of the child nodes resulting from a split. The information gain is the difference between the entropy of the parent node and the weighted average entropy of the child nodes.

The higher the information gain, the better the split, as it indicates a greater reduction in entropy and, therefore, more useful information gained from the split.

Decision tree algorithms use information gain as a criterion for selecting the best attribute to split the data at each node. The attribute with the highest information gain is chosen as the optimal attribute for the split.

By recursively evaluating information gain and selecting the attribute with the highest gain at each node, decision trees build a hierarchy of splits that leads to a final tree structure capable of making predictions on unseen data.

In summary, information gain is a measure used in decision tree algorithms to assess the quality of splits. It compares the entropy of the parent node with the average entropy of the child nodes resulting from a split, and the attribute with the highest information gain is selected as the optimal split attribute. Information gain helps decision trees find the most informative features for classification tasks.



Post-pruning and pre-pruning:
Post-pruning and pre-pruning are techniques used in decision tree algorithms to prevent overfitting and improve the generalization ability of the model. They involve strategies to control the growth of the decision tree or prune unnecessary branches.

Pre-pruning (Early stopping):
Pre-pruning, also known as early stopping, refers to stopping the growth of a decision tree before it reaches its full depth based on certain conditions or criteria. The tree is pruned during the construction phase itself, without considering the entire training dataset. Some common pre-pruning techniques include:

Setting a maximum depth for the tree: Limiting the depth of the tree prevents it from becoming too complex and overfitting the training data.
Specifying a minimum number of samples required to split a node: By setting a threshold on the minimum number of samples, it prevents further splits if the node contains a smaller number of instances, reducing the chances of overfitting.
Applying a minimum impurity decrease threshold: This criteria stops a split if the improvement in impurity (e.g., Gini impurity or information gain) is below a certain threshold, ensuring that only significant splits are considered.
Post-pruning (Cost complexity pruning):
Post-pruning, also known as cost complexity pruning or backward pruning, involves growing the decision tree to its full depth and then pruning the unnecessary branches afterward. It uses a validation dataset or a pruning criterion to evaluate the quality of each subtree and determine whether to keep or remove it. The most common technique for post-pruning is cost complexity pruning, which involves adding a cost complexity parameter (also known as alpha or complexity parameter) to control the trade-off between tree complexity and accuracy. A subtree with higher alpha value (more complex) may be pruned to improve generalization. Various algorithms, such as reduced error pruning and weakest link pruning, can be used for post-pruning.

Pre-pruning and post-pruning are complementary techniques, and their effectiveness can vary depending on the dataset and problem at hand. Pre-pruning can save computational resources by avoiding unnecessary growth of the tree, while post-pruning can improve accuracy by selectively removing branches that are not beneficial. Both techniques aim to strike a balance between model complexity and accuracy, helping decision trees generalize well to unseen data.





