# Tệp: app_quanly_xe.py
import tkinter as tk
from tkinter import ttk  # Sử dụng ttk để có giao diện đẹp hơn
from tkinter import messagebox
import db_connector     # Import tệp kết nối chúng ta vừa tạo

# --- CÁC HÀM XỬ LÝ SỰ KIỆN VÀ LOGIC ---

def load_data_to_treeview():
    """
    Lấy dữ liệu từ bảng SanPham và hiển thị lên Treeview
    """
    # Xóa dữ liệu cũ trên cây trước khi tải
    for row in tree.get_children():
        tree.delete(row)
        
    conn = None
    try:
        conn = db_connector.get_connection()
        if conn:
            cursor = conn.cursor()
            # Lấy các cột đúng như trong CSDL
            cursor.execute("SELECT MaSP, TenSP, HangSX, NamSX, GiaBan, SoLuongTon FROM SanPham")
            rows = cursor.fetchall()
            
            # Chèn dữ liệu vào cây
            for row in rows:
                tree.insert('', tk.END, values=row)
                
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
    finally:
        if conn:
            conn.close()

def add_product():
    """
    Thêm một sản phẩm mới vào CSDL
    """
    # Lấy dữ liệu từ các ô nhập liệu
    ma_sp = entry_ma_sp.get()
    ten_sp = entry_ten_sp.get()
    hang_sx = entry_hang_sx.get()
    nam_sx = entry_nam_sx.get()
    gia_ban = entry_gia_ban.get()
    ton_kho = entry_ton_kho.get()

    # Kiểm tra đơn giản (không để trống mã)
    if not ma_sp:
        messagebox.showwarning("Cảnh báo", "Mã sản phẩm không được để trống")
        return

    conn = None
    try:
        conn = db_connector.get_connection()
        if conn:
            cursor = conn.cursor()
            sql_query = "INSERT INTO SanPham (MaSP, TenSP, HangSX, NamSX, GiaBan, SoLuongTon) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(sql_query, (ma_sp, ten_sp, hang_sx, int(nam_sx), float(gia_ban), int(ton_kho)))
            conn.commit() # Xác nhận thay đổi
            
            messagebox.showinfo("Thành công", "Thêm sản phẩm thành công")
            clear_form()
            load_data_to_treeview() # Tải lại dữ liệu
            
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể thêm sản phẩm: {e}")
    finally:
        if conn:
            conn.close()

def update_product():
    """
    Cập nhật sản phẩm đã chọn
    """
    ma_sp = entry_ma_sp.get()
    
    if not ma_sp:
        messagebox.showwarning("Cảnh báo", "Không có sản phẩm nào được chọn để cập nhật")
        return

    conn = None
    try:
        conn = db_connector.get_connection()
        if conn:
            cursor = conn.cursor()
            sql_query = """
            UPDATE SanPham 
            SET TenSP = ?, HangSX = ?, NamSX = ?, GiaBan = ?, SoLuongTon = ?
            WHERE MaSP = ?
            """
            cursor.execute(sql_query, 
                           (entry_ten_sp.get(), 
                            entry_hang_sx.get(), 
                            int(entry_nam_sx.get()), 
                            float(entry_gia_ban.get()), 
                            int(entry_ton_kho.get()), 
                            ma_sp))
            conn.commit()
            
            messagebox.showinfo("Thành công", "Cập nhật sản phẩm thành công")
            clear_form()
            load_data_to_treeview()
            
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể cập nhật sản phẩm: {e}")
    finally:
        if conn:
            conn.close()

def delete_product():
    """
    Xóa sản phẩm được chọn
    """
    ma_sp = entry_ma_sp.get()

    if not ma_sp:
        messagebox.showwarning("Cảnh báo", "Không có sản phẩm nào được chọn để xóa")
        return

    # Hỏi xác nhận
    if messagebox.askyesno("Xác nhận", f"Bạn có chắc chắn muốn xóa sản phẩm {ma_sp} không?"):
        conn = None
        try:
            conn = db_connector.get_connection()
            if conn:
                cursor = conn.cursor()
                # Lưu ý: Cần đảm bảo sản phẩm này không được tham chiếu ở bảng CTHoaDon...
                # Nếu không sẽ bị lỗi khóa ngoại.
                sql_query = "DELETE FROM SanPham WHERE MaSP = ?"
                cursor.execute(sql_query, (ma_sp,))
                conn.commit()
                
                messagebox.showinfo("Thành công", "Xóa sản phẩm thành công")
                clear_form()
                load_data_to_treeview()
                
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xóa sản phẩm: {e}\n(Lỗi: Có thể sản phẩm đã được bán hoặc nhập hàng)")
        finally:
            if conn:
                conn.close()

def on_tree_select(event):
    """
    Khi người dùng nhấp vào một dòng trên cây,
    dữ liệu sẽ được điền vào các ô nhập liệu.
    """
    # Lấy ID của dòng được chọn
    selected_item = tree.focus()
    if not selected_item:
        return
        
    # Lấy giá trị của dòng đó
    values = tree.item(selected_item, 'values')
    
    # Xóa các ô nhập liệu trước
    clear_form()
    
    # Điền dữ liệu vào
    entry_ma_sp.insert(0, values[0])
    entry_ten_sp.insert(0, values[1])
    entry_hang_sx.insert(0, values[2])
    entry_nam_sx.insert(0, values[3])
    entry_gia_ban.insert(0, values[4])
    entry_ton_kho.insert(0, values[5])

def clear_form():
    """
    Xóa trắng tất cả các ô nhập liệu
    """
    entry_ma_sp.delete(0, tk.END)
    entry_ten_sp.delete(0, tk.END)
    entry_hang_sx.delete(0, tk.END)
    entry_nam_sx.delete(0, tk.END)
    entry_gia_ban.delete(0, tk.END)
    entry_ton_kho.delete(0, tk.END)

# --- THIẾT KẾ GIAO DIỆN (UI) ---

# 1. Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý Xe (Sản phẩm) - Cửa hàng DOUBLE IT")
root.geometry("1000x600")

# 2. Tạo một Frame cho Form nhập liệu (giống mockup [cite: 325-339])
form_frame = ttk.Frame(root, padding="10")
form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Các nhãn và ô nhập liệu
ttk.Label(form_frame, text="Mã xe (*):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_ma_sp = ttk.Entry(form_frame, width=30)
entry_ma_sp.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Tên xe (*):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_ten_sp = ttk.Entry(form_frame, width=30)
entry_ten_sp.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Hãng xe (*):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_hang_sx = ttk.Entry(form_frame, width=30)
entry_hang_sx.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Năm SX:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_nam_sx = ttk.Entry(form_frame, width=30)
entry_nam_sx.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Giá bán (*):").grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_gia_ban = ttk.Entry(form_frame, width=30)
entry_gia_ban.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(form_frame, text="Tồn kho:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
entry_ton_kho = ttk.Entry(form_frame, width=30)
entry_ton_kho.grid(row=5, column=1, padx=5, pady=5)

# 3. Frame cho các nút bấm chức năng
button_frame = ttk.Frame(form_frame)
button_frame.grid(row=6, column=0, columnspan=2, pady=10)

btn_add = ttk.Button(button_frame, text="Thêm", command=add_product)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_update = ttk.Button(button_frame, text="Sửa", command=update_product)
btn_update.grid(row=0, column=1, padx=5, pady=5)

btn_delete = ttk.Button(button_frame, text="Xóa", command=delete_product)
btn_delete.grid(row=0, column=2, padx=5, pady=5)

btn_clear = ttk.Button(button_frame, text="Làm mới Form", command=clear_form)
btn_clear.grid(row=0, column=3, padx=5, pady=5)

# 4. Tạo Frame cho Bảng dữ liệu (Treeview)
tree_frame = ttk.Frame(root, padding="10")
tree_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Các cột cho Treeview
columns = ("ma_sp", "ten_sp", "hang_sx", "nam_sx", "gia_ban", "ton_kho")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

# Đặt tên cho các tiêu đề cột
tree.heading("ma_sp", text="Mã SP")
tree.heading("ten_sp", text="Tên Sản Phẩm")
tree.heading("hang_sx", text="Hãng SX")
tree.heading("nam_sx", text="Năm SX")
tree.heading("gia_ban", text="Giá Bán")
tree.heading("ton_kho", text="Tồn Kho")

# Đặt độ rộng cho các cột
tree.column("ma_sp", width=80)
tree.column("ten_sp", width=120)
tree.column("hang_sx", width=100)
tree.column("nam_sx", width=60)
tree.column("gia_ban", width=100)
tree.column("ton_kho", width=60)

# Thêm thanh cuộn
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Gắn sự kiện khi nhấp chuột vào một dòng
tree.bind('<<TreeviewSelect>>', on_tree_select)

# --- KHỞI CHẠY ỨNG DỤNG ---
if __name__ == "__main__":
    # Tải dữ liệu lần đầu khi mở ứng dụng
    load_data_to_treeview()
    
    # Bắt đầu vòng lặp của giao diện
    root.mainloop()