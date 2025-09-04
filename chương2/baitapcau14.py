#gia xử 0 = chủ nhật , 1 = thứ hai, 2 = thứ 3, 3 = thứ 4, 4 = thứ 5, 5 = thứ 6, 7= thứ 7
day7 = ['chủ nhật','thứ hai','thứ 3','thứ 4','thứ 5','thứ 6','thứ 7']
ngaydi = 3 # ngày đi thứ 4 nên = 3
songaydi = 137
ngayve = (ngaydi + songaydi)%7
print('về nhà vào thứ: ',day7[ngayve])  