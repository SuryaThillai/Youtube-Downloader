import PIL.Image
from pytube import YouTube
from tkinter import *
from tkinter import ttk,filedialog,messagebox
from PIL import Image,ImageTk

win = Tk()
win.minsize(width=600,height=500)
win.title("Youtube Downloader")
# win.config(bg="white")


yt_image = ImageTk.PhotoImage(Image.open("youtube.png"))
canvas = Canvas(width=300,height=300)
canvas.create_image((150,150),image=yt_image)
canvas.pack()

# Link Label

link_text = Label(text="Link:",font=("Ariel",20,"bold"))
link_text.place(x=70,y=300)

link_entry = Entry(width=45)
link_entry.place(x=130,y=303)

# Resolution

res_text = Label(text="Resolution:",font=("Ariel",20,"bold"))
res_text.place(x=20,y=340)

resolution = ["360p","480p","720p","1080p"]
res_entry = ttk.Combobox(values=resolution)
res_entry.place(x=135,y=345)

# Save to

# save_text = Label(text="Save To:",font=("Ariel",18,"bold"))
# save_text.place(x=50,y=380)

def open_file():
    folder = filedialog.askdirectory(initialdir="/",title="Select folder")
    return folder.title()
    # if folder:
    #     save_button.config(text=folder.title())
    # return folder.title()


# save_button = Button(text="select",width=25,height=1,command=open_file)
# save_button.place(x=130,y=380)

def download_video():
    yt = YouTube(link_entry.get())
    yt.streams.filter(resolution=res_entry.get(),adaptive=True, file_extension="mp4")
    stream = yt.streams.get_by_itag(22)
    if stream.download(output_path=open_file()):
        messagebox.showinfo(title="YT Downloader",message="Download Successfully")



download_button = Button(text="Download",font=("Raleway",20,"bold"),command=download_video)
download_button.config(bg="#D61355",fg="#D61355")
download_button.place(x=220,y=380)


win.mainloop()





