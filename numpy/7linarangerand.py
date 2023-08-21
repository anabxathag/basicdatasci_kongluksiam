import numpy as np

# linspace() ไล่เลขตามค่าที่เรากำหนด ค่อยข้างละเอียด เหมาะกับทำกราฟ
aba = np.linspace(1,5)  # ไล่ค่าตั้งแต่1ถึง5
print(aba)

aba = np.linspace(1,7,4)  # ไล้ค่าตั้งแต่1ถึง7 เอา4ตัว
print(aba)

aba = np.linspace(1,4,endpoint=False)  # ไล่ค่าตั้งแต่1ถึง4 แต่ไม่เอา4ที่เป็นค่าท้ายสุด
print(aba)

# arange เหมือนlinspace แต่ไม่ละเอียดเท่า
aba = np.arange(9)  # 0, 1, 2, ..., 8
print(aba)

aba = np.arange(5.0)  # decimal
print(aba)

aba = np.arange(-5,5)
print(aba)

aba = np.arange(-5,0,dtype="float")
print(aba)

aba = np.arange(-5,0,dtype="complex")
print(aba)

aba = np.arange(1,11,2) #(start,stop,step)
print(aba)

# random สุ่มเลขระหว่าง0-1
abc = np.random.random((3,4))   # (row, col)
print(abc)
