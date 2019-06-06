def checkio(number):
    bin_num = bin(number)
    list_bin_num = list(bin_num)
    ans = 0
    for i in list_bin_num:
        if i == "1":
            ans = ans + 1
    return ans
