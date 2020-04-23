import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import os
import Calculate

def update_lines(num, data, line):
    line.set_data_3d(data[:, :100*num])
    return line


def Draw(para, filename = 'myvideo.mp4'):
    data = Calculate.Alogrithim(para[0], para[1], para[2], para[3], para[4], para[5], para[6], para[7])
    fig = plt.figure(figsize = (6,6))
    ax = fig.add_subplot(111, projection = "3d")
    line, = ax.plot(data[0,0:2], data[1,0:2], data[2,0:2])

    # Setting the axes properties
    ax.set_xlim3d([-20, 20])
    ax.set_xlabel('X')

    ax.set_ylim3d([-20, 20])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0, 40])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')

    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, frames = 1000, fargs=(data, line), blit=False)

    ffmpegpath = os.path.abspath("../../ffmpeg/ffmpeg-20200422-2e38c63-win64-static/ffmpeg-20200422-2e38c63-win64-static/bin/ffmpeg.exe")
    matplotlib.rcParams["animation.ffmpeg_path"] = ffmpegpath
    mywriter = animation.FFMpegWriter(fps = 100)
    line_ani.save(filename, writer=mywriter)




