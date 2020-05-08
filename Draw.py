import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import os
import Calculate

#Update lines and time label on the animation
def update_lines_time(num, data, line, time, T):
    line.set_data_3d(data[:, :100*num]) #not get every point in the graph otherwise the video will be very long
    time.set_text("T = {0:.1f}".format(T / 100000 * 100 * num)) #To show the time
    return line, time

def Draw(para, filename, draw_type):
    data = Calculate.Alogrithim(para[0], para[1], para[2], para[3], para[4], para[5], para[6], para[7])
    fig = plt.figure(figsize = (6,6))
    ax = fig.add_subplot(111, projection = "3d")
    
    #Determine the edges of plots
    edges = []
    for i in range(3):
        ax_min = np.min(data[i])
        ax_max = np.max(data[i])
        gap = (ax_max - ax_min) / 20
        edges.append([ax_min - gap, ax_max + gap])
    
    #Lable some important points
    ax.scatter(data[0,0], data[1,0], data[2,0], lw = 0.8, alpha = 0.5, color = 'b', label = "Start Point")
    ax.scatter(data[0,-1], data[1,-1], data[2,-1], lw = 0.8, alpha = 0.5, color = 'r', label = "Last Point")
    ax.scatter(0, 0, 0, lw = 0.8, color = 'black', alpha = 0.5, label = "Origin")
    
    #for R < 1, the only fixed point is the origin
    if para[4] > 1:
        p = Calculate.fix_point(para[4], para[5], para[6])
        ax.scatter(p[:,0],p[:,1],p[:,2], color = "brown", alpha = 0.5, lw = 0.8, label = "Fixed Points")

    ax.legend(loc = "best")
    # Setting the axes properties
    ax.set_xlim3d(edges[0])
    ax.set_xlabel('X')

    ax.set_ylim3d(edges[1])
    ax.set_ylabel('Y')

    ax.set_zlim3d(edges[2])
    ax.set_zlabel('Z')
    ax.legend(loc = "upper left")

    if draw_type == "anima":
        line, = ax.plot(data[0,0:2], data[1,0:2], data[2,0:2], lw = 0.6, color = 'g')
        time = ax.text(edges[0][0], edges[1][1], edges[2][1], "T = 0")

        # Creating the Animation object
        line_ani = animation.FuncAnimation(fig, update_lines_time, frames = 1000, fargs=(data, line, time, para[3]), blit=False)
        
        #Store the video
        ffmpegpath = os.path.abspath("../../ffmpeg/ffmpeg-20200422-2e38c63-win64-static/ffmpeg-20200422-2e38c63-win64-static/bin/ffmpeg.exe")
        matplotlib.rcParams["animation.ffmpeg_path"] = ffmpegpath
        mywriter = animation.FFMpegWriter(fps = 100)
        line_ani.save(filename, writer=mywriter)
    
    if draw_type == "static":
        #Draw the static final plot
        ax.plot(data[0], data[1], data[2], lw = 0.6, color = 'g')
        ax.text(edges[0][0], edges[1][1], edges[2][1], "[R,P,B] = [{0},{1},{2:.2f}]\n[X,Y,Z] = [{3},{4},{5}]".format(para[4],para[5],para[6],para[0],para[1],para[2]))
        plt.savefig(filename)

    else:
        return "Wrong Draw Type!"





