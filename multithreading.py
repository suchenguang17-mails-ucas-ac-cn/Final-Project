import Draw
import threading

def draw_B_static(N1, N2):
    para_static_B = []
    for i in range(N1, N2):
        para_static_B.append([20, 1, 11, 50, 28, 10, i/15, 0, "../Project_Pictures/B/" + str(i) + "_15.png"])

    for para in para_static_B:
        Draw.Draw_static(para[0:8], para[8])

t1 = threading.Thread(target=draw_B_static, args=(0, 33))
t2 = threading.Thread(target=draw_B_static, args=(34, 67))
t3 = threading.Thread(target=draw_B_static, args=(68, 100))

t1.start()
t2.start()
t3.start()