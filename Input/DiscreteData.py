# 离散数据
import sys
from dataclasses import dataclass, field
from typing import Set
import numpy as np

from Input.BaseData import BaseData


@dataclass
class DiscreteData(BaseData):
    """ 离散数据 """
    length: int = 0
    """ 当前区间个数 """
    range_set: Set[float] = field(default_factory=list)
    """ 区间默认左闭右闭 """

    def add_range(self, first: float, second: float = None, pace: float = None):
        """ first代表第一个值 second代表第二个值 pace代表步长"""
        if second is None and first not in self.range_set:
            self.range_set.add(first)
            self.length += 1
        # TODO 正在构思这部分参数

    def show_range(self):
        """ 输出当前范围列表 """
        print("length:", self.length)
        print(self.range_set)

    def get_data(self) -> float:
        """ 在区间内随机得到一个数据 TODO 这里应该有个默认精度问题"""
        random_range = np.random.choice(self.length)
        return list(self.range_set)[random_range]
