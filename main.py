import tkinter
import customtkinter
from pytube import YouTube
import os
from pathlib import Path

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk() # Initialises app
app.geometry("480x480") # Resolution of the app
app.title("YT Downloader")
        
# Download -----Video-----
def VideoDownload():
    try:
        YTlink = link.get() # Grabs the inputted YT link
        YTobject = YouTube(YTlink, on_progress_callback=on_progress)
        video = YTobject.streams.get_highest_resolution() #REMINDER# allow user to change resolution to specific choice 
        
        title.configure(text=YTobject.title, text_color="white") # Fetches the title of the youtube link

        video.download(DownloadPath) # Downloads the actual video
        print("Completed Video Download")

    except:
        print("Invalid Link") #REMINDER# output this in the app instead of CLI

# Download -----Audio-----
def AudioDownload():
    try:
        YTlink = link.get()
        YTobject = YouTube(YTlink, on_progress_callback=on_progress)
        audio = YTobject.streams.get_audio_only()

        title.configure(text=YTobject.title, text_color="white")

        audio.download(DownloadPath) # Downloads the actual audio
        print("Completed Audio Download")

    except:
            print("Invalid Link")

# Progress Percentage
def on_progress(stream, chunk, bytes_remaining):
    TotalSize = stream.filesize
    BytesDownloaded = TotalSize - bytes_remaining
    CompletionRate = BytesDownloaded / TotalSize * 100   # For 0% to 100%
    per = str(int(CompletionRate)) # Turns percentage into a whole number
    ProgressPercent.configure(text=per + '%')
    ProgressPercent.update() # Updates progress percentage

    # Update Progress Bar
    ProgressBar.set(float(CompletionRate) / 100)

# UI Elements
title = customtkinter.CTkLabel(app, text="Enter URL", font=("arial", 22, "bold"))
title.pack(padx=10, pady=50) # Create a text title

# URL Input
url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url) 
link.pack() # Create link input bar

# Download Progress
ProgressPercent = customtkinter.CTkLabel(app, text="0%", font=("arial", 16, "bold"))
ProgressPercent.pack(pady=10)

ProgressBar = customtkinter.CTkProgressBar(app, width=350, progress_color="red")
ProgressBar.set(0)
ProgressBar.pack()

DownloadPath = str(os.path.join(Path.home() / 'Downloads')) # Sets download path to /Downloads
# Video Download Button
download = customtkinter.CTkButton(app, font=("arial", 16, "bold"), fg_color="dark red", hover_color="red", text="MP4 Download", command=VideoDownload)
download.pack(padx=10, pady=50) # Creates the button

# Audio Download Button
download = customtkinter.CTkButton(app, font=("arial", 16, "bold"), fg_color="dark red", hover_color="red", text="MP3 Download", command=AudioDownload)
download.pack(padx=10, pady=5) # Creates the button

# App Runner
app.mainloop()

##### For v2 LIST AUDIO FILES AS MP4 FIX THIS

##### For v2 Change That Messages are inside of app not inside of TERMINAL