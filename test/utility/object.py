# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import unittest
from karmia.utility import KarmiaUtilityObject


class TestKarmiaUtilityObjectIsDict(unittest.TestCase):
    def test_is_dict(self):
        utility = KarmiaUtilityObject()

        self.assertEqual(utility.is_dict({}), True)
        self.assertEqual(utility.is_dict(0), False)
        self.assertEqual(utility.is_dict(""), False)
        self.assertEqual(utility.is_dict(True), False)
        self.assertEqual(utility.is_dict(lambda x: x), False)

class TestKarmiaUtilityObjectFlip(unittest.TestCase):
    def test_flip(self):
        utility = KarmiaUtilityObject()
        values = {"a": "A", "b": "B", "c": "C", "d": 1, "e": 2, "f": 3}
        result = utility.flip(values)

        for key in values.keys():
            self.assertEqual(result[values[key]], key)

class TestKarmiaUtilityObjectMerge(unittest.TestCase):
    def test_merge(self):
        utility = KarmiaUtilityObject()
        dictionary1 = {
            "a": "A",
            "b": {
                "c": "C",
                "d": {
                    "e": "E",
                    "f": {
                        "g": "G",
                        "h": {
                            "i": "I",
                            "j": {
                                "k": "K",
                                "l": {
                                    "m": "M"
                                },
                                "n": {
                                    "o": 'O'
                                }
                            }
                        }
                    }
                }
            }
        }
        dictionary2 = {
            "b": {
                "d": {
                    "f": {
                        "g": "G-2",
                        "h": {
                            "j": {
                                "n": "N",
                                "o": "O",
                                "p": {
                                    "q": "Q"
                                }
                            }
                        }
                    },
                    "r": "R",
                    "s": {
                        "t": "T"
                    }
                }
            },
            "u": "U",
            "v": {
                "w": "W"
            }
        }
        result = utility.merge(dictionary1, dictionary2)

        self.assertDictEqual(result, {
            "a": "A",
            "b": {
                "c": "C",
                "d": {
                    "e": "E",
                    "f": {
                        "g": "G-2",
                        "h": {
                            "i": "I",
                            "j": {
                                "k": "K",
                                "l": {
                                    "m": "M"
                                },
                                "n": "N",
                                "o": "O",
                                "p": {
                                    "q": "Q"
                                }
                            }
                        }
                    },
                    "r": "R",
                    "s": {
                        "t": "T"
                    }
                }
            },
            "u": "U",
            "v": {
                "w": "W"
            }
        })

class TestKarmiaUtilityObjectMergeProperties(unittest.TestCase):
    def test_merge_properties(self):
        utility = KarmiaUtilityObject()
        dictionary1 = {
            "a": "A",
            "b": {
                "c": "C",
                "d": {
                    "e": "E",
                    "f": {
                        "g": "G",
                        "h": {
                            "i": "I",
                            "j": {
                                "k": "K",
                                "l": {
                                    "m": "M"
                                },
                                "n": {
                                    "o": 'O'
                                }
                            }
                        }
                    }
                }
            }
        }
        dictionary2 = {
            "b": {
                "d": {
                    "f": {
                        "g": "G-2",
                        "h": {
                            "j": {
                                "n": "N",
                                "o": "O",
                                "p": {
                                    "q": "Q"
                                }
                            }
                        }
                    },
                    "r": "R",
                    "s": {
                        "t": "T"
                    }
                }
            },
            "u": "U",
            "v": {
                "w": "W"
            }
        }
        result = utility.merge_properties(dictionary1, dictionary2)

        self.assertDictEqual(result, {
            "a": "A",
            "b": {
                "c": "C",
                "d": {
                    "e": "E",
                    "f": {
                        "g": "G-2",
                        "h": {
                            "i": "I",
                            "j": {
                                "k": "K",
                                "l": {
                                    "m": "M"
                                },
                                "n": "N",
                                "o": "O",
                                "p": {
                                    "q": "Q"
                                }
                            }
                        }
                    },
                    "r": "R",
                    "s": {
                        "t": "T"
                    }
                }
            },
            "u": "U",
            "v": {
                "w": "W"
            }
        })

class TestKarmiaUtilityObjectRemove(unittest.TestCase):
    def test_remove(self):
        utility = KarmiaUtilityObject()
        value = {"a": "A", "b": "B", "c": "C", "d": 1, "e": 2, "f": 3}
        result = utility.remove(value, "c")

        self.assertEqual(len(result.keys()), 5)
        self.assertIn("a", result)
        self.assertIn("b", result)
        self.assertNotIn("c", result)
        self.assertIn("d", result)
        self.assertIn("e", result)
        self.assertIn("f", result)

    def test_remove_deep(self):
        utility = KarmiaUtilityObject()
        value = {
            "a": {
                "b": {
                    "c": {
                        "d": {
                            "e": {
                                "f": 'value'
                            }
                        }
                    }
                }
            }
        }
        result = utility.remove(value, "e")

        self.assertDictEqual(result, {
            "a": {
                "b": {
                    "c": {
                        "d": {}
                    }
                }
            }
        })

    def test_remove_multiple_position(self):
        utility = KarmiaUtilityObject()
        value = {
            "a": {
                "a": {
                    "key": {}
                }
            },
            "b": {
                "b": {
                    "b": {
                        "b": {
                            "key": {}
                        }
                    }
                }
            }
        }
        result = utility.remove(value, "key")

        self.assertDictEqual(result, {
            "a": {
                "a": {}
            },
            "b": {
                "b": {
                    "b": {
                        "b": {}
                    }
                }
            }
        })

    def test_remove_multiple_property(self):
        utility = KarmiaUtilityObject()
        value = {
            "a": {
                "a": {
                    "a1": {}
                }
            },
            "b": {
                "b": {
                    "b1": {}
                }
            }
        }
        result = utility.remove(value, ["a1", "b1"])

        self.assertDictEqual(result, {
            "a": {
                "a": {}
            },
            "b": {
                "b": {}
            }
        })

class TestKarmiaUtilityObjectRemoveProperties(unittest.TestCase):
    def test_remove(self):
        utility = KarmiaUtilityObject()
        value = {"a": "A", "b": "B", "c": "C", "d": 1, "e": 2, "f": 3}
        result = utility.remove_properties(value, "c")

        self.assertEqual(len(result.keys()), 5)
        self.assertIn("a", result)
        self.assertIn("b", result)
        self.assertNotIn("c", result)
        self.assertIn("d", result)
        self.assertIn("e", result)
        self.assertIn("f", result)

    def test_remove_deep(self):
        utility = KarmiaUtilityObject()
        value = {
            "a": {
                "b": {
                    "c": {
                        "d": {
                            "e": {
                                "f": 'value'
                            }
                        }
                    }
                }
            }
        }
        result = utility.remove_properties(value, "e")

        self.assertDictEqual(result, {
            "a": {
                "b": {
                    "c": {
                        "d": {}
                    }
                }
            }
        })

    def test_remove_multiple_position(self):
        utility = KarmiaUtilityObject()
        value = {
            "a": {
                "a": {
                    "key": {}
                }
            },
            "b": {
                "b": {
                    "b": {
                        "b": {
                            "key": {}
                        }
                    }
                }
            }
        }
        result = utility.remove_properties(value, "key")

        self.assertDictEqual(result, {
            "a": {
                "a": {}
            },
            "b": {
                "b": {
                    "b": {
                        "b": {}
                    }
                }
            }
        })

    def test_remove_multiple_property(self):
        utility = KarmiaUtilityObject()
        value = {
            "a": {
                "a": {
                    "a1": {}
                }
            },
            "b": {
                "b": {
                    "b1": {}
                }
            }
        }
        result = utility.remove_properties(value, ["a1", "b1"])

        self.assertDictEqual(result, {
            "a": {
                "a": {}
            },
            "b": {
                "b": {}
            }
        })



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
