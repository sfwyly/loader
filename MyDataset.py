
from modules import Dataset

class MyDataset(Dataset):

    def __init__(self, is_train = True,**kwargs):
        super(MyDataset,self).__init__(is_train =is_train,**kwargs)

    def processLabelStr(self,category_str) -> int:
        return int(category_str.split("-")[1][1:])
