import multiprocessing as  mp
import Draw

para_static_R = [[-10, 0, 5, 200, 0.2, 0.6, 13, 0], [2, 3, -4, 200, 0.9, 10, 8 / 3, 0],
                 [100, 200, 300, 200, 0.5, 1, 6, 0], [160, 10, 2, 200, 0.7, 2, 5, 0],
                 [1.e-4, 0, 1, 200, 0.9, 10, 8 / 3, 0], [1.e-4, 0, 1, 200, 0.99, 10, 8 / 3, 0],
                 [1.e-4, 0, 1, 200, 1.01, 10, 8 / 3, 0], [1.e-4, 0, 1, 200, 1.2, 10, 8 / 3, 0],
                 [2, 3, -4, 200, 8, 10, 8 / 3, 0], [160, 10, 2, 200, 10, 2, 5, 0],
                 [-10, 0, 0, 200, 13.962, 10, 8 / 3, 0], [0, 0, 10, 200, 13.962, 10, 8 / 3, 0],
                 [3, 6, 8, 200, 15, 10, 8 / 3, 0], [3, 6, 8, 200, 24, 10, 8 / 3, 0],
                 [6.11, 6.11, 14, 200, 15, 10, 8 / 3, 0], [7.83, 7.83, 23, 200, 24, 10, 8 / 3, 0],
                 [3, 2, 6, 200, 28, 10, 8 / 3, 0], [50, 20, -60, 200, 28, 10, 8 / 3, 0],
                 [8.6, 8.6, 28, 100, 28, 10, 8 / 3, 0], [8.6, 8.6, 28, 200, 28, 10, 8 / 3, 0],
                 [1000, 1000, 1000, 200, 28, 10, 8 / 3, 0], [1000, 1000, 1000, 1000, 28, 10, 8 / 3, 0],
                 [470 / 19, 10, 8 / 3, 200, 2, 2, 2, 0], [470 / 19, 10, 8 / 3, 200, 2, 2, 1.95, 0],
                 # 上面两个能不能画到一张图里面
                 [144, 10, 8 / 3, 200, 1, 1, -1, 0], [144, 10, 8 / 3, 200, 1, 1, -.95, 0],
                 [144, 10, 8 / 3, 200, 1, 1, -1, 0], [144, 10, 8 / 3, 200, 1, 1, -.95, 0]]

for i in range(len(para_static_R)):
    para_static_R[i].append("../Project_Pictures/tendency/" + str(i) + ".png")


for para in para_static_R:
    Draw.Draw_static(para[0:8], para[8])

if __name__ == '__main__':
    p1 = mp.Process(target=draw_R_static, args=(0, 7))
    p2 = mp.Process(target=draw_R_static, args=(7, 14))
    p3 = mp.Process(target=draw_R_static, args=(14, 21))
    p4 = mp.Process(target=draw_R_static, args=(21, 28))

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
