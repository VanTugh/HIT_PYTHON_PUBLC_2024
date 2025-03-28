# Bai 1
from collections import Counter

my_tuple = tuple(map(int, input("Hãy nhập dãy số vào đây: ").split()))
count = Counter(my_tuple)
result = [num for num, dem in count.items() if dem % 5 == 0 and dem % 10 != 0]

if result:
    print(*result)
else:
    print("Không có")

# Bai 2
def kiemtraso():
    while True:
        try:
            x = int(input("Nhập số x (0 < x < 10000):\n ")) 
            if 0 < x < 10000:
                return x
            else:
                print("Hãy nhập lại!")
        except ValueError:
            print("Lỗi! Vui lòng nhập một số nguyên hợp lệ.")

def dem_so_buoc_toi_thieu(x):
    return ((x + 2) // 3)

if __name__ == "__main__":
    x = kiemtraso()  # Kiểm tra giá trị x
    print(dem_so_buoc_toi_thieu(x))  # In kết quả

# Bai 3
def tim_nguoi_thap_nhi():
    so_nguoi = int(input("Nhập số người vào đây: "))

    dsach = []  # Danh sách lưu (tên, điểm)
    diem = []   # Danh sách lưu điểm

    for _ in range(so_nguoi):
        ten, diem_so = input().rsplit(maxsplit=1)
        diem_so = int(diem_so)  # Chuyển điểm thành số nguyên
        dsach.append((ten, diem_so))  # Thêm vào danh sách
        diem.append(diem_so)  # Lưu điểm vào danh sách điểm

    # Hàm Bubble Sort để sắp xếp danh sách điểm
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - 1 - i):  # So sánh từng cặp phần tử liên tiếp
                if arr[j] > arr[j + 1]:  # Nếu phần tử trước lớn hơn phần tử sau, đổi chỗ
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break  # Nếu không có sự hoán đổi nào, danh sách đã được sắp xếp
        return arr

    # Xóa điểm trùng lặp và sắp xếp bằng bubble_sort
    diem_riêng = list(set(diem))
    diem_riêng = bubble_sort(diem_riêng)  # Sắp xếp danh sách điểm bằng bubble_sort

    if len(diem_riêng) < 2:
        print("Không có điểm thấp nhì")
        return

    # Điểm thấp nhì là phần tử thứ 2 sau khi sắp xếp
    diem_thap_nhi = diem_riêng[1]

    # Tìm tất cả tên có điểm thấp nhì và sắp xếp theo tên
    ket_qua = sorted(ten for ten, diem_so in dsach if diem_so == diem_thap_nhi)

    # In kết quả
    print("\n".join(ket_qua))


# Chạy chương trình bài 3
tim_nguoi_thap_nhi()
