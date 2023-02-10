workers_num = 0 
work_volume = 0

while workers_num <= 0 or work_volume <= 0:
    work_volume = float(input("Введите общий объем работ (в часах): "))
    workers_num = int(input("Введите общее число работников: "))
else:
    avg_load = work_volume / workers_num
    print(f"Средняя загрузка = {avg_load:.2f} (ч.)")