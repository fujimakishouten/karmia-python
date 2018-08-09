# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



# Import modules
import random
import sys
from typing import Optional


class KarmiaUtilityRandom:
    def __init__(self, options: Optional[dict]={}):
        self.number = options.get("number", "0123456789")
        self.lower = options.get("lower", "abcdefghijklmnopqrstuvwxyz")
        self.upper = options.get("upper", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.special = options.get("special", "!\"#$%&\'()*+,_./:;<=>?@[\\]^_`{|}~")

        random.seed()

    def string(self, length: int, options: Optional[dict]={}):
        characters = ""
        result = ""

        number = options.get("number", None)
        if number is not None:
            characters = characters + number if isinstance(number, str) else self.number

        lower = options.get("lower", None)
        if lower is not None:
            characters = characters + lower if isinstance(lower, str) else self.lower

        upper = options.get("upper", None)
        if lower is not None:
            characters = characters + upper if isinstance(upper, str) else self.upper

        special = options.get("special", None)
        if special is not None:
            characters = characters + special if isinstance(special, str) else self.special

        if len(characters) < 1:
            raise RuntimeError("")

        for i in range(length):
            result = result + characters[random.randint(0, len(characters))]

        return result

    def integer(self, min: int=0, max: int=sys.maxsize):
        return random.randint(min, max)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
