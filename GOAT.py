# Greatest Of All Tools right here
# Try to read this code challenge(impossible) 😵

import hashlib
import requests
import random
import time
from termcolor import cprint,colored

colors = ['red','blue','green','yellow','magenta','cyan']
banner =r"""
      ________      ________      ________  _________   
     |\   ____\    |\   __  \    |\   __  \|\___   ___\ 
     \ \  \___|    \ \  \|\  \   \ \  \|\  \|___ \  \_| 
      \ \  \  ___   \ \  \\\  \   \ \   __  \   \ \  \  
       \ \  \|\  \ __\ \  \\\  \ __\ \  \ \  \ __\ \  \ 
        \ \_______\\__\ \_______\\__\ \__\ \__\\__\ \__\
         \|_______\|__|\|_______\|__|\|__|\|__\|__|\|__|
                     Greatest Of All Tools 😁
    """
cprint(banner,f'{random.choice(colors)}',attrs=['bold'])    
headers = {'user-agent': "Lattice's Most Goated Tool"}

def main():
    def clear():
            print("\r", end='')
            print(" " * 80, end='')
            print("\r", end='')
    try:

        def buster():
        
                count = 1
                okay = "[+]"
                    
                # Taking input
                url = input("\tEnter the url here: ")
                url = url.lower().strip()
            
                if url[-1] != "/":
                    url = url+"/"

                if url[:4] == "http" in url or (url[:5] == "https"):
                    pass
                else:
                    cprint("\n\tERROR: Please enter a valid URL...",'red',attrs=['bold'])
                    clear()
                    time.sleep(1)
                    return buster()

                wordlist = input("\tEnter the wordlist here: ")
                print("")
                try:
                    # Parsing Through wordlist
                    with open(wordlist,"r") as file:
                        read = file.readlines()
                except FileNotFoundError:
                        return cprint("\tERROR: Please enter a valid wordlist",'red',attrs=['bold'])
                try:
                        # Making requests
                        for words in read:

                            print(f"\r\tProgress ({count}/{len(read)})",end='',flush=True)  
                            count +=1
                            
                            words = words.strip()
                            req = requests.get(url+words,headers=headers)                
                            code = req.status_code

                            
                        
                            if code == 404:
                                clear()
                                pass
                            else:
                                clear()
                                cprint(f"\t{okay}{code} Directory found at {url+words}",'green',attrs=['bold'])

                            if count >= len(read):
                                    print("\r" + " " * 40, end='', flush=True) 

                        cprint("\n\tDone :) ",'green',attrs=['bold'])
      
                except requests.RequestException as e:
                    cprint(f"{e}",'red',attrs=['bold'])
    
    
        

        def file_hasher(file,algo):
            try:
                with open(file,"rb") as f:
                    hash = hashlib.file_digest(f,algo)
                    return print(f"\t{algo} hash results for {file}: {colored(hash.hexdigest(),f'{random.choice(colors)}',attrs=['bold'])}")
            except:
                return print("\tCould not open file...")

        def word_hasher(algo):
                    hashes = []
                    wordlist = str(input("\tEnter the wordlist file here: ").strip())
                    try: 
                        # Parsing words in file
                        with open(wordlist,'r') as e:
                               read = e.readlines()
                    except FileNotFoundError:
                            return cprint("\tERROR: Please enter a valid wordlist",'red',attrs=['bold'])

                    # Hashing words in file
                    for words in read:
                                words = words.strip()
                                hashe = hashlib.new(algo)
                                hashe.update(bytes(words,'utf-8'))
                                finished = hashe.hexdigest()
                                hashes.append(finished)
                                symbol = "\4"*len(finished)
                    
                    # Fotmatting output
                    formatt = "\n".join(hashes)
                    with open("goat_hashes.txt",'w') as file:
                        file.write(formatt)
                    cprint(f"\n{algo} Hash(es) here:\n{symbol}\n{formatt}\n{symbol}","red",attrs=['bold'])

                    return cprint("\nHash(es) written to 'goat_hashes.txt'","light_blue",attrs=['underline'])

        def hasher():

                algos = {"1":'MD5',"2":'SHA256',"3":'SHA512'}

                # Taking user input
                question1 = str(input("\n\tWhat hashing algorithm would you like?\n\t1)MD5\n\t2)SHA256\n\t3)SHA512\n\n\tEnter here: ").strip())

                if question1 in algos:
                    cprint(f"\tYou chose algo: {algos[question1]}",'green',attrs=['bold'])
                    question2 = str(input("\n\tYou Hashing a file or wordlist?\n\t1) wordlist\n\t2) file\n\n\tEnter here: ").strip())
                else:
                    return cprint("\tEnter a valid number 1-3...",'red',attrs=['bold'])
    
                if question2 =="1":
                    return word_hasher(algos[question1])
                elif question2 == "2":
                    file_to_hash = str(input("\tEnter the name of the file here: ").strip())
                    return file_hasher(file_to_hash,algos[question1])
                else:
                    return cprint("\tEnter a valid number 1-2...",'red',attrs=['bold'])
                    




        def cracker():
            cracked_hashes = []
            passfile_hashes = []
            algos = {"1":'MD5',"2":'SHA256',"3":'SHA512'}
            question = str(input("\n\tWhat hashing algorithm would you like?\n\t1)MD5\n\t2)SHA256\n\t3)SHA512\n\n\tEnter here: ").strip())

            try:
                if question in algos:
                        
                    # Getting input   
                    pass_file = str(input("\n\tEnter your passfile: "))
                    hash_file = input("\tEnter the hash file: ")

                    try:
                        # Parsing Pass and Hash files
                        with open(pass_file,'r') as file1:
                               read = file1.readlines()
                        with open(hash_file,'r') as file2:
                            read1 = file2.readlines()
                    except FileNotFoundError:
                            return cprint("\t\nEnter a valid wordlist",'red',attrs=['bold'])    
                    # Hashing passwords in list
                    for passes in read:
                                passes = passes.strip()
                                hashing = hashlib.new(algos[question])
                                hashing.update(bytes(passes,'utf-8'))
                                finished = hashing.hexdigest()
                                passfile_hashes.append(finished)

                    
                    # Checking if password hashes match
                    for hashes in read1:
                                hashes = hashes.strip()         
                                if hashes in passfile_hashes:
                                    index = passfile_hashes.index(hashes)
                                    index2 = read1[index].strip()
                                    cracked = read[index].strip()
                                    
                                    # Formatting output
                                    formatting = colored(index2,'red',attrs=['bold'])+":"+colored(cracked,'green',attrs=['bold'])
                                    cracked_hashes.append(formatting)
                                    stars = "\4"*len(formatting)
                                    done = "\n".join(cracked_hashes)
                            
                                if cracked_hashes == []:                 
                                    return cprint("\tCould not find a password to the hashes",'magenta','on_light_blue',attrs=['bold'])
                                # Writing to file
                                with open("goat_hashes.cracked",'w') as file:
                                                     file.write(done)
 
                    if len(cracked_hashes) >= 1:
                        cprint(f"\nCRACKED\n{stars}\n{done}\n{stars}",'red',attrs=['bold'])
                        return cprint("\nCracked Hash(es) written to 'goat_hashes.cracked'","light_blue",attrs=['underline'])
                
                else:
                    return cprint("Enter a valid number",'red',attrs=['bold']) 
            except:
                return print("Error")


        def searcher():

                count = 1
                username = str(input("\tEnter the username here: "))
                username = username.lower()
                username = username.replace(" ","")
                print("")
                sites ={"Twitch":  f"https://twitch.tv/{username}",
                        "Reddit":  f"https://www.reddit.com/user/{username}",
                        "Instagram":f"https://www.instagram.com/{username}",
                        "TikTok":  f"https://www.tiktok.com/@{username}",
                        "Facebook":f"https://www.facebook.com/{username}",
                        "Osu":f"https://osu.ppy.sh/users/{username}", # yes osu
                        "LinkTree":f"https://linktr.ee/{username}",
                        "Github":f"https://github.com/{username}",
                        "Youtube":f"https://www.youtube.com/@{username}",
                        "Pinterest":f"https://www.pinterest.com/{username}",}
               
                # IF OR ELSE?!?!?
                for site in sites:

                            print(f"\r\tchecking platforms ({count}/{len(sites)})",end='',flush=True)  
                            count +=1

                            headers = {'user-agent': 'Lattice goat searcher'}
                            good = f"\t{colored("[+]",'green',attrs=['bold'])} successful user at {sites[site]}"

                            try:
                                r = requests.get(sites[site],headers=headers)
                                code = r.status_code
                                html = str(r.text)


                                match site:
                                    case "Twitch":
                                        if "meta name" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass
                                    case "Reddit":
                                        if "Posts" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass
                                    case "Instagram":
                                        if "hl=" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass
                                    case "TikTok":
                                        if "uniqueId" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass
                                    case "Facebook":
                                        if "og:" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass
                                    case "Github":
                                        if "- Overview" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass
                                    case "Youtube":
                                        if "subscribe-button" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass                              
                                    case "Osu":
                                        if "User not found" in html:
                                            pass
                                        else:
                                            clear()
                                            print(good)
                                    case "Pinterest":
                                        if "profile-followers" in html:
                                            clear()
                                            print(good)
                                        else:
                                            pass

                            except requests.RequestException as e:
                                           cprint(f"\n{e}",'red',attrs=['bold'])

                            if count >= len(sites):
                                    print("\r" + " " * 40, end='', flush=True) 

                cprint("\n\tDone :)",'green',attrs=['bold'])


            
        select = str(input("""
        Select a number:

        1) hasher   (who needs md5sum? 🥱)
        2) buster   (Temu Dirbuster 🙏 )
        3) cracker  (Crack the words u just hashed, cause why not 😁)
        4) searcher (Checks platforms for a valid user 🧐)

        Enter Here: """).strip())

        if select == "1":
            hasher()
        elif select == "2":
            buster()
        elif select == "3":
            cracker()
        elif select == "4":
            searcher()
        else:
            cprint("\tPlease select a valid number 1-4",'red',attrs=['bold'])
            time.sleep(1)
            return main()
    except:
        return cprint("\n\n\tExiting...",'red',attrs=['bold'])

# MAN 
main()
