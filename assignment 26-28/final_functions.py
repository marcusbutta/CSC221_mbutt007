def min_max_sum(n1, n2, n3):
    max_n = max(n1, n2, n3)
    min_n = min(n1, n2, n3)
    sum_n = sum([n1, n2, n3])

    return min_n, max_n, sum_n


def min_max_sum_improved(*n):
    max_n = max(n)
    min_n = min(n)
    sum_n = sum(n)

    return min_n, max_n, sum_n


def if_elif_else(num):
    if num < 5:
        return "Your number is less than 5."
    elif num <= 10:
        return "Your number is less than or equal to 10."
    else:
        return "Your number is greater than 10."


# For testing purposes:
def min_max_sum_improved_bug(*n):
    max_n = max(n)
    min_n = min(n)
    sum_n = sum(n)

    return min_n, max_n, sum_n + 7
