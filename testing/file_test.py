import os.path

def makeafile():
    open("newfile.txt","w")

def test_homer():
    assert os.path.exists("newfile.txt") == True

