def pascals_triangle(n):
    if n == 1:
        return [1]
    nth_list = []
    for i in range(n):
        if i == 0:
            nth_list.append(pascals_triangle(n - 1)[0])
        elif i == n - 1:
            nth_list.append(pascals_triangle(n - 1)[-1])
        else:
            nth_list.append(pascals_triangle(n - 1)[i - 1] + pascals_triangle(n - 1)[i])
    return nth_list


print(pascals_triangle(8))
