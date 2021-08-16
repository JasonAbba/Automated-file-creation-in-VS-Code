import sys
import os

def create(args):
    filename = args[1] # filename

    folders = {'python' : '\\Python\\',
               'c#' : '\\C#\\',
               'java' : '\\Java\\',
               'c++' : '\\C++\\'}
    folder = folders[args[2]] # folder
    ext = {'python' : '.py',
               'c#' : '.cs',
               'java' : '.java',
               'c++' : '.cpp'}
    ext_name = ext[args[2]]
    # print(folder)
    # print(ext_name)

    path = r'C:\Users\JasonPC\Documents\CodeVault' + folder + filename + ext_name
    open(path, 'w+') # create the file
    folder = folder[0:-1] # extracting folder name
    os.chdir(r'C:\Users\JasonPC\Documents\CodeVault' + folder) # change directory
    os.system('code .') # shorthand command to execute vscode from cmd
    
if __name__ == '__main__':
    create(sys.argv)