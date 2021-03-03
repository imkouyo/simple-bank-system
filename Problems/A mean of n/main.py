times = int(input())
num_list = []
for _ in range(times):
    num_list.append(int(input()))
print(sum(num_list) / times)