import os
import time

hinh = [
"""
    *    
   * *   
  *****  
 *     * 
*       *
""",
"""
    *    
   * *   
  *   *  
 *     * 
  *   *  
   * *   
    *    
""",
"""
*****  
*      
*****  
    *  
*****  
""",
"""
*****  
*   *  
*   *  
*   *  
*****  
"""
]

for i in range(len(hinh)):
    os.system("cls" if os.name == "nt" else "clear")  # xóa màn hình (Windows = cls, Linux/Mac = clear)
    print(hinh[i])
    time.sleep(5)  # dừng 5 giây
