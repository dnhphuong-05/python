def bin_packing(weights, P):
    weights.sort(reverse=True)
    bins = []

    for weight in weights:
        placed = False

        for b in bins:
            if sum(b) + weight <= P:
                b.append(weight)
                placed = True
                break

        if not placed:
            bins.append([weight])

    return bins

# Nhập danh sách các gói hàng
weights = list(map(int, input("Nhập vào các gói kiện hàng với số lượng kg, cách nhau bởi dấu cách: ").split(", ")))

# Nhập dung tích tối đa của container
P = int(input("Nhập vào khối lượng container có thể chứa tối đa: "))

# Gọi hàm và in kết quả
result = bin_packing(weights, P)
print(f"Cần {len(result)} thùng để chứa các gói hàng.")
for i, b in enumerate(result, 1):
    print(f"Thùng {i}: {b}")
