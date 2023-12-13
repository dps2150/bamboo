import pandas as pd
import copy
import sys


# BAMBOO DATA FRAME

class DataFrame():
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data.to_dict('list')  # {col:data[col] for col in data.columns}
            self.len = len(data)
        elif isinstance(data, dict):
            self.data = copy.deepcopy(data)
            self.len = len(data[next(iter(data.keys()))])

    def __getitem__(self, value):
        # to select multiple columns ex: df[out_columns], 400ns add, can be removed if col selection is extracted
        if isinstance(value, list):
            return pd.DataFrame({key:self.data[key] for key in self.data.keys() & set(value)})
        return self.data[value]

    def __setitem__(self, args, value):
        if isinstance(args, list):
            if isinstance(value, list) or isinstance(value, tuple):
                if len(args) == len(value):
                    for i in range(len(args)):
                        self.data[args[i]] = [value[i]] * self.len
                else:
                    # todo :: handle error
                    return 'Column and Values need to be the same length, please check your number and dial again'
            else:
                for i in range(len(args)):
                    self.data[args[i]] = [value] * self.len

        else:
            if isinstance(value, list):
                if len(value) == self.len:
                    self.data[args] = value
                else:
                    # TODO :: handle error
                    print(f'ERROR: values need to be same len as dataframe: {self.len} rows')
                    return
            else:
                self.data[args] = [value] * self.len

    def __repr__(self):

        return 'Please Develop in Pandas DataFrame'

    def __len__(self):
        return self.len

    def reset_index(self, drop):
        # dummy function to match pandas :: can utilize on defined index column if needed in future
        return self

    @property
    def columns(self):
        return list(self.data.keys())

    @property
    def at(self):
        return AT(self)

    @property
    def loc(self):
        return LOC(self)

    @property
    def unique(self):
        return set(self.data)

    def to_pd(self):
        return pd.DataFrame(self.data)


class AT:
    def __init__(self, a):
        self.a = a

    def __getitem__(self, args):
        index, col = args
        return self.a[col][index]

    def __setitem__(self, args, value):
        index, col = args
        self.a[col][index] = value


class LOC:
    def __init__(self, a):
        self.a = a

    def __getitem__(self, args):
        index_s, col = args
        return self.a[col][index_s]

    def __setitem__(self, args, value):
        if isinstance(args, slice):
            for i in range(args.start, args.stop):
                self.a[col][i] = value
        else:
            index, col = args
            self.a[col][index] = value

    # TODO :: add in slice set and multi
