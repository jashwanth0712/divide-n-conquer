## Problem it solves
#### Often when working on machine learning or deep leaning models, you have to deal with large amounts of data. Some times the datasets might be as big as 500gb. In cases like that, the system you are currently working on might not have enough resourses to contain the whole data set pyshically at a time. If you've done some projects on deep learning you understand that we train the model with small amounts of data at a time, to improve processing speed and fine tune the parameters in between. we call it a batch. Even though we have a whole 500 gb dataset in the memory the training algorithm only uses the batch sized amount at a time. That means there is no point of storing the whole 500gb when we only need a batch sized amount at any single point of time.

#### This is the motivation of our problem statement. Why not just store only what we need i.e. one batch sized data at a time. Upload the whole dataset into the blockchain, divide the dataset into equal sized batches, Retrieve one batch at a time, pass the retreived batch into the training algorithm. Typically each batch takes some time while it's being processed. During that time we can download the subsequent batch from the blockchain and delete the previous batch from the memory and free that space.

#### Advantages of storing the dataset into a blockchain over conventional methods:
#### * Security of the data is ensured
#### * It's decentralised and no single entity can change the data
#### * A record is maintained of all changes done to the dataset

## Challenges we faced
#### * The process we are using to train the model ,using one batch one after another, is called incremental learning. This type is learning is not supported all models.Some models like KNN, SVM do not support this.
#### * 
