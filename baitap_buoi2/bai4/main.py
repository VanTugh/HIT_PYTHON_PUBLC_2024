#   Dãy số Fibonacci
# Hãy viết chương trình tìm n số Fibonacci đầu tiên.
# Quy luật của dãy số Fibonacci: số tiếp theo bằng tổng của 2 số trước, 2 số đầu tiên của dãy số là 0, 1. Ví dụ: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Hàm main để chạy chương trình
if __name__ == "__main__":
    n = int(input("Nhập vào số lượng số Fibonacci cần tìm: "))
    if n <= 0:
        print("Số lượng phải lớn hơn 0")
    else:
        fib_sequence = fibonacci(n)
        print("Dãy số Fibonacci:")
        print(" ".join(map(str, fib_sequence)))
