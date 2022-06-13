#
# from modules import *
# from MyDataset import MyDataset
#
#
#
# root_file = 'E:/competion/jitu/low-resolution/'
# dataloader = DataLoader(MyDataset(root_path=root_file,balanced = True,balanced_num=200),batch_size = 6,image_size=(256,256),shuffle = True)
# for X_trains,labels in dataloader:
#     print(X_trains.shape, labels.shape)
#     break

# root_file = '/root/datapath/'
# train_file_paths, val_file_paths = Dataset.splitTrainAndTest(root_path=root_file,split_ratio=0.8,save_path="/root/.json")
# dataset = Dataset(root_path=root_file,balanced = False)
# dataset.setAllFilePaths(train_file_paths)
# dataloader = DataLoader(dataset,batch_size = 6,image_size=(256,256),shuffle = True)
# for X_trains,labels in dataloader:
#     print(X_trains.shape, labels.shape)
#
#
# dataset = Dataset(root_path=root_file,balanced = False,balanced_num=200)
# #train_file_paths, val_file_paths = MyDataset.splitTrainAndTest(root_file,0.8,"E:/test.json") #'F:/celeA HQ/'
#
#
# #dataset.setAllFilePaths(train_file_paths)#与balanceSample不可兼得
#
# # trains , labels = dataset.loader()
#
# dataloader = DataLoader(dataset,batch_size = 6,image_size=(256,256),shuffle = True)
#
# for X_trains,labels in dataloader:
#     # print(X_trains)
#     print(X_trains.shape, labels.shape)
#     break
#     #print(X_trains.shape,labels.shape)
#
#
# # print(dataset.category_to_label)

# def frange(start, stop, incre):
#
#     x = start
#     while x < stop:
#         yield x
#         x += incre
# l = list(frange(0, 4, 0.5))
# print(min(l), max(l))
# x = 123 - 12j
# print(x)


# import numpy as np
# a = np.array([[1,1,1],[1,1,1],[1,1,1],[1,1,1]])
# b = np.array([1,1,1])
# print(a - b)
# print((lambda x: (x+3)*5/2)(3))
# a = {'x':1,'y':2,'z':3}
# b = {'w':10,'x':11,'y':2}
# print(a.items() & b.items())
# import re
# text = 'Computer says "no." Phone says "yes."'
# str_pat = re.compile(r'\"(.*?)\"')
# print(str_pat.findall(text))
a = [1,1,2]
a.remove(1)
print(a + [0] * 0)
