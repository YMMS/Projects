# Projects

+ **SVD-CV**: 通过图像的SVD，来解释特征值的含义: 发现取少量有限特征值最大的前几个分量就能获得与原图相近的图片。


<iframe height=555 width=888 src="./SVD-CV/timg.gif">

+ **Tennis-NaiveBayes**: `sklearn.naive_bayes` 在Tennis数据集上的示例

```
Method: BernoulliNB
Gold:  [1 1 0 0 0 1 0 1 0 0 0 0 0 1]
Pred:  [1 1 0 0 0 0 0 1 0 0 0 0 0 0]
Mean Accuracy:  0.8571428571428571


Method: GaussianNB
Gold:  [1 1 0 0 0 1 0 1 0 0 0 0 0 1]
Pred:  [1 1 0 0 0 0 0 1 0 0 0 0 0 1]
Mean Accuracy:  0.9285714285714286


Method: MultinomialNB
Gold:  [1 1 0 0 0 1 0 1 0 0 0 0 0 1]
Pred:  [1 1 0 0 0 0 0 1 0 0 0 0 0 0]
Mean Accuracy:  0.8571428571428571
```
