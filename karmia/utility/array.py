# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



# Import modules
from typing import Any, Union


class KarmiaUtilityArray:
    def unique(self, values: list) -> list:
        """
        Removes duplicate values from an array

        :param list values:
        :rtype list:
        """
        return list(self.flip(values).keys())

    def count(self, values: list, item: Any) -> int:
        """
        Count item in list

        :param values:
        :param item:
        :rtype: int
        """
        return values.count(item)

    def range(self, start: int, stop: Union[int, None] = None, step: Union[int, None] = None) -> iter:
        """
        Get iterator of integer from start to end

        :param int start
        :param int|None stop:
        :param int|None step:
        :rtype: iter
        """
        if stop:
            return range(start, stop, step or 1)

        return range(0, start, 1)

    def flip(self, values: list) -> dict:
        """
        Get dict that exchanges index with their value

        :param list values:
        :rtype: dict
        """
        return {item: key for key, item in enumerate(values)}

    def intersection(self, values1: list, values2: list) -> list:
        """
        Get intersection of two arrays

        :param list values1:
        :param list values2:
        :rtype: list
        """
        items = self.flip(values2)

        return self.unique([v for v in values1 if v in items])


    def difference(self, values1: list, values2: list) -> list:
        """
        Get difference of two arrays

        :param list values1:
        :param list values2:
        :rtype: list
        """
        items = self.flip(self.intersection(values1, values2))

        return [v for v in values1 + values2 if v not in items]




# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
