# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



# Import modules
import re
import regex
import unicodedata
from typing import Any, Optional, Pattern, Union
from functools import reduce

# Variables
others = regex.compile("\\p{C}", regex.IGNORECASE|regex.UNICODE)


class KarmiaUtilityString:
    def is_string(self, value: Any) -> bool:
        """
        Check is string

        :param value:
        :return:
        """
        return isinstance(value, str)

    def strip(self, string: str, mask_characters=" \t\n\r\0\x0B") -> str:
        """
        Strip left string

        :param str string:
        :param str mask_characters: default " \t\n\r\0\x0B"
        :rtype str
        """
        return self.rstrip(self.lstrip(string, mask_characters), mask_characters)

    def lstrip(self, string: str, mask_characters=" \t\n\r\0\x0B") -> str:
        """
        Strip left string

        :param str string:
        :param str mask_characters: default " \t\n\r\0\x0B"
        :rtype str
        """
        return regex.sub("^[{0}]+".format(mask_characters), "", string)

    def rstrip(self, string: str, mask_characters=" \t\n\r\0\x0B") -> str:
        """
        Strip right string

        :param str string:
        :param str mask_characters: default " \t\n\r\0\x0B"
        :rtype str
        """
        return regex.sub("[{0}]+$".format(mask_characters), "", string)

    def trim(self, string: str, mask_characters=" \t\n\r\0\x0B") -> str:
        """
        Alias to strip

        :param str string:
        :param str mask_characters: default " \t\n\r\0\x0B"
        :rtype str
        """
        return self.strip(string, mask_characters)

    def ltrim(self, string: str, mask_characters=" \t\n\r\0\x0B") -> str:
        """
        Alias to lstrip

        :param str string:
        :param str mask_characters: default " \t\n\r\0\x0B"
        :rtype str
        """
        return self.lstrip(string, mask_characters)

    def rtrim(self, string: str, mask_characters=" \t\n\r\0\x0B") -> str:
        """
        Strip right string

        :param str string:
        :param str mask_characters: default " \t\n\r\0\x0B"
        :rtype str
        """
        return self.rstrip(string, mask_characters)

    def normalize(self, string: str, form="NFKC") -> str:
        lines = map(lambda s: regex.sub(others, "", s), regex.split("\r\n|\r|\n", string))

        return self.trim(unicodedata.normalize(form, "\n".join(lines)))

    def unquote(self, string: str) -> str:
        """
        Unquote string

        :param str string:
        :rtype str
        """
        if ((string.startswith("'") and string.endswith("'"))
                or (string.startswith('"') and string.endswith('"'))):

            return string[1:-1]

        return string

    def zfill(self, string: Union[int, str], width: int) -> str:
        """
        Pads string on the left with zeros

        :param int|str string:
        :param int width:
        :rtype: str
        """
        return str(string).zfill(width)

    def camelcase(self, string: str, capitalize: bool=False) -> str:
        """
        Convert from kebab-case/snake_case to camelCase

        :param str string:
        :param bool capitalize: default False
        :rtype: str
        """
        result = "".join(map(lambda s: s[0].upper() + s[1:], regex.split("[-_]", string)))
        if capitalize:
            return result[0].upper() + result[1:]

        return result[0].lower() + result[1:]

    def snakecase(self, string: str):
        """
        Convert from camelCase/kebab-case to snake_case

        :param str string:
        :rtype: str
        """
        result = string[0].lower() + string[1:].replace("-", "_")

        return regex.sub("([A-Z])", "_\\1", result).lower()

    def kebabcase(self, string: str):
        """
        Convert from camelCase/snake_case to kebab-case

        :param str string:
        :rtype: str
        """
        result = string[0].lower() + string[1:].replace("_", "-")

        return regex.sub("([A-Z])", "-\\1", result).lower()

    def parse(self, string: str,
              delimiter: Union[Pattern, str, None]="(,|,? )",
              separator: Union[Pattern, str, None]="=") -> dict:
        """
        Parse "key1=value1, key2=value2" formatted string

        :param str string:
        :param re|str delimiter: Default "(,|,? )"
        :param re|str separator: Default "="
        :rtype: dict
        """
        def _parse(collection: dict, parameter: str) -> dict:
            """
            Add key value to collection

            :param dict collection:
            :param str parameter:
            :rtype: dict
            """
            data = regex.split(separator, parameter, 2)
            key = self.unquote(self.strip(data[0]))
            collection[key] = self.unquote(self.strip(data[1])) if len(data) > 1 else key

            return collection

        if not string:
            return {}

        return reduce(_parse, regex.split(delimiter, string), {})

    def to_boolean(self, string: Any) -> bool:
        """
        Change from "true", "on", "1" to true and others to false

        :param str string:
        :rtype: bool
        """
        if self.is_string(string):
            return None is not regex.match("^(?i)(true|1|on)$", string)

        return bool(string)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
