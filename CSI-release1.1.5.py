# Ko có MT làm thì ko sao vì MT đâu biết python XD XD XD


import os as o
import time as t
pt = 0
user = o.getlogin()
print(f"Hello, {user}")
print("Welcome to hex's 13th Python 3.13 project of guessing!")
print("Do as best as you can!")

t.sleep(1)

print("Counting up to 5...")
for i in range(1, 6): 
    print(i)
    t.sleep(1)
print("START!")
t.sleep(1)

a = str(input("Quel jour est célébrée la Journée des enseignants vietnamiens ?  :  "))
if a == "20 Novembre": 
    print("Vrai")
    pt += 1
else: 
    print("Faux")
    pt -= 0.25

t.sleep(1)

a = str(input("Tiên học lễ, hậu học văn. Mái gì dạy dỗ chúng em nên người ?  :  "))
if a == "Mái trường": 
    print("Đúng")
    pt += 1
else: 
    print("Sai")
    pt -= 0.25

t.sleep(1)

a = str(input("What is something small and white that all students can use to write on the blackboard?  :  "))
if a == "Chalk": 
    print("Correct")
    pt += 1
else: 
    print("Wrong")
    pt -= 0.25

t.sleep(1)

a = str(input("Bài hát của nhạc sĩ Vũ Hoàng về thầy cô (gợi ý bắt đầu bài: Khi thầy...)?  :  "))
if a == "Bụi phấn": 
    print("Đúng")
    pt += 1
else: 
    print("Sai rồi")
    pt -= 0.25

t.sleep(1)

a = str(input("Nom complet du 20 novembre ? (en vietnamien)  :  "))
if a == "Hiến chương Nhà giáo Việt Nam": 
    print("Vrai")
    pt += 1
else: 
    print("Faux")
    pt -= 0.25

t.sleep(1.5)

print("SCORE:", pt)

t.sleep(3)