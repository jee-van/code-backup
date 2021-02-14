import os
import time
import shutil

check_directory = '/home/jeevan/Downloads'
file_types = {
    'Documents' : ('.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.txt', '.wks', '.wps', '.wpd'),
    'Music' : ('.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl'),
    'Video' : ('.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'),
    'Compressed' : ('.z7', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.tz', '.z', '.zip'),
    'Pictures' : ('.ai', '.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.ps', '.psd', '.svg', 'tif', '.tiff'),
    'Programs' : ('.c', '.cpp', '.class', '.cs', '.java', '.sh', '.h', '.swift', '.py', '.vb')
}


for file in os.listdir(check_directory):
    if file.endswith(file_types['Documents']):
        shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, list(file_types.keys())[0]))
    elif file.endswith(file_types['Music']):
        shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, list(file_types.keys())[1]))
    elif file.endswith(file_types['Video']):
        shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, list(file_types.keys())[2]))
    elif file.endswith(file_types['Compressed']):
        shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, list(file_types.keys())[3]))
    elif file.endswith(file_types['Pictures']):
        shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, list(file_types.keys())[4]))
    elif file.endswith(file_types['Programs']):
        shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, file_types.keys()[5]))
    else:
        if file not in list(file_types.keys()):
            shutil.move(src=os.path.join(check_directory, file), dst=os.path.join(check_directory, 'Others'))

