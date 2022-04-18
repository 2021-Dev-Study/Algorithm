cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()

for cro in cro_list:
    len_i = len(string)
    string = string.replace(cro, "_")

print(len(string))