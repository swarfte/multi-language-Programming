import sys
import os

import config.keyword
import config.symbol
import config.type
import config.function
import config.number

#order is important
keyword_list = [
    config.type.TypeKeyword().keywords,
    config.keyword.Keyword().keywords,
    config.symbol.SymbolKeyword(space=False).keywords,
    config.number.NumberKeyword().keywords,
    config.function.FunctionKeyword().keywords,
]


def encode(file_path: str) -> None:

    with open(file_path, 'r', encoding="utf-8") as f:
        data = f.read()

    for keyword_file in keyword_list:
        for key, replace_value in keyword_file.items():
            if key in data:
                data = data.replace(key, replace_value[0])

    with open(file_path+"cn", 'w', encoding="utf-8") as f:
        f.write(data)


if __name__ == '__main__' and len(sys.argv) == 2:
    # print(str(sys.argv[1]))
    encode(str(sys.argv[1]))
    os.system("pause")
