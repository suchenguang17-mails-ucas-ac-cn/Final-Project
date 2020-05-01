import Draw
'''
paras_anima = [
    [20, 1, 11, 50, 10, 28, 8/3, 0, "../Project_Videos/firsttry.mp4"],
    [20, 1, 11, 50, 10, 28, 5/3, 0, "../Project_Videos/secondtry.mp4"],
    [10, 0, 5, 50, 10, 28, 8/3, 0, "../Project_Videos/thirdtry.mp4"],
    [10, 0, 5, 50, 10, 15, 8/3, 0, "../Project_Videos/4try.mp4"],
    [10, 0, 5, 50, 10, 20, 8/3, 0, "../Project_Videos/5try.mp4"],
    [10, 0, 5, 50, 20, 15, 8/3, 0, "../Project_Videos/6try.mp4"],
    [10, 0, 5, 50, 10, 15, 10, 0, "../Project_Videos/7try.mp4"],
    [10, 0, 5, 50, 10, 15, 1, 0, "../Project_Videos/8try.mp4"],
    [30, 10, 20, 50, 10, 28, 8/3, 0, "../Project_Videos/9.mp4"],
    [0.1, 0.1, 0.1, 50, 10, 28, 8/3, 0, "../Project_Videos/10.mp4"],
    [0.1, 0.1, 0.1, 50, 10, 28, 8/3, 0, "../Project_Pictures/1.png"]

]

para_static_P = [
    #[20, 1, 11, 50, 1, 28, 8/3, 0, "../Project_Pictures/P/0_1.mp4"],
    #[20, 1, 11, 50, 4, 28, 8/3, 0, "../Project_Pictures/P/4.png"],
    #[20, 1, 11, 50, 25, 28, 8/3, 0, "../Project_Pictures/P/25.png"],
    #[20, 1, 11, 50, 6, 28, 8/3, 0, "../Project_Pictures/P/6.png"],
    [20, 1, 11, 50, 21, 28, 8/3, 0, "../Project_Pictures/P/21.png"]
    #[20, 1, 11, 50, 75, 28, 8/3, 0, "../Project_Pictures/P/75.png"],
    #[20, 1, 11, 50, 10000, 28, 8/3, 0, "../Project_Pictures/P/10000.png"]
]

para_static_R = []
for i in range(100):
    para_static_R.append([20, 1, 11, 50, 10, i, 8/3, 0, "../Project_Pictures/R/" + str(i) + ".png"])

for para in para_static_R:
    Draw.Draw_static(para[0:8], para[8])
'''
para_test = [8.6, 8.6, 28, 100, 10, 28, 8 / 3, 0, "../Project_Pictures/test.png"]
Draw.Draw_static(para_test[0:8], para_test[8])
'''
for para in paras_anima:
    Draw.Draw_anima(para[0:8], para[8])

for para in para_static_P:
    Draw.Draw_static(para[0:8], para[8])
'''


'''    [20, 1, 11, 50, 10, 28, 8/3, 0, "../Project_Videos/firsttry.png"],
    [20, 1, 11, 50, 10, 28, 5/3, 0, "../Project_Videos/secondtry.png"],
    [10, 0, 5, 50, 10, 28, 8/3, 0, "../Project_Videos/thirdtry.png"],
    [10, 0, 5, 50, 10, 15, 8/3, 0, "../Project_Videos/4try.png"],
    [10, 0, 5, 50, 10, 20, 8/3, 0, "../Project_Videos/5try.png"],
    [10, 0, 5, 50, 20, 15, 8/3, 0, "../Project_Videos/6try.png"],
    [10, 0, 5, 50, 10, 15, 10, 0, "../Project_Videos/7try.png"],
    [10, 0, 5, 50, 10, 15, 1, 0, "../Project_Videos/8try.png"],
    [30, 10, 20, 50, 10, 28, 8/3, 0, "../Project_Videos/9.png"],
    [0.1, 0.1, 0.1, 50, 10, 28, 8/3, 0, "../Project_Videos/10.png"]'''
