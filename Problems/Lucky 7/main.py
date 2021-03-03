times = int(input())
num_list = []
for _ in range(times):
    num_list.append(int(input()))
for i in range(times):
    if num_list[i] % 7 == 0:
        print(num_list[i] * num_list[i])