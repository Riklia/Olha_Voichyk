def find_pairs(arr, target):
    num = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                num += 1
    return num


if __name__ == "__main__":
    print(find_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5))
