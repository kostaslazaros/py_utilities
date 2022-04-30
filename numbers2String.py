grnumber_map_basic = {
    0: "",
    1: "ένα",
    2: "δύο",
    3: "τρία",
    4: "τέσσερα",
    5: "πέντε",
    6: "έξι",
    7: "επτά",
    8: "οκτώ",
    9: "εννέα",
    10: "δέκα",
    11: "έντεκα",
    12: "δώδεκα",
    20: "είκοσι",
    30: "τριάντα",
    40: "σαράντα",
    50: "πενήντα",
    60: "εξήντα",
    70: "εβδομήντα",
    80: "ογδόντα",
    90: "ενενήντα",
    100: "εκατό",
    200: "διακόσια",
    300: "τριακόσια",
    400: "τετρακόσια",
    500: "πεντακόσια",
    600: "εξακόσια",
    700: "επτακόσια",
    800: "οκτακόσια",
    900: "εννιακόσια",
    1000: "χίλια",
    10000: "δέκα χιλιάδες",
    100000: "εκατό χιλιάδες",
    1000000: "ένα εκατομμύριο",
    1000000000: "ένα δισεκατομμύριο",
}

grnumber_map_xiliades = {
    0: "",
    1: "ένα",
    2: "δύο",
    3: "τρεις",
    4: "τέσσερεις",
    5: "πέντε",
    6: "έξι",
    7: "επτά",
    8: "οκτώ",
    9: "εννέα",
    10: "δέκα",
    11: "έντεκα",
    12: "δώδεκα",
    20: "είκοσι",
    30: "τριάντα",
    40: "σαράντα",
    50: "πενήντα",
    60: "εξήντα",
    70: "εβδομήντα",
    80: "ογδόντα",
    90: "ενενήντα",
    100: "εκατό",
    200: "διακόσια",
    300: "τριακόσια",
    400: "τετρακόσια",
    500: "πεντακόσιες",
    600: "εξακόσιες",
    700: "επτακόσιες",
    800: "οκτακόσιες",
    900: "εννιακόσιες",
    1000: "χίλια",
    10000: "δέκα χιλιάδες",
    100000: "εκατό χιλιάδες",
    1000000: "ένα εκατομμύριο",
    1000000000: "ένα δισεκατομμύριο",
}


def split_triades(value: str) -> list:
    length = len(value)
    rest = length % 3
    triades = (length // 3) + 1
    if rest == 0:
        triades -= 1
    final = []
    for i in range(triades):
        start = -3 * i - 3
        end = length - 3 * i
        final.append(value[start:end])
    return final


ones = {
    0: "μηδέν",
    1000: "χίλια",
    1000000: "ένα εκατομμύριο",
    1000000000: "ένα δισεκατομμύριο",
    1000000000000: "ένα τρισεκατομμύριο",
    1000000000000000: "ένα τετράκις εκατομμύριο",
}


postfixes = {
    0: "",
    1: " χιλιάδες",
    2: " εκατομμύρια",
    3: " δισεκατομμύρια",
    4: " τρισεκατομμύρια",
    5: " τετράκις εκατομμύρια",
}


def get_floating_num(number: float) -> str:
    rounded_num = round(number, 2)
    number_parts = str(rounded_num).split(".")
    num_part1 = number_parts[0]
    num_part2 = number_parts[1]
    if len(num_part2) == 1:
        num_part2 = num_part2 + "0"
    if int(num_part2) == 0:
        return num2text_gr(int(num_part1))
    if num_part2 == "01":
        return (
            num2text_gr(int(num_part1))
            + " και "
            + num2text_gr(int(num_part2))
            + " λεπτό"
        )
    else:
        return (
            num2text_gr(int(num_part1))
            + " και "
            + num2text_gr(int(num_part2))
            + " λεπτά"
        )


def num2text_gr(number: int) -> str:
    if number in ones:
        return ones[number]
    num_str = str(number)
    num_arr = split_triades(num_str)
    res = []
    for i, triada in enumerate(num_arr):
        number = int(triada)
        res.append(conversion((number, i)))
    res.reverse()
    return " ".join(res)


def conversion(tuple):
    num = tuple[0]
    idx = tuple[1]
    if num == 0:
        return ""
    if num == 1 and idx == 1:
        return "χίλια"
    if num == 1 and idx == 2:
        return "ένα εκατομμύριο"
    if num == 1 and idx == 3:
        return "ένα δισεκατομμύριο"
    if num == 1 and idx == 4:
        return "ένα τρισεκατομμύριο"
    return number2stringWrapper(num, idx) + postfixes[idx]


def number2string10s(number: int, dic_map: dict) -> str:
    if number in dic_map:
        return dic_map[number]
    if number < 100:
        if number == 0:
            return "μηδέν"
        return dic_map[number // 10 * 10] + " " + dic_map[number % 10]
    return ""


def number2string100s(number: int, dic_map: dict) -> str:
    if number in dic_map:
        return dic_map[number]
    if number < 1000:
        if number // 100 == 1:
            return dic_map[100] + "ν" + " " + number2string10s(number % 100, dic_map)
        else:
            return (
                dic_map[(number // 100) * 100]
                + " "
                + number2string10s(number % 100, dic_map)
            )
    return ""


def number2stringWrapper(number: int, idx: int) -> str:
    grnumber_map = grnumber_map_basic
    if idx == 1:
        grnumber_map = grnumber_map_xiliades
    if number in grnumber_map:
        return grnumber_map[number]
    if number < 100:
        return number2string10s(number, grnumber_map)
    if number < 1000:
        return number2string100s(number, grnumber_map)
    return ""


if __name__ == "__main__":
    print(get_floating_num(15543454.991))
