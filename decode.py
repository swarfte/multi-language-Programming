import sys
import os

import config.keyword
import config.symbol
import config.type
import config.function
import config.number

#order is important
keyword_list = [
    config.keyword.Keyword().keywords,
    config.type.TypeKeyword().keywords,
    config.symbol.SymbolKeyword().keywords,
    config.function.FunctionKeyword().keywords,
    config.number.NumberKeyword().keywords
]


def decode(file_path: str) -> None:

    with open(file_path, 'r', encoding="utf-8") as f:
        data = f.read()

    for keyword_file in keyword_list:
        for key, replace_value in keyword_file.items():
            for value in replace_value:
                if value in data:
                    data = data.replace(value, key+" ")

    with open(file_path[:-2], 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__' and len(sys.argv) == 2:
    # print(str(sys.argv[1]))
    decode(str(sys.argv[1]))
    os.system("pause")
