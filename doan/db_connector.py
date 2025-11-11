# Tập: db_connector.py
import pyodbc

# !!! QUAN TRỌNG: HÃY THAY THẾ CÁC GIÁ TRỊ NÀY
# SERVER_NAME = 'TEN_MAY_CHU_CUA_BAN' # Ví dụ: DESKTOP-ABCDE\SQLEXPRESS
# DATABASE_NAME = 'QuanLyCuaHangXeMay'
# USERNAME = 'TEN_DANG_NHAP_SQL' # Ví dụ: 'sa'
# PASSWORD = 'MAT_KHAU_CUA_BAN'

def get_connection():
    
    # Tạo và trả về một đối tượng kết nối đến SQL Server.

    try:
        # Sử dụng driver ODBC 17 cho SQL Server
        # Đây là chuỗi kết nối đã sửa
        conn_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=HIEU-PC\SQLEXPRESS;"
            "DATABASE=QuanLyCuaHangXeMay;"
            "UID=hieuSQL;"
            "PWD=123;"
            "TrustServerCertificate=yes;"  # Thêm dòng này để sửa lỗi chứng chỉ
        )
        
        conn = pyodbc.connect(conn_string)
        return conn

    except pyodbc.Error as e:
        print(f"Lỗi khi kết nối đến SQL Server: {e}")
        return None

# Bạn có thể thêm đoạn này ở cuối file để chạy thử
if __name__ == '__main__':
    conn = get_connection()
    if conn:
        print("Kết nối thành công!")
        conn.close()
    else:
        print("Kết nối thất bại.")
        