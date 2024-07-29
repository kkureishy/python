import os #import os module

#main funciton
def main():
    #create directory
    os.mkdir('MyFiles')
    #create nested directory
    os.mkdir('MyFiles/Docs')
    os.mkdir('MyFiles/Images')
    os.mkdir('MyFiles/Videos')

main()