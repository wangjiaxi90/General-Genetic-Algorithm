# 所有数据类型需要遵从的数据规范
from dataclasses import dataclass


@dataclass
class BaseData:
    def add_range(self):
        pass

    def show_range(self):
        pass

    def delete_range(self, index: int):
        pass

    def get_data(self):
        pass
