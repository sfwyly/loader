# loader
A streaming frame for data preprocessing.

# Characters
+ Similar to the PyTorch statement
+ More simple procedure call
+ More flexible customize self code
+ More plenty of data processing methods

# Usage
## Statement

```
root_file = '/root/datapath/'
dataloader = DataLoader(Dataset(root_path=root_file,balanced = True,balanced_num=200),batch_size = 6,image_size=(256,256),shuffle = True)
for X_trains,labels in dataloader:
    print(X_trains.shape, labels.shape)
```

## Customize split dataset and transfer to Dataset

```
root_file = '/root/datapath/'
train_file_paths, val_file_paths = Dataset.splitTrainAndTest(root_path=root_file,split_ratio=0.8,save_path="/root/split.json")
dataset = Dataset(root_path=root_file,balanced = False)
dataset.setAllFilePaths(train_file_paths)
dataloader = DataLoader(dataset,batch_size = 6,image_size=(256,256),shuffle = True)
for X_trains,labels in dataloader:
    print(X_trains.shape, labels.shape)
```

## Customize label processing

```
class MyDataset(Dataset):

    def __init__(self, is_train = True,**kwargs):
        super(MyDataset,self).__init__(is_train =is_train,**kwargs)
    # override
    def processLabelStr(self,category_str) -> int:
        return int(category_str.split("-")[1][1:])
dataloader = DataLoader(MyDataset(root_path=root_file,balanced = True,balanced_num=200),batch_size = 6,image_size=(256,256),shuffle = True)
for X_trains,labels in dataloader:
    print(X_trains.shape, labels.shape)
```

## Video reading and customize split

