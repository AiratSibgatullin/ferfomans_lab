import sys


def get_path(len_list, step):
    # длина кругового списка определяется нахождением общего кратного между количеством чисел и интервалом движения
    cyclical_list = [x for x in range(1, len_list + 1)] * (step-1)
    path_list = [1]
    for i in range(step-1, len(cyclical_list), step-1):
        if cyclical_list[i] != 1:
            path_list.append(cyclical_list[i])
        else:
            break
    for i in path_list:
        print(i, end="")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please, usage: python task_1.py value_1 value_2")
        sys.exit(1)
    get_path(int(sys.argv[1]), int(sys.argv[2]))
