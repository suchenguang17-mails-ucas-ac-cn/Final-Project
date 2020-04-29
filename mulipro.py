import multiprocessing as  mp
import Draw

def draw_P_static(N1, N2):
    para_static_P = []
    for i in range(N1, N2):
        para_static_P.append([20, 1, 11, 50, 4 + i * 23 / 100, 28, 8/3, 0, "../Project_Pictures/P/" + str(i) + "_23.png"])

    for para in para_static_P:
        Draw.Draw_static(para[0:8], para[8])

if __name__ == '__main__':
    p1 = mp.Process(target=draw_P_static, args=(0, 25))
    p2 = mp.Process(target=draw_P_static, args=(25, 50))
    p3 = mp.Process(target=draw_P_static, args=(50, 75))
    p4 = mp.Process(target=draw_P_static, args=(75, 100))

    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
'''
def draw_B_static(N1, N2):
    para_static_B = []
    for i in range(N1, N2):
        para_static_B.append([20, 1, 11, 50, 10, 28, i/15, 0, "../Project_Pictures/P/" + str(i) + "_15.png"])

    for para in para_static_B:
        Draw.Draw_static(para[0:8], para[8])

if __name__ == '__main__':
    p1 = mp.Process(target=draw_B_static, args=(0, 25))
    p2 = mp.Process(target=draw_B_static, args=(26,50))
    p3 = mp.Process(target=draw_B_static, args=(51,75))
    p4 = mp.Process(target=draw_B_static, args=(76,100))
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()'''