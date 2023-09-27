import pandas as pd 

class DataFrame:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.len = len(data)
            self.data = {col:data[col] for col in data.columns}

        #self.at = self.__getitem__

    def __getitem__(self, args):
        index, columns = args
        if isinstance(columns, str):
            return self.data[columns][index]


    def __setitem__(self, index, value):
        self.data[index] = value

    def __repr__(self):
        return repr(self.data)
    
    def __len__(self):
        return self.len

    @property
    def at(self):
        return at(self)


class at:
    def __init__(self, main):
        self.main = main
    def __getitem__(self, value):
        return self.main[value]
    
    
    
class DataFrame2:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.len = len(data)
            self.data = {col:data[col] for col in data.columns}
            
    def at(self, index, column):
        return self.data[column][index]
