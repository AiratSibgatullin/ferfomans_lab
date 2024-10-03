import sys
from statistics import mean


def main():
    if len(sys.argv) != 2:
        print("Please, usage: python task_4.py file_name")
        sys.exit(1)
    file_nums = sys.argv[1]
    with open(rf"{file_nums}", "r") as file:
        nums = [int(num) for num in file.read().split()]
    print(get_count_moves(nums))


def get_count_moves(values):
    return int(sum([abs(val - int(mean(values))) for val in values]))
    # сократил следующие инструкции
    #count = 0
    #average = int(mean(values))
    #for num in values:
    #    count += abs(num - average)


if __name__ == "__main__":
    main()
