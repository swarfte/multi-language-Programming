from ast import keyword


class SymbolKeyword(object):
    def __init__(self, space: bool = True) -> None:
        self.keywords = {
            "->": ["回傳值"],
            "**": ["次方"],
            "!=": ["不等於"],
            "+=": ["加等於"],
            "-=": ["減等於"],
            "*=": ["乘等於"],
            "/=": ["除等於"],
            "%=": ["取餘等於"],
            "==": ["等於"],
            "+": ["加"],
            "-": ["減"],
            "*": ["乘"],
            "/": ["除"],
            "=": ["被賦值"],
            "%": ["餘數"],
            "!": ["非"],
        }
        try:
            if space:
                self.fix()
        except Exception as e:
            print("Failed to fix keyword:", e)

    def fix(self) -> None:
        keyword_copy = dict()
        for k, v in self.keywords.items():
            keyword_copy[" " + k] = v

        self.keywords = keyword_copy
