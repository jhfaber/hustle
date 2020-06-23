

from imagesearch import imagesearch

def saveimage(img):
    files = [f for f in listdir("unclassified") if isfile(join("unclassified", f))]
    filename = "unclassified/" + str(files.__len__() + 1) + ".png"
    img.save(filename)





def capture(event):
    pos = imagesearch("character.png")
    print("saving images")
    x = pos[0]
    y = pos[1]
    
    saveimage(ImageGrab.grab(bbox=(x - 43, y - 24, x - 8, y)))
    saveimage(ImageGrab.grab(bbox=(x - 87, y - 2, x - 52, y + 22)))
    saveimage(ImageGrab.grab(bbox=(x - 43, y + 19, x - 8, y + 43)))
    saveimage(ImageGrab.grab(bbox=(x + 1, y + 40, x + 36, y + 64)))
    saveimage(ImageGrab.grab(bbox=(x + 43, y + 19, x + 78, y + 43)))
    saveimage(ImageGrab.grab(bbox=(x + 87, y - 3, x + 122, y + 21)))
    saveimage(ImageGrab.grab(bbox=(x + 43, y - 24, x + 78, y)))




if __name__ == '__main__':
    root = tk.Tk()
    my_image = Image.open("background.png") # just to make it pretty 
    filename = ImageTk.PhotoImage(my_image)
    panel = tk.PanedWindow()
    panel = tk.Label(root, image=filename)
    root.bind('<F1>', capture)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()