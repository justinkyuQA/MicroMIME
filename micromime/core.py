import mimetypes
import sys

def show(filename):

    mime,_ = mimetypes.guess_type(filename)

    print()
    print("MicroMIME")
    print("="*40)
    print("File :", filename)
    print("Type :", mime or "Unknown")
