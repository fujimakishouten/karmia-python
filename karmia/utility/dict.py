# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



# Import modules
from typing import Any, Union
from functools import reduce


class KarmiaUtilityDict:
    def is_dict(self, value: Any) -> bool:
        """
        Check if value is an instance of Object

        :param Any value:
        :rtype bool:
        """
        return isinstance(value, dict)

    def flip(self, value: dict) -> dict:
        """
        Get object that exchanges key with their value

        :param value:
        :return:
        """
        return {value[property]: property for property in value.keys()}

    def merge(self, value1: dict, value2: dict) -> dict:
        """
        Recursively merge dicts

        :param dict value1:
        :param dict value2:
        :rtype: dict
        """
        def assign(collection: dict, key: str) -> dict:
            """
            Assign parameters

            :param dict collection:
            :param str key:
            :rtype: dict
            """
            if key in collection:
                if isinstance(collection[key], dict):
                    if isinstance(value2[key], dict):
                        collection[key] = self.merge(collection[key], value2[key])

                        return collection
            collection[key] = value2[key]

            return collection

        return reduce(assign, list(value2.keys()), value1)

    def merge_properties(self, value1: dict, value2: dict) -> dict:
        """
        Alias to merge

        :param dict value1:
        :param dict value2:
        :rtype: dict
        """
        return self.merge(value1, value2)

    def remove(self, value: dict, properties: Union[list, str, None]) -> dict:
        """
        Remove property from dict

        :param dict value:
        :param list|str properties:
        :return:
        """
        def pop(collection: dict, key: str) -> dict:
            if key in properties:
                return collection

            collection[key] = value[key]
            if isinstance(collection[key], dict):
                collection[key] = self.remove(collection[key], properties)

            return collection

        properties = properties or []
        properties = properties if isinstance(properties, list) else [properties]

        return reduce(pop, list(value.keys()), {})

    def remove_properties(self, value: dict, properties: Union[list, str, None]) -> dict:
        """
        Alias to remove

        :param dict value:
        :param list|str properties:
        :return:
        """
        return self.remove(value, properties)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
