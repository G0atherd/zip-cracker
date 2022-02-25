import zipfile
from colorama import Fore
print('\033[31m' + '###########################################################################')
print('\033[31m' + '#  __________ ____        ____  ____      _    ____ _  _______ ______     #')
print('\033[31m' + '# / /__  /_ _|  _ \      /  ___ |  _ \   / \  / ___| |/ / ____|  _ \ \    #')
print('\033[31m' + '# | |  / / | || |_) |____| |   | |_) |  / _ \| |   |  /|  _| | |_) | |    #')
print('\033[31m' + '# | |  / /_| ||  __/_____| |___|  _ <  / ___ \ |___| . \| |__|  _ || |< > #')
print('\033[31m' + '# | |/____|___|_|         \____|_| \_\/_/   \_\____|_|\_\_____|_| \_\|    #')
print('\033[31m' + '# \_\                                                             /_/     #')
print('\033[31m' + '#               Tool To Crack Any Password ZIP File                       #')
print('\033[31m' + '#                    Coded by: Goatherd#9951                              #')
print('\033[31m' + '#                github:https://github.com/G0atherd                       #')
print('\033[31m' + '###########################################################################')

print("\033[36")
file = str(input("Please inpute your zip file:"))
wordlist1 = str(input("Please inpute your wordlist:"))

def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack.
	"""
	zipfilename = file
	dictionary = wordlist1

	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				pass
	print("Password:"+ password)

if __name__ == '__main__':
	main()
