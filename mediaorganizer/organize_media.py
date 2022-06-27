"""
Put simply, this file needs to be CLI based. Take in a directory to scan (recursively), take all files of a certain type
(not extensions, files) and place  them in a destination, recursively based on their folder structure.

"""

import os
import argparse
import magic



#ok. Take in the directory to scan recursively. Check and see if the destination directory is inside of it. If so, ignore it.
#Next, iterate through each file, check to see if it is of a given file type, and if so, get its directory structure,
#move it over.
def move_media(scandir,dest,filetype):
    if not os.path.exists(dest):
        os.mkdir(dest)
    print("starting...")
    for subdir, dirs, files in os.walk(scandir):
        if not subdir == dest:
            for file in files:
                fullfilepath=os.path.join(subdir,file)
                mime=magic.Magic(mime=True)
                mimefile=mime.from_file(fullfilepath)

                if mimefile.find(filetype) != -1:
                    print(fullfilepath)
                    #its a video
                    newfilepath=dest+"/"+fullfilepath
                    os.rename(fullfilepath,newfilepath)

def main():
    parser = argparse.ArgumentParser(description='mediaorganizer allows you to sift through your media and put it all in one place')
    parser.add_argument('-s', '--scandir', help='The directory to recursively scan through', required=True)
    parser.add_argument('-d', '--dest', help='The destination directory to put files', required=True)
    parser.add_argument('-f','--filetype',help="The filetype to look for", required=True)
    args = vars(parser.parse_args())
    print(args)
    move_media(args['scandir'],args['dest'],args['filetype'])

if __name__ == "__main__":
    main()