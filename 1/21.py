import tkMessageBox
def openfile(filename):
    try:
        fp=open(filename)
    except:
        tkMessageBox.showwarning(
            "open file",
            "Cannot open filr\n(%s)" %filename
        )
    return
