from pdf_to_text import Pdf
from text_to_audio import Audio
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilenames
from tkinter.messagebox import showinfo
PURPLE = "#511845"
VOICE_LIST = [
    "Female (US)",
    "Male (US)",
    "Female (US child)",
    "Male (US child)",
    "Female (British)",
    "Male (British)",
]



pdf = Pdf()

audio = Audio()


def button_state():
    if pdf.pdf_data and audio.voice_key != "":
        mp3_button.config(state="normal",
                          image=mp3_image)

    else:
        mp3_button.config(state="disabled",
                          image=mp3_image_dis)


def load_pdf():
    pdf.text = ""
    file_name.delete(0, END)
    pdf_data = askopenfilenames(filetypes=(
                                            ('PDF documents', '*.pdf'),
                                            ('All files', '*.*')
                                            )
                                )
    pdf.pdf_data = pdf_data[0]
    pdf.pdftt()
    if len(pdf.text) > 3000:
        showinfo(title="Alert", message="PDF file exceeds 3000 character maximum.\nPlease try another file.")
        pdf.text = ""
        return
    else:
        pdf_filename = pdf_data[0].split("/")[-1]
        file_name.insert(0, pdf_filename)
    button_state()


def set_voice(x):

    audio.voice_key = x
    button_state()

def create_mp3():

    path = asksaveasfilename(title="whatever", filetypes=(
                                                            ('MP3 audio', '*.mp3'),
                                                            ('All files', '*.*')
                                                            )
                                                        )
    audio.create_mp3(text=pdf.text, path=path)
    path_split = path.split("/")
    showinfo(title="Success!", message=f"Your file has been saved to {path_split[-2]} as {path_split[-1]}.")



# --------------- Set up UI ----------------------#
window = Tk()
window.title("PDF to MP3")
canvas = Canvas()
canvas.config(width=610,
              height=710)
bg_img = PhotoImage(file="gradientbg.png")
canvas.create_image(305, 355, image=bg_img)
canvas.grid(row=0, column=0, columnspan=6, rowspan=8)
load_img = PhotoImage(file="button_upload-pdf.png")
load_btn = Button(text="Upload PDF", image=load_img, command=load_pdf, borderwidth=0, highlightthickness=0,
                  )
load_btn.grid(row=5, column=3)
file_name = Entry()
file_name.config(width=40)
file_name.grid(row=5, column=1, columnspan=2)
mp3_image = PhotoImage(file="button_create-mp.png")
mp3_image_dis = PhotoImage(file="button_create-mp-disabled.png")
mp3_button = Button(text="Create MP3", image=mp3_image_dis, command=create_mp3, borderwidth=0, highlightthickness=0,
                    state="disabled")
mp3_button.grid(row=6, column=3)

voice_var = StringVar(window)
voice_var.set("Choose a voice")
voice_dropdown = OptionMenu(window, voice_var, *VOICE_LIST, command=set_voice)
voice_dropdown.config(
    bg=PURPLE,
    fg="black",
    borderwidth=0,
    highlightthickness=0,
    width=35
)
voice_dropdown.grid(row=6, column=1, columnspan=2)




window.mainloop()



