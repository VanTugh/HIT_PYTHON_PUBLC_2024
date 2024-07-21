# Viết một chương trình nhận vào một số N từ người dùng và in ra tất cả các cặp số Amicable từ 1 đến N. Cặp số Amicable là cặp số mà tổng các ước số của số thứ nhất bằng số thứ hai và ngược lại.
def sum_of_divisors(num):
    """
    Hàm này tính tổng các ước số của một số num.
    """
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i
    return total

def find_amicable_pairs(n):
    """
    Hàm này tìm và in ra các cặp số Amicable từ 1 đến n.
    """
    amicable_pairs = []
    for num in range(1, n + 1):
        sum1 = sum_of_divisors(num)
        sum2 = sum_of_divisors(sum1)
        if num == sum2 and num != sum1 and num < sum1:
            amicable_pairs.append((num, sum1))
    
    return amicable_pairs

if __name__ == "__main__":
    N = int(input("Nhập vào một số N: "))
    if N <= 0:
        print("Số N phải lớn hơn 0")
    else:
        pairs = find_amicable_pairs(N)
        if pairs:
            print("Các cặp số Amicable từ 1 đến", N, "là:")
            for pair in pairs:
                print(pair)
        else:
            print("Không có cặp số Amicable nào trong khoảng từ 1 đến", N)
