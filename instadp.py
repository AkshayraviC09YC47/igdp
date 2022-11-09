from instaloader import Instaloader
import argparse

banner="""

 /$$$$$$  /$$$$$$          /$$$$$$$  /$$$$$$$ 
|_  $$_/ /$$__  $$        | $$__  $$| $$__  $$
  | $$  | $$  \__/        | $$  \ $$| $$  \ $$
  | $$  | $$ /$$$$ /$$$$$$| $$  | $$| $$$$$$$/
  | $$  | $$|_  $$|______/| $$  | $$| $$____/ 
  | $$  | $$  \ $$        | $$  | $$| $$      
 /$$$$$$|  $$$$$$/        | $$$$$$$/| $$      
|______/ \______/         |_______/ |__/      
                                              
 #### Instagram Profile Picture Downloader ####                                              
                                              
"""

parser = argparse.ArgumentParser()

parser.add_argument('-u',help ='Enter the username')
parser.add_argument('-l',help ='Path to the username list text file')

args = parser.parse_args()
username = args.u
u_list =args.l

if not any((username,u_list)):
	print(banner)
	print("-"*100)
	print("To download single users profile pic, use this command:   'python3 instadp.py -u sunnyleone'")
	print("To download multiple users profile pic, use this command: 'python3 instadp.py -l usernamelist.txt'")
	print("-"*100)

if username:
	print(banner)
	print(f"Downloading {username} profile picture, please wait....")
	Instaloader().download_profile(username, profile_pic_only=True)

if u_list:
	print(banner)
	with open(u_list,'r') as f:
		for line in f:
			for word in line.split():
				print(f"Downloading {word} profile picture, please wait....")
				Instaloader().download_profile(word, profile_pic_only=True)
				print("-"*50)
