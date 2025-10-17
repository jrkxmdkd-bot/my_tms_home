def cycle_sequence(numbers, limit):
    count = 0
    while count < limit:
        for num in numbers:
            yield num
            count += 1
            if count >= limit:
                break


if __name__ == "__main__":
    seq = [1, 2, 3]
    n = int(input("Введите количество чисел: "))
    for num in cycle_sequence(seq, n):
        print(num, end=" ")
