# -*- coding:utf-8 -*-

import os
import numpy as np

class TennisDataset():
    
    def __init__(self, dirpath="/home/yangming/Datasets/ToyDatasets/tennis"):
        self.dirpath = dirpath
        with open(os.path.join(dirpath, "train"), "r") as filer:
            for idx, line in enumerate(filer):
                attributes, values, label = self._line_parser(line)
                if idx == 0:
                    self.attributes = attributes
                    self.attribute_value_set_dict = dict([(attribute, set()) for attribute in attributes])
                    self.label_value_set = set()
                else:
                    assert attributes == self.attributes, "第{}行属性与首行属性个数不匹配!"
                self.label_value_set.add(label)
                for attribute, value in zip(attributes, values):
                    self.attribute_value_set_dict[attribute].add(value)
        label_value_set = list(self.label_value_set)
        self.label2index = dict(zip(label_value_set, range(len(label_value_set))))
        self.index2label = dict(zip(range(len(label_value_set)), label_value_set))
        self.attribute2vocab = {}
        for attribute in self.attribute_value_set_dict:
            value_set = list(self.attribute_value_set_dict[attribute])
            value2idx = dict(zip(value_set, range(len(value_set))))
            idx2value = dict(zip(range(len(value_set)), value_set))
            self.attribute2vocab[attribute] = [value2idx, idx2value]
        
    def __call__(self, mode="train"):
        X, Y = [], []
        with open(os.path.join(self.dirpath, mode), "r") as filer:
            for line in filer:
                attributes, values, label = self._line_parser(line)
                xl = []
                for attribute, value in zip(attributes, values):
                    xl.append(self.attribute2vocab[attribute][0][value])
                X.append(xl)
                Y.append(self.label2index[label])
        return np.asarray(X, dtype=np.int), np.asarray(Y, dtype=np.int)
                
    def _line_parser(self, line):
        items = line.strip().split(",")
        label = items[-1]
        attributes, values = zip(*[tuple(item.split("=")) for item in items[:-1]])
        return attributes, values, label
            
tennisdataset = TennisDataset()

if __name__ == "__main__":
    pass