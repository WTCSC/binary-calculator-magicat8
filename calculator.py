def is_bin(bin_str):
    return all(ch in '01' for ch in bin_str)

def bin_to_dec(bin_str):
    dec_value = 0
    for i, digit in enumerate(bin_str[::-1]):
        dec_value += int(digit) * (2 ** i)
    return dec_value

def dec_to_bin(dec):
    if dec == 0:
        return "0"
    binary_str = ""
    while dec > 0:
        binary_str = str(dec % 2) + binary_str
        dec //= 2
    return binary_str

def make_8_bit(bin_str):
    return bin_str.zfill(8)

def binary_calculator(bin1, bin2, operator):
    if not is_bin(bin1) or not is_bin(bin2):
        return "Error"

    dec1 = bin_to_dec(bin1)
    dec2 = bin_to_dec(bin2)

    if operator == '+':
        result = dec1 + dec2
    elif operator == '-':
        result = dec1 - dec2
    elif operator == '*':
        result = dec1 * dec2
    elif operator == '/':
        if dec2 == 0:
            return "NaN"
        result = dec1 // dec2
    else:
        return "Error"

    if result > 255 or result < 0:
        return "Overflow"

    binary_result = dec_to_bin(result)

    return make_8_bit(binary_result)


