# 连续数据
import sys
from dataclasses import dataclass, field
from typing import List, Tuple, Set
import numpy as np

from Input.BaseData import BaseData


@dataclass
class ContinuousData(BaseData):
    """ 连续数据 """
    length: int = 0
    """ 当前区间个数 """
    range_set: Set[Tuple[float, float]] = field(default_factory=list)
    """ 区间默认左闭右闭 """

    def add_range(self, up: float = None, down: float = None, one_point: bool = False):
        """up是上限，down是下限 one_point代表是不是指的特定的一个点"""
        if up is None and down is None:
            # 抛异常
            pass
        if up is not None and down is not None:
            if down < up:
                # 抛异常
                pass
            else:
                self.range_set.add((up, down))
                self.length += 1
                return
        if up is None:
            if one_point:
                self.range_set.add((down, down))
            else:
                # 这里要加个警告 尽量不要这样做
                self.range_set.add((down, sys.float_info.max))
            self.length += 1
            return
        if down is None:
            if one_point:
                self.range_set.add((up, up))
            else:
                # 这里要加个警告 尽量不要这样做
                self.range_set.add((sys.float_info.min, up))
            self.length += 1

    def show_range(self):
        """ 输出当前范围列表 """
        print("length:", self.length)
        print(self.range_set)

    def get_data(self) -> float:
        """ 在区间内随机得到一个数据 TODO 这里应该有个默认精度问题"""
        random_range = np.random.choice(self.length)
        curr_range = list(self.range_set)[random_range]
        return np.random.uniform(curr_range[0], curr_range[1])
