from tkinter import *
from pytube import Search
from PIL import ImageTk, Image

output = 'C:/Users/Nico/Desktop/Download_music'
results_btn = {}
thumbnails = {}


def main():
    def search_show_titles(to_search):
        s = Search(to_search.get())
        search_titles = []
        # thumbnails_url = []
        for each_video in range(len(s.results)):
            search_titles.append(s.results[each_video].title)
            print(search_titles)

            # thumbnails_url.append(ImageTk.PhotoImage(Image.open(s.results[each_video].thumbnail_url)))

            def download_video(selected_download=search_titles[each_video]):
                for i in range(len(s.results)):

                    if s.results[i].title == selected_download:
                        print(f'Downloading {selected_download}')
                        # print(s.results[i].thumbnail_url)
                        s.results[i].streams.get_audio_only().download(output)

            results_btn[search_titles[each_video]] = Button(window, text=search_titles[each_video], fg='black',
                                                            font=("Helvetica", 10), command=download_video)
            results_btn[search_titles[each_video]].pack(side=BOTTOM, pady=2)

            # thumbnails[search_titles[each_video]] = Label(window, image=search_titles[each_video])
            # thumbnails[search_titles[each_video]].pack(side="bottom", fill="both", expand="yes")

    window = Tk()
    window.title("Music downloader")
    window.iconbitmap("icon.ico")
    width = 1050
    height = 800
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    align = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(align)
    window.resizable(width=False, height=False)

    welcome_lbl = Label(window, text="Download music for free!", fg='black', font=("Helvetica", 10))
    welcome_lbl.place(x=10, y=20)

    results_btn2 = [Button(window, text="The search results are:", fg='black', font=("Helvetica", 10))]
    results_btn2[0].place(x=10, y=150)

    to_search = Entry(window, bd=5)
    to_search.place(x=70, y=60)

    btn = Button(window, text="Accept", fg='green', command=lambda: search_show_titles(to_search))
    btn.place(x=120, y=95)
    window.mainloop()


if __name__ == '__main__':
    main()
