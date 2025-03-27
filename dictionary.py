D = {
'name' : ' Vagh Tung',
'age'  : 20,
'address' : 'Vinh Loc, Thanh Hoa',
'status' : 'single'
}
# truy xuat du lieu
print(D.get('name'))
# hoac print(D['name'])

# them va cap nhat du lieu
D['name']='Nguyen Van Tung'
print(D)
# xoa
# duyet qua dictionary
for key, value in D.items() :
    print(f"{key} : {value}")
# kiem tra 
if 'name' in D :
    print(f"co ton tai {D.get('name')} trong D")  

#pop(key) → Khi cần lấy giá trị trước khi xóa.
#popitem() → Khi cần xóa phần tử cuối cùng (hữu ích cho cấu trúc LIFO).
#clear() → Khi muốn xóa sạch nhưng giữ lại dictionary.
#del → Khi muốn xóa một key cụ thể hoặc toàn bộ dictionary.