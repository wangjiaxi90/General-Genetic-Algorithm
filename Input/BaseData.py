# 所有数据类型需要遵从的数据规范
from dataclasses import dataclass


@dataclass
class BaseData:
    def add_range(self, **kwargs):
        pass

    def show_range(self):
        pass

    def get_data(self):
        pass
