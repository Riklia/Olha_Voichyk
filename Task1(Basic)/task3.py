def digital_root(num):
    while num//10 != 0:
        num = sum(int(i) for i in str(num))
    return num


if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
