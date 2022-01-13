# 13.1

ls = [int(i) for i in input().split()]

def sort_sum_of_numbers(ls):
    new_ls = []
    for i in ls:
        summ = 0
        while i:
            last = i % 10
            summ += last
            i = i // 10
        new_ls.append(summ)
    return sorted(new_ls)
print(sort_sum_of_numbers(ls))