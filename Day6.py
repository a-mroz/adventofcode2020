def task1(lines):
    result = 0

    unique_chars = set()

    for line in lines:
        if not line:
            result += len(unique_chars)
            unique_chars = set()
        else:
            unique_chars.update(list(line))

    result += len(unique_chars)

    return result


def task2(lines):
    from collections import Counter

    result = 0

    group_frequenices = Counter()
    lines_in_group = 0

    for line in lines:
        if not line:
            result += sum(1 for _,
                          v in group_frequenices.items() if v == lines_in_group)
            group_frequenices.clear()
            lines_in_group = 0
        else:
            group_frequenices += Counter(line)
            lines_in_group += 1

    result += sum(1 for _, v in group_frequenices.items()
                  if v == lines_in_group)

    return result


if __name__ == "__main__":
    with open('./input-day6', 'r') as f:
        lines = f.read().splitlines()
        print(task1(lines))
        print(task2(lines))
