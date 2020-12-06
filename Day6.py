def task1():
    result = 0

    with open('./input-day6', 'r') as f:
        lines = f.read().splitlines()

        unique_chars = set()

        for line in lines:
            if not line:
                result += len(unique_chars)
                unique_chars = set()
            else:
                unique_chars.update(list(line))

        result += len(unique_chars)

    return result


if __name__ == "__main__":
    print(task1())
