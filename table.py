from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def func_s(x):
	S_pod = [5,8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11]
	return S_pod[(S_pod.index(x) + 1) % 16]

def F2_mul(x, y): 
    x = int(x)
    y = int(y)
    sum = 0
    mult = x & y
    while mult != 0:
        sum ^= mult & 1
        mult >>= 1
   
    return sum

wb = Workbook()
dest_filename = 'new_wb.xlsx'
ws1 = wb.active

for i in range(16):
	row_temp = []
	for j in range(16):
		counter = 0
		for itera in range(16):
			if F2_mul(itera, i) == F2_mul(func_s(itera), j):
				counter+=1
		if counter!= 0:
			print(i, j,',',bin(i).count("1") + bin(j).count("1"), ',', (counter - 8) / 16)
		row_temp.append(counter - 8)
	ws1.append(row_temp)		

wb.save(filename = dest_filename)