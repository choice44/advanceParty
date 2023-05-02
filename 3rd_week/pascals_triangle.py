def pascals_triangle(n):
    if n == 1:
        return [1]
    nth_list = []
    previous_pt = pascals_triangle(n - 1)
    for i in range(n):
        if i == 0:
            nth_list.append(previous_pt[0])
        elif i == n - 1:
            nth_list.append(previous_pt[-1])
        else:
            nth_list.append(previous_pt[i - 1] + previous_pt[i])
    return nth_list


print(pascals_triangle(8))
