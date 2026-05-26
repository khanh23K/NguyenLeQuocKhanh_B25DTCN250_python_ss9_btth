branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] #(Đơn vị: VNĐ)
target_achieved = [True, True, False, True, False] # (True là Đạt chỉ tiêu, False là Không đạt)
choice = '0'
while True:
    choice = input('''===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): ''') 
    if choice == "1":
        print('---BÁO CÁO DOANH THU TỔNG HỢP---')
        print(f"{"Tên cơ sở":<30} | {'Doanh thu':<10} | {'Trạng thái':<10}")
        print("-"*65)
        for i in range(len(branch_names)):
            print(f'{branch_names[i]:<30} | {daily_revenues[i]:<10} | {'Đạt' if target_achieved[i] else 'không đạt':<10}')
        print('-'*65)
        print(f'=> TONG DOANH THU TOAN VUNG: {sum(daily_revenues)} VND')
    elif choice == "2":
        max_revenue = max(daily_revenues)
        min_revenue = min(daily_revenues)
        max_index = branch_names [daily_revenues.index(max_revenue)]
        min_index = branch_names[daily_revenues.index(min_revenue)]
        max_branch = branch_names[max_index]
        min_branch = branch_names[min_index]
        print(f'''--- THONG KE CO SO NOI BAT
- Cơ sở co doanh thu CAO NHẬT: {max_branch} ({max_revenue})
- Cơ sở co doanh thu THAP NHAT: {min_branch} ({min_revenue})''')
    elif choice == "3":
        failed_branches = []
        for i, target in enumerate(target_achieved):
            if not target:
                failed_branches.append (branch_names [i])
        print(f'''DANH SACH CO SO CAN HO TRO TRA CỨU ĐƯỢC
{failed_branches}''')
    elif choice == "4":
        print("Hệ thống ghi nhận du lieu hoàn tất. Tạm biệt!")
        break
    else:
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")  
    