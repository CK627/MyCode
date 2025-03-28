import tkinter
import webbrowser


def open_iqy():
    webbrowser.open('https://www.iqiyi.com')


def open_tx():
    webbrowser.open('https://v.qq.com')


def open_yq():
    webbrowser.open('https://www.youku.com/')


def button():
    url = 'https://jx.xmflv.cc/?url='
    video = entry_movie_link.get()
    webbrowser.open(url + video)


def empty():
    entry_movie_link.delete(0, 'end')


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('VIP视频破解软件')
    root.geometry('480x200')
    label_movie_link = tkinter.Label(root, text='网页视频链接：')
    label_movie_link.place(x=20, y=30, width=100, height=30)
    entry_movie_link = tkinter.Entry(root)
    entry_movie_link.place(x=125, y=30, width=260, height=30)
    button_movie_link = tkinter.Button(root, text='清空', command=empty)
    button_movie_link.place(x=400, y=30, width=50, height=30)
    button_movie1 = tkinter.Button(root, text='爱奇艺', command=open_iqy)
    button_movie1.place(x=25, y=80, width=80, height=40)

    button_movie2 = tkinter.Button(root, text='腾讯视频', command=open_tx)
    button_movie2.place(x=125, y=80, width=80, height=40)

    button_movie3 = tkinter.Button(root, text='优酷视频', command=open_yq)
    button_movie3.place(x=225, y=80, width=80, height=40)

    button_movie = tkinter.Button(root, text='播放VIP视频', command=button)
    button_movie.place(x=325, y=80, width=125, height=40)
    lab_remind = tkinter.Label(root, text='提示：将视频链接复制到框内，点击播放VIP视频')
    lab_remind.place(x=50, y=150, width=400, height=20)
    root.mainloop()
