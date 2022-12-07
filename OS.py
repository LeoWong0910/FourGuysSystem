import os
from time import sleep
from pathlib import Path


# TASK 1: command dir_size
# Write a function dir_size(directory) which computes the total size in bytes of all files in a
# given directory (recursively).

def dir_size(directory):
    try:
        totalSize = os.path.getsize(directory)
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            if os.path.isfile(path):
                totalSize += os.path.getsize(path)
            elif os.path.isdir(path):
                totalSize += dir_size(path)
        return totalSize
    except FileNotFoundError:
        print("The directory is not found.")
    except:
        print("Something went wrong.")

# TASK 2: command dir_info
# Write a function dir_info(directory) which returns three values: 
# (1) Number of files inside the directory (recursively)
# (2) Number of directories inside the directory (recursively)

def dir_info(directory):
    from pathlib import Path
    
    path = Path(directory)
    num_dirs, num_files = 0, 0

    for f in path.glob('*'):
        print(f.name)
        if f.is_dir():
            num_dirs += 1
        if f.is_file():
            num_files += 1
    print("Number of files: ", num_files)
    print("Number of directories: ", num_dirs)

# TASK 3: command find_string
# Write a function find_string(s, file) for finding all lines in file that contain the string s.
# You should report the line number and the line itself as in the following example:
def find_string(string, file):
      lineno = 0
      list=[]
      with open (file,'r') as rfile:
        for i in rfile:#i = line
            lineno +=1
            if string in i:
                list.append((lineno,i.rstrip()))
      for i in list:
            print(i[0],i[1])

      return list

# TASK 4: command find_files
# Write a function find_files(directory, pattern)
# For finding all files in directory (recursively) with names matching pattern.
def find_files(directory, pattern = None, allfile = []):
    filelist = os.listdir(directory) 
    for filename in filelist: 
        filepath = os.path.join(directory, filename) 
        # 判断文件夹 
        if os.path.isdir(filepath): 
            # 文件夹继续递归 
            find_files(filepath, pattern, allfile) 
        else: 
            temp_file_type = filepath.split(".")[-1]
            # 判断文件类型
            if pattern is None or temp_file_type in pattern: 
                allfile.append(filepath) 
            # 展示所有未包含的文件 
            else: 
                print("the file is not include : %s" % filepath ) 
    return allfile

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
        
def list():
    command = ['help','quit','clear','find_files','find_string','dir_info','dir_size']
    
    print("->" , end=' ')
    for elm in command:
        print(elm + "," , end=' ')
    print()

if __name__ == '__main__':
        clear()
        print("Welcome to FourGuysOs v1.0")
        print("Press \"help\" to list all the command.")

        while(True):
            cmd = input()
            
            if cmd == "help":
                #Done
                list()
                
            if cmd == "clear":
                #Done
                clear()
                print("Press \"help\" to list all the command.")
                
            
            if cmd == "quit":
                clear()
                break
            
            if cmd == "find_files":
                #Done
                dir = input("Input the directory: ")
                pat = input("Input the name that you looking for: ")
                dir = dir.translate({ord('"'): None})
                pat = pat.translate({ord('"'): None})
                print(find_files(dir,pat))
            
            if cmd == "find_string":
                file = input("Input the file name that you are looking for: ")
                string = input("Input the Keywords that you are looking for: ")
                file = file.translate({ord('"'): None})
                string = string.translate({ord('"'): None})
                find_string(string,file)
            
            if cmd == "dir_info":
                file = input("Input the directory that you are looking for: ")
                file = file.translate({ord('"'): None})
                dir_info(file)
            
            if cmd == "dir_size":
                #Done
                dir = input("Input the directory: ")
                dir = dir.translate({ord('"'): None})
                print("Total Size: %d Bytes" %dir_size(dir))
          
