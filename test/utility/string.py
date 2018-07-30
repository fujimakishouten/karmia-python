# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import unittest
from karmia.utility import KarmiaUtilityString


class TestKarmiaUtilityStringIsString(unittest.TestCase):
    def test_string(self):
        utility = KarmiaUtilityString()
        string = "Hello, world."

        self.assertEqual(utility.is_string(string), True)

    def test_number(self):
        utility = KarmiaUtilityString()
        number = 1

        self.assertEqual(utility.is_string(number), False)

    def test_dict(self):
        utility = KarmiaUtilityString()
        dictionaly = {}

        self.assertEqual(utility.is_string(dictionaly), False)


class TestKarmiaUtilityStringStrip(unittest.TestCase):
    def test_whitespace(self):
        utility = KarmiaUtilityString()
        string = 'Hello, world.'

        self.assertEqual(utility.strip("\t   {0}   \r\n".format(string)), string)

    def test_specified_character(self):
        utility = KarmiaUtilityString()

        self.assertEqual(utility.strip("abc", "bad"), "c")

    def test_strip_left_string(self):
        utility = KarmiaUtilityString()
        string = 'Hello, world.'

        self.assertEqual(utility.lstrip("\t   {0}   \r\n".format(string)), "{0}   \r\n".format(string))

    def test_strip_right_string(self):
        utility = KarmiaUtilityString()
        string = 'Hello, world.'

        self.assertEqual(utility.rstrip("\t   {0}   \r\n".format(string)), "\t   {0}".format(string))


class TestKarmiaUtilityStringTrim(unittest.TestCase):
    def test_whitespace(self):
        utility = KarmiaUtilityString()
        string = 'Hello, world.'

        self.assertEqual(utility.trim("\t   {0}   \r\n".format(string)), string)

    def test_specified_character(self):
        utility = KarmiaUtilityString()

        self.assertEqual(utility.trim("abc", "bad"), "c")

    def test_strip_left_string(self):
        utility = KarmiaUtilityString()
        string = 'Hello, world.'

        self.assertEqual(utility.ltrim("\t   {0}   \r\n".format(string)), "{0}   \r\n".format(string))

    def test_strip_right_string(self):
        utility = KarmiaUtilityString()
        string = 'Hello, world.'

        self.assertEqual(utility.rtrim("\t   {0}   \r\n".format(string)), "\t   {0}".format(string))

class TestKarmiaUtilityStringNormalize(unittest.TestCase):
    def test_normalize(self):
        utility = KarmiaUtilityString()
        string = "\u202b１２３\r\nＡＢＣ\rｄｅｆ\nｱｲｳｴｵｶﾞ"
        result = "123\nABC\ndef\nアイウエオガ"

        self.assertEqual(utility.normalize(string, "NFKC"), result)


class TestKarmiaUtilityStringUnquote(unittest.TestCase):
    def test_not_quoted(self):
        utility = KarmiaUtilityString()
        string = "Hello, world."

        self.assertEqual(utility.unquote(string), string)

    def test_single_quoted(self):
        utility = KarmiaUtilityString()
        string = "Hello, world."

        self.assertEqual(utility.unquote("'{0}'".format(string)), string)

    def test_double_quoted(self):
        utility = KarmiaUtilityString()
        string = "Hello, world."

        self.assertEqual(utility.unquote('"{0}"'.format(string)), string)

    def test_part_of_string(self):
        utility = KarmiaUtilityString()
        string = '"Hello", world.'

        self.assertEqual(utility.unquote(string), string)

    def test_unmatched(self):
        utility = KarmiaUtilityString()
        string = "'Hello, world." + '"'

        self.assertEqual(utility.unquote(string), string)


class TestKarmiaUtilityStringZfill(unittest.TestCase):
    def test_zfill(self):
        utility = KarmiaUtilityString()
        number = 1

        self.assertEqual(utility.zfill(number, 0), "1")
        self.assertEqual(utility.zfill(number, 1), "1")
        self.assertEqual(utility.zfill(number, 2), "01")
        self.assertEqual(utility.zfill(number, 3), "001")
        self.assertEqual(utility.zfill(number, 4), "0001")
        self.assertEqual(utility.zfill(number, 5), "00001")


class TestKarmiaUtilityStringCamelCase(unittest.TestCase):
    def test_from_snake_case(self):
        utility = KarmiaUtilityString()
        snake = 'snake_case_to_camel_case'
        camel = 'snakeCaseToCamelCase'

        self.assertEqual(utility.camelcase(snake), camel)
        self.assertEqual(utility.camelcase(snake, True), "{0}{1}".format(camel[0].upper(), camel[1:]))

    def test_from_kebab_case(self):
        utility = KarmiaUtilityString()
        kebab = 'kebab-case-to-camel-case'
        camel = 'kebabCaseToCamelCase'

        self.assertEqual(utility.camelcase(kebab), camel)
        self.assertEqual(utility.camelcase(kebab, True), "{0}{1}".format(camel[0].upper(), camel[1:]))


class TestKarmiaUtilityStringSnakeCase(unittest.TestCase):
    def test_from_camel_case(self):
        utility = KarmiaUtilityString()
        camel = 'camelCaseToSnakeCase'
        snake = 'camel_case_to_snake_case'

        self.assertEqual(utility.snakecase(camel), snake)

    def test_from_kebab_case(self):
        utility = KarmiaUtilityString()
        kebab = 'kebab-case-to-snake-case'
        snake = 'kebab_case_to_snake_case'

        self.assertEqual(utility.snakecase(kebab), snake)


class TestKarmiaUtilityStringKebabCase(unittest.TestCase):
    def test_from_camel_case(self):
        utility = KarmiaUtilityString()
        camel = 'camelCaseToKebabCase'
        kebab = 'camel-case-to-kebab-case'

        self.assertEqual(utility.kebabcase(camel), kebab)

    def test_from_kebab_case(self):
        utility = KarmiaUtilityString()
        snake = 'snake_case_to_kebab_case'
        kebab = 'snake-case-to-kebab-case'

        self.assertEqual(utility.kebabcase(snake), kebab)


class TestKarmiaUtilityStringParse(unittest.TestCase):
    def test_specified_delimiter(self):
        utility = KarmiaUtilityString()
        string = "key1=value1:key2=value2"
        result = utility.parse(string, ":")

        self.assertEqual(result["key1"], "value1")
        self.assertEqual(result["key2"], "value2")

    def test_specified_separator(self):
        utility = KarmiaUtilityString()
        string = "key1:value1 key2:value2"
        result = utility.parse(string, " ", ":")

        self.assertEqual(result["key1"], "value1")
        self.assertEqual(result["key2"], "value2")

    def test_include_single_quote(self):
        utility = KarmiaUtilityString()
        string = "key1=value1, key2=value2, key3=value'3"
        result = utility.parse(string)

        self.assertEqual(result["key1"], "value1")
        self.assertEqual(result["key2"], "value2")
        self.assertEqual(result["key3"], "value'3")

    def test_include_double_quote(self):
        utility = KarmiaUtilityString()
        string = 'key1=value1, key2=value2, key3=value"3'
        result = utility.parse(string)

        self.assertEqual(result["key1"], "value1")
        self.assertEqual(result["key2"], "value2")
        self.assertEqual(result["key3"], 'value"3')

    def test_empty_string(self):
        utility = KarmiaUtilityString()
        result = utility.parse("")

        self.assertDictEqual(result, {})

    def test_authorize_header(self):
        utility = KarmiaUtilityString()
        format = 'Digest username="{0}", realm="{1}", nonce="{2}", uri="{3}", ' \
                 + 'algorithm={4}, response="{5}", qop={6}, nc={7}, cnonce="{8}"'
        username = 'USER_NAME'
        realm = 'REALM'
        nonce = 'NONCE'
        uri = '/'
        algorithm = 'MD5'
        response = 'RESPONSE'
        qop = 'auth'
        nc = '00000001'
        cnonce = 'CNONCE'
        string = format.format(username, realm, nonce, uri, algorithm, response, qop, nc, cnonce)
        result = utility.parse(string)

        self.assertEqual(result["Digest"], 'Digest')
        self.assertEqual(result["username"], username)
        self.assertEqual(result["realm"], realm)
        self.assertEqual(result["nonce"], nonce)
        self.assertEqual(result["uri"], uri)
        self.assertEqual(result["algorithm"], algorithm)
        self.assertEqual(result["response"], response)
        self.assertEqual(result["qop"], qop)
        self.assertEqual(result["nc"], nc)
        self.assertEqual(result["cnonce"], cnonce)

class KarmiaUtilityStringToBoolean(unittest.TestCase):
    def test_true(self):
        utility = KarmiaUtilityString()
        self.assertEqual(utility.to_boolean("true"), True)
        self.assertEqual(utility.to_boolean("True"), True)
        self.assertEqual(utility.to_boolean("TRUE"), True)
        self.assertEqual(utility.to_boolean(1), True)
        self.assertEqual(utility.to_boolean(True), True)

    def test_false(self):
        utility = KarmiaUtilityString()
        self.assertEqual(utility.to_boolean("false"), False)
        self.assertEqual(utility.to_boolean("False"), False)
        self.assertEqual(utility.to_boolean("FALSE"), False)
        self.assertEqual(utility.to_boolean("true1"), False)
        self.assertEqual(utility.to_boolean("false1"), False)
        self.assertEqual(utility.to_boolean(""), False)
        self.assertEqual(utility.to_boolean("0"), False)
        self.assertEqual(utility.to_boolean(0), False)
        self.assertEqual(utility.to_boolean(False), False)



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
