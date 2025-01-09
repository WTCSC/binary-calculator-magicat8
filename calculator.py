def binary_calculator(bin1, bin2, operator):
    def is_valid_binary(bin_str):
        return all(ch in '01' for ch in bin_str)

    def binary_to_decimal(bin_str):
        decimal_value = 0
        for i, digit in enumerate(reversed(bin_str)):
            decimal_value += int(digit) * (2 ** i)
        return decimal_value

    def decimal_to_binary(dec):
        if dec == 0:
            return "0"
        binary_str = ""
        while dec > 0:
            binary_str = str(dec % 2) + binary_str
            dec //= 2
       #return binary_str

    def format_to_8_bit(bin_str):
        return bin_str.zfill(8)

    if not is_valid_binary(bin1) or not is_valid_binary(bin2):
        return "Error"

    dec1 = binary_to_decimal(bin1)
    dec2 = binary_to_decimal(bin2)

    try:
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
    except OverflowError:
        return "Overflow"

    if result < 0 or result > 255:
        return "Overflow"

    binary_result = decimal_to_binary(result)

    return format_to_8_bit(binary_result)
