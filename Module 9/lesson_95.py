speakers_file = open('speakers.txt', 'r', encoding='utf-8')
data = speakers_file.read(14)
speakers_file.seek(1)
data_2 = speakers_file.read(22)
print(data)
print(data_2)
# for i_line in speakers_file:
#     print(i_line, end = '')
speakers_file.close()
