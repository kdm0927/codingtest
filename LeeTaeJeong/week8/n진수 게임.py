def solution(n, t, m, p):
    def convert_to_base(num, base):
        if num == 0: return "0"
        digits = "0123456789ABCDEF"
        res = ""
        while num > 0:
            res += digits[num % base]
            num //= base
        return res[::-1] # 역순으로 뒤집어 반환

    full_str = ""
    number = 0
    while len(full_str) < t * m:
        full_str += convert_to_base(number, n)
        number += 1
        
    return full_str[p-1 : t*m : m]