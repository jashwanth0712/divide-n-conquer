# divide-n-conquer
application to efficiently manage memory by storing and retrieving different parts of a dataset/file
# problem
- while dealing with real life datascience problems the Datasets can be very huge.
- In cases like that, the system you are currently working on might not have enough resourses to contain the whole data set pyshically at a time.
- If you've done some projects on deep learning you understand that we train the model with small amounts of data at a time, to improve processing speed and fine tune the parameters in between. we call it a **batch**.

# Solution 💡
### Dividing the Dataset into batches of smaller size
![alt text](https://cdn-icons-png.flaticon.com/512/179/179696.png)
# how we do 😎
- We upload the dataset by splitting the entire dataset into parts
- when user clicks recieve, one batch is sent at a time
- only after the first batch is completed the next batch is fetched
- during the process of fetching , the first batch is deleted in order to free the space

![alt text](https://raw.githubusercontent.com/jashwanth0712/divide-n-conquer/main/Photos/dnq_output.png)

# Use case 👨‍💻
Consider another scenario where you are applying a Deep Learning Model on a huge image dataset and you don't have enough memory to store the entire dataset, this problem can also be solved by using Divide And Conquer. The dataset can be divided into smaller chunks and stored in the blockchain and can be used to train the model by downloading and deleting different parts of the dataset

# How to Use 🤔
- Install the module 
- run `dividenconquer.upload()` to upload the dataset into web3.storage
- after uploading , click on the `dividenconquer.download_first()` to download the first batch of the dataset
- for the subsequent batches you can run `dividenconquer.download_next()`
- **NOTE** : these functions have to be called within the jupiter notebook while writing the ML model

# Challenges we ran into 
## synchronous download of batches
The main problem was the synchronous download of the data batch by batch, if the data was fetched after the previous one is completed, then the entire code would have some amount of empty time between batch 1 and batch2 
- to avoid this, we have started downloading half batch at a time thereby leaving the remaining half as a buffer either for the incoming next batch or the about-to-be-deleted batch
 ![qeueue](https://benoitpasquier.com/images/2020/03/queue-data-structure.png)

## Velo by wix
It was interesting to work with wix , but also time consuming since this was our first time with the platform,we were unable to handle few customizations for our website

##  incremental learning
Different problems include finding a proper classification algorithm that can perform [incremental learning](https://en.wikipedia.org/wiki/Incremental_learning) and also exploring Wix to create a website which proved to be pretty useful in the end
- We found that **SGDClassifier** can be used for incremental learning

## ipfs in python
we were unable to execute the store function in python , since the documentation only had js 
- created a js file that runs through the trigger made by the `main.py` file
