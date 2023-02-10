for line in file1:
    if line_count == 202:
        break
    line_count += 1
    # print(line, end="")
    if line.find("+---") == 0:
        if last:
            file2 = folder_buff[0] + "\\\n"
            folder_buff[0] = line[4:-1]
        else:
            folder_buff[0] = line[4:-1]
            last2_iter = 0
            last = True
        continue
    last = False
    if line.find("|") == 0:
        if (index := line.find("+---")) > 0:
            while (x_ := line.count("|")) == (folderIndex-1):
                last2_iter -= 1
            #last2_iter -= 1
            folderIndex = line.count("|") + last2_iter
            folder_buff[folderIndex] = "\\" + line[index + 4:-1]
            continue
        if (index := line.find("\---")) > 0:
            folderIndex = line.count("|")
            folder_buff[folderIndex] = "\\" + line[index + 4:-1]
            last2_iter += 1
            continue
        else:
            if file_str_return := file_str(line):
                file2 += concat_list(folder_buff, 0, folderIndex) + "\\" + file_str_return