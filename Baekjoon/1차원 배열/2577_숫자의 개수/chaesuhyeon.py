List = []
for i in range(3):
    List.append(int(input()))
a = str(List[0] * List[1] * List[2])
print(a.count("0"),a.count("1"), a.count("2"), a.count("3"), a.count("4"), a.count("5"), a.count("6"), a.count("7"), a.count("8"), a.count("9"), sep="\n")

#
a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))