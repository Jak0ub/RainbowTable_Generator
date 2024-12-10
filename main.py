import os
import sys
import time
import platform
main_list = []
system = platform.system()
#def
if system == "Windows":
	def clean():
		os.system("cls")
else:
	def clean():
		os.system("clear")
def main():
	print(r'''    
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |
  | |\__,_|_|\_\___/ \__,_|_.__/ 
 _/ |                            
|__/                            
''')
#Var
list_main = []
final_list = []
times = []
total = 0
error = 0
person = 0
#loading...
clean()
main()
time.sleep(0.6)
clean()
print(r'''    
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |   _
  | |\__,_|_|\_\___/ \__,_|_.__/   (_) 
 _/ |                            
|__/                             
''')
time.sleep(0.6)
clean()
print(r'''     
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |   _    _
  | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)
 _/ |                            
|__/                            
''')
time.sleep(0.6)
clean()
print(r'''    
   _       _               _     
  (_)     | |             | |    
   _  __ _| | _____  _   _| |__  
  | |/ _` | |/ / _ \| | | | '_ \ 
  | | (_| |   < (_) | |_| | |_) |   _    _    _
  | |\__,_|_|\_\___/ \__,_|_.__/   (_)  (_)  (_)
 _/ |                            
|__/                             
''')
time.sleep(0.6)
clean()
#Main Menu
while True:
	error = 0
	clean()
	main()
	print(f"|Info|:\n\t|1.| |If you don't have answer, just leave the field empty.|\n\t|2.| |To quit entering details just press ENTER until program starts making wordlist|\n\t|3.| |Do NOT add spaces between your input ONLY for spliting two things (ex. Name, Name, Name) NOT (ex. Name, Name Name)|\n\n")
	name = input(f"|{person + 1}.Person's first name|: ")
	if name == "":
		error += 1
	else:
		list_main.append(name.lower())
	surname = input(f"|{person + 1}.Person's surname name|: ")
	if surname == "":
		error += 1
	else:
		list_main.append(surname.lower())
	if error == 0:
		all = f"{name}{surname}"
		list_main.append(all)
	nickname = input(f"|{person + 1}.Person's nickname(Someting, Someting, ....)|: ")
	if nickname == "":
		error += 1
	else:
		if "," in nickname:
			nick = nickname.split(", ")
			for one in nick:
				list_main.append(one.lower())
		else:
			list_main.append(nickname.lower())

	year = input("|Person's birth year|: ")
	if year == "":
		error += 1
	else:
		final_list.append(year)
	hobbies = input(f"|{person + 1}.Person's hobbies(Someting, Someting, ....)|: ")
	if hobbies == "":
		error += 1
	else:
		if "," in hobbies:
			hobby = hobbies.split(", ")
			for one in hobby:
				list_main.append(one.lower())
		else:	
			list_main.append(hobbies.lower())
	words = input("|Key words|(favourite film, something, something..)|: ")
	if words == "":
		error += 1
	else:
		if "," in words:
			word = words.split(", ")
			for slov in word:
				list_main.append(slov.lower())
		else:
			list_main.append(words.lower())
	if error == 6:
		break
	else:
		person += 1
for char in list_main:
	for i in range(len(char)):
		new_word = char[:i] + char[i].upper() + char[i+1:]
		final_list.append(new_word)
#getting wordlist filename
clean()
main()
save_as = input("Enter filename for this wordlist: ")
okay = len(final_list) ** 2
start = time.time()
#creating wordlist
with open(f"{save_as}", "a") as file:
	for char in final_list:
		for char2 in final_list:
			word = f"{char}{char2}"
			file.write(f"{word}\n")
			total += 1
			final = round(time.time() - start)
			if final not in times:
				times.append(final)
				clean()
				print(f"{total} of {okay}")
				
clean()		
print(f"Wordlist of {total} words is done")
input()

