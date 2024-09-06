#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1

    if index == 0:
        print("{} arguments.".format(index))
    elif index == 1:
        print("{} argument:".format(index))
    else:
        print("{} arguments:".format(index))

    if index >= 1:
        index = 0
        for arg in sys.argv:
            if index != 0:
                print("{}: {}".format(index, arg))
            index += 1
