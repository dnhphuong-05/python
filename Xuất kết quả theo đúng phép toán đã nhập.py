a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
op = input("Chọn phép toán '+', '-', '*', '/': ")

def ketqua(a, b, op):
    try:
        match op:
            case '+':
                return f"a + b = {a + b}"
            case '-':
                return f"a - b = {a - b}"
            case '*':
                return f"a * b = {a * b}"
            case '/':
                if b != 0:
                    return f"a / b = {a / b}"
                else:
                    return "Lỗi"
            case _:
                return "Lỗi"
    except ValueError:
        return "nhập mà cũng sai, ngu"

# Gọi hàm và in kết quả
print(ketqua(a, b, op))
