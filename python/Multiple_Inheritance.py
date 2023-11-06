# Ông cho cha kế thừa, cha cho con kế thừa thì con được kế thừa từ cả cha và ông.
# Một "người" có thể được kế thừa trực tiếp từ nhiều "người".
# Cú pháp 
class Lopcha1:
    print("Ông nội nè")

class Lopcha2:
    print("Cha nè")

class Lopcondakethua(Lopcha1, Lopcha2):
    print("=> Đây là đa kế thừa")

da_thua_ke = Lopcondakethua()

#  Multilevel Inheritance (Kế thừa đa cấp)
class LopCha:
    print("Lại là cha đây")
class LopCon(LopCha):
    print("Lại là con đây")
class KethuaLopCon(LopCon):
    print("=> Đây là kế thừa đa cấp")

ke_thua_da_cap = KethuaLopCon()