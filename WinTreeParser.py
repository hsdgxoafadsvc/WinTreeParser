def file_str(line: str) -> str:
    i = 0
    for letter in line:
        if letter == "\n":
            return ""
        if letter == " " or letter == "|":
            i += 1
            continue
        break
    return line[i:]


def concat_list(value: list, begin: int, end: int) -> str:
    temp_str = ""
    while begin < end + 1:
        temp_str += value[begin]
        begin += 1
    return temp_str


return_file = ""

with open(r"C:\Users\borod\OneDrive\Рабочий стол\Прочее(27.12.2022).txt", "r", errors='ignore') as file1:
    line_count = 0
    folder_buff = [""] * 20
    folder_index = 0
    last = False
    for line in file1:
        if line.find("+---") == 0:
            if last:
                return_file = folder_buff[0] + "\\\n"
                folder_buff[0] = line[4:-1]
            else:
                folder_buff[0] = line[4:-1]
                last = True
            continue
        last = False
        if line.find("|") == 0:
            if (index := line.find("+---")) > 0 or (index := line.find("\---")) > 0:
                folder_buff[index // 4] = "\\" + line[index + 4:-1]
                folder_index = index // 4
                continue
            else:
                if file_str_return := file_str(line):
                    return_file += concat_list(folder_buff, 0, folder_index) + "\\" + file_str_return