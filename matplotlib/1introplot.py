import matplotlib.pyplot as plt
"""
# Data Visualization
    การนำข้อมูลมาแสดงผลในรูปแบบกราฟฟิก กราฟ แผนภูมิ หรืออื่นๆ เพื่อใช้อธิบาย
ความสัมพันธ์ของข้อมูลได้ง่ายมากยิ่งขึ้น โดยข้อมูลที่สนใจมักอยู่ในรูปแบบอักขระ ข้อความ
ตัวเลข หรือแบบตาราง ซึ่งจำนวนข้อมูลมีอย่างมากมายมหาศาล
    การใช้Data Visualizationจะช่วยให้การวิเคราะห์ข้อมูลมาทำได้ง่ายมากยิ่งขึ้น
และเห็นภาพวมของข้อมูลทั้งหมด ดังคำกล่าว"ภาพหนึ่งภาพแทนคำพูดนับพันคำ"
"""
# ข้อมูลแกนx,แกนy ต้องเป็นข้อมูลแบบชุด เช่น List,Numpy Array,DataSeries,DataFrame

x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.bar(x,y)    # กราฟแท่ง
plt.show()      # แสดงกราฟ
plt.plot(x,y)    # กราฟเส้น
plt.show()
