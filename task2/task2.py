import sys
import math


def main():
    if len(sys.argv) != 3:
        print("Please, usage: python task_2.py path_to_file_one path_to_file_two")
        sys.exit(1)

    circle = sys.argv[1]
    points = sys.argv[2]

    with open(rf"{circle}", "r") as file:
        center_x, center_y = map(int, file.readline().split())
        radius = int(file.readline())

    with open(rf"{points}", "r") as file:
        for line in file:
            point_x, point_y = map(int, line.split())
            position = get_position(center_x, center_y, radius, point_x, point_y)
            print(position)


def get_position(center_x, center_y, radius, point_x, point_y):
    distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)

    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


if __name__ == "__main__":
    main()

