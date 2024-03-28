from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip
import shutil


# FUNCTION
def select_video():
    path = filedialog.askdirectory()
    video_path.config(text=path)


def download():
    try:
        link_to_video = video_link_entry.get()
        file_path = video_path.cget('text')
        mpy_new_video = YouTube(link_to_video).streams.get_highest_resolution().download()
        video_clip = VideoFileClip(mpy_new_video)
        # Code for mp3
        audio_file = video_clip.audio
        audio_file.write_audiofile('audio.mp3')
        audio_file.close()
        shutil.move('audio.mp3', file_path)
        # code for mp4
        video_clip.close()
        shutil.move(mpy_new_video, file_path)

    except Exception as a:
        print(a)
        messagebox.showinfo(title="Oops", message="Video can't be download!")
    else:
        messagebox.showinfo(title="Success", message="Download Complete")
    finally:
        video_link_entry.delete(0, END)


window = Tk()
window.title("Video Downloader")
window.resizable(width=False, height=False)

canvas = Canvas(window, width=300, height=250)
canvas.pack()

# APP LABEL
app_label = Label(text="Youtube", fg='blue', font=('Arial', 25))
canvas.create_window(150, 20, window=app_label)
app_label = Label(text="Video Downloader", fg='blue', font=('Arial', 25))
canvas.create_window(150, 60, window=app_label)

video_link = Label(text='Enter video URL')
canvas.create_window(150, 90, window=video_link)

video_link_entry = Entry(window, width=45)
canvas.create_window(150, 120, window=video_link_entry)

download_name = Label(text='Click to download')
canvas.create_window(90, 190, window=download_name)

download_link = Button(text="Download", command=download)
canvas.create_window(245, 190, window=download_link)

video_path = Label(text='Select path')
canvas.create_window(90, 155, window=video_path)

video = Button(text='Select Video', command=select_video)
canvas.create_window(245, 155, window=video)


window.mainloop()
