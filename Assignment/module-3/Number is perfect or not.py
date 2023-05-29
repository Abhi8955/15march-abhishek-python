def is_perfect_number(number):
    if number <= 0:
        return False

    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    if sum(divisors) == number:
        return True
    else:
        return False
