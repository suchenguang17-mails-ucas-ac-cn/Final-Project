#Use multiprocessing to draw animations or static plots of a lot of different parameter sets
import Draw
import multiprocessing as  mp

#Use N1 and N2 to divide tasks
def draw_R(N1, N2, draw_type):
    para_R = [

                 [-10, 0, 5, 100, 0.2, 0.6, 13, 0], [2, 3, -4, 100, 0.9, 10, 8 / 3, 0],
                 [2, 3, -4, 100, 0.1, 1, 6, 0], [160, 10, 2, 100, 0.7, 2, 5, 0],
                 [1.e-4, 0, 1, 100, 0.9, 10, 8 / 3, 0], [1.e-4, 0, 1, 100, 0.95, 10, 8 / 3, 0],
                 [1.e-4, 0, 1, 100, 1.01, 10, 8 / 3, 0], [1.e-4, 0, 1, 100, 1.2, 10, 8 / 3, 0],
                 [2, 3, -4, 100, 8, 10, 8 / 3, 0], [160, 10, 2, 100, 10, 2, 5, 0],
                 [-10, 0, 0, 100, 13.962, 10, 8 / 3, 0], [0, 0, 10, 100, 13.962, 10, 8 / 3, 0],
                 [3, 6, 8, 100, 15, 10, 8 / 3, 0], [3, 6, 8, 100, 24, 10, 8 / 3, 0],
                 [6.1101, 6.1101+1.e-5, 14, 100, 15, 10, 8 / 3, 0], [7.6594, 7.6594+1.e-5, 23, 100, 24, 10, 8 / 3, 0],
                 [3, 2, 6, 100, 28, 10, 8 / 3, 0], [50, 20, -60, 100, 28, 10, 8 / 3, 0],
                 [8.6, 8.5, 28, 100, 80, 10, 8 / 3, 0], [8.6, 8.6, 28.1, 100, 80, 10, 8 / 3, 0],
                 [8.6, 8.7, 28, 100, 80, 10, 8 / 3, 0], [8.6, 8.6, 28, 100, 80, 10, 8 / 3, 0],
                 [100, 100, 100, 100, 28, 1, 8 / 3, 0], [100, 100, 100, 100, 28, 10, 8 / 3, 0],
                 [1, 1, -1,  100, 470 / 19, 10, 8 / 3,  0], [1, 1, -.95, 100, 470 / 19, 10, 8 / 3, 0],
                 [19.53, 19.53, 143, 100, 144, 10, 8 / 3,  0], [19.53, 19.53, 142,  100, 144, 10, 8 / 3, 0],
                 [7.956, 7.956, 23.737, 100, 24.737, 10, 8 / 3, 0], [7.956, 7.957, 23.737, 100, 24.737, 10, 8 / 3, 0],
                 [1, 1, -1, 100, 167, 10, 8 / 3, 0], [1, 1, -.95, 100, 167, 10, 8 / 3, 0],
    ]

    if draw_type == "anima":
        for i in range(len(para_R)):
            para_R[i].append("../Project_Videos/tendency/" + str(i) + "Test.mp4")

        for i in range(N1, N2):
            Draw.Draw(para_R[i][0:8], para_R[i][8], "anima")

    if draw_type == "static":
        for i in range(len(para_R)):
            para_R[i].append("../Project_Pictures/tendency/" + str(i) + "TEST.png")

        for i in range(N1, N2):
            Draw.Draw(para_R[i][0:8], para_R[i][8], "static")
    
    else:
        return "Wrong Draw Type!"

#Build Multiprocess
def multi_draw_R(draw_type):
    if __name__ == '__main__':
        p1 = mp.Process(target=draw_R, args=(0, 8,  draw_type))
        p2 = mp.Process(target=draw_R, args=(8, 16, draw_type))
        p3 = mp.Process(target=draw_R, args=(16, 24, draw_type))
        p4 = mp.Process(target=draw_R, args=(24, 32, draw_type))

        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()

multi_draw_R("static")
multi_draw_R("anima")
