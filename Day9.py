import fileinput

window_length = 25


def parse():
    numbers = []

    for l in fileinput.input():
        numbers.append(int(l.strip()))

    return numbers


def task1(numbers):
    for i in range(window_length, len(numbers)):
        number = numbers[i]

        found = False

        for candidate1 in numbers[(i - window_length):i]:
            found = False

            for candidate2 in numbers[(i - window_length + 1):i]:
                if candidate1 + candidate2 == number:
                    found = True
                    break

            if found:
                break

        if not found:
            return number


def task2(numbers, weak_spot):
    for i in range(len(numbers)):
        temporary_sum = numbers[i]

        for j in range(i+1, len(numbers)):
            temporary_sum += numbers[j]

            if temporary_sum == weak_spot:
                return min(numbers[i:j+1]) + max(numbers[i:j+1])

            if temporary_sum > weak_spot:
                break


numbers = parse()

# Part 1
weak_spot = task1(numbers)
print(weak_spot)

# Part 2
print(task2(numbers, weak_spot))
