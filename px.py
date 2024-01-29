import subprocess
import webbrowser
import os
import colorama
from colorama import Fore, Style
import csv
import platform
import time
import shutil
import json
from tkinter import messagebox as Mb
import pyttsx3
import random
from googletrans import Translator
import requests
from pydub import AudioSegment
import sqlite3
import pyshorteners
from PIL import Image
from io import BytesIO
from pytz import timezone
from lorem_text import lorem
import datetime

current_time = time.strftime("%Y-%m-d %H:%M:%S", time.localtime())

#CLEAR OLD TERMINAL
os.system('cls' if platform.system() == "Windows" else 'clear')


pxmain = f"""
██████╗ ██╗  ██╗    ██╗                                
██╔══██╗╚██╗██╔╝    ╚██╗                               
██████╔╝ ╚███╔╝      ╚██╗                              
██╔═══╝  ██╔██╗      ██╔╝                              
██║     ██╔╝ ██╗    ██╔╝                               
╚═╝     ╚═╝  ╚═╝    ╚═╝                                
                                                       
██████╗ ██╗   ██╗    ██████╗ ██╗   ██╗██████╗  ██████╗ 
██╔══██╗╚██╗ ██╔╝    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗
██████╔╝ ╚████╔╝     ██████╔╝ ╚████╔╝ ██████╔╝██║   ██║
██╔══██╗  ╚██╔╝      ██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║
██████╔╝   ██║       ██║        ██║   ██║  ██║╚██████╔╝
╚═════╝    ╚═╝       ╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ 
v22.10.23/r21                              @c4gwn                   


Dev: https://github.com/pyroalww
OS Type: {platform.system()} {platform.release()}
Decoder: PyroManualDecoder.exe | Online: True | Version 1.3.3
Decryptor started: {current_time} 
Worker: Local Python
Local libs: subprocess, webbrowser, os, colorama, Fore, Style, csv, platform, time, shutil, json, tkinter, pyttsx3, random, googletrans, Translator, requests, sqlite3, pyshorteners, tetris, pytz, lorem_text, gensim
Used code lines: 1442
Mode: Compiled mode
License: QWXC3F-30ML10-SM1SP-1OOSQP-WIN
URL Shortener Engine: pyshorteners [ACTIVE_API_1YEARS]

> "help" for commands

"""

morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..'
    }
class PxShell:
    def __init__(self):
        self.commands = {
            'startapp': {
                'description': 'Start an application',
                'usage': 'startapp [app_name]',
                'function': self.start_app
            },
            'startdir': {
                'description': 'Change the current directory',
                'usage': 'startdir [directory_path]',
                'function': self.start_directory
            },
            'start': {
                'description': 'Starts a file',
                'usage': 'start [file_dir]',
                'function': self.start
            },
            'searchweb': {
                'description': 'Search the web using your default browser',
                'usage': 'searchweb [search_term]',
                'function': self.search_web
            },
            'killtask': {
                'description': 'Terminate a running task',
                'usage': 'killtask [task_name]',
                'function': self.kill_task
            },
            'dialog': {
                'description': 'Starts a messagebox',
                'usage': 'dialog [dialogtype(1/2/3)] [title] [message]',
                'function': self.dialog
            },
            'help': {
                'description': 'Display a list of available commands',
                'usage': 'help',
                'function': self.show_help
            },
            'setBluetooth': {
                'description': 'Turn Bluetooth on (1) or off (0)',
                'usage': 'setBluetooth [1 or 0]',
                'function': self.set_bluetooth
            },
            'installPlugin': {
                'description': 'Installs .px extension to px shell. (Working on it! Hard to use.)',
                'usage': 'installPlugin [px file location]',
                'function': self.add_custom_command
            },
            'fixcpu': {
                'description': 'Optimize CPU performance for AC power scheme',
                'usage': 'fixcpu',
                'function': self.fix_cpu
            },
            'terminalColor': {
                'description': 'Change terminal text color',
                'usage': 'terminalColor [red, blue, green]',
                'function': self.change_terminal_color
            },
            'quicknote': {
                'description': 'Open Notepad',
                'usage': 'quicknote',
                'function': self.open_notepad
            },
            'takenote': {
                'description': 'Quick note',
                'usage': 'takenote [note]',
                'function': self.take_note
            },
            'voicenote': {
                    'description': 'Read your note with voice',
                    'usage': 'voiceenote [note]',
                    'function': self.voice_note
            },
            'shutdown': {
                'description': 'Shutdown the computer',
                'usage': 'shutdown',
                'function': self.shutdown_computer
            },
            'restart': {
                'description': 'Restart the computer',
                'usage': 'restart',
                'function': self.restart_computer
            },
            'cl': {
                'description': 'Clear the terminal screen',
                'usage': 'cl',
                'function': self.clear_terminal
            },
            'trashclear': {
                'description': 'Empty the recycle bin (Windows only)',
                'usage': 'trashclear',
                'function': self.empty_recycle_bin
            },
            'searchYT': {
                'description': 'Search YouTube and open the results in your default browser',
                'usage': 'searchYT [search_term]',
                'function': self.search_youtube
            },
            'shortlink': {
                'description': 'Makes more shorter your link',
                'usage': 'shortlink [long_url]',
                'function': self.linkshorter
            },
            'exportcsv': {
                'description': 'Export command history to a CSV file',
                'usage': 'exportcsv',
                'function': self.export_to_csv
            },
            'convertAudio': {
                'description': 'Converts audio to another format',
                'usage': 'convertAudio [input_audio] [output_format]',
                'function': self.convert_audio
            },
            'systeminfo': {
                'description': 'Display system information',
                'usage': 'systeminfo',
                'function': self.system_info
            },
            'analyzetest': {
                'description': 'analyzes tesxxt',
                'usage': 'analyetext [path]',
                'function': self.analyze_text
            },
            'currenttime': {
                'description': 'Display the current time',
                'usage': 'currenttime',
                'function': self.get_current_time
            },
            'calculate': {
                'description': 'Perform a calculation',
                'usage': 'calculate [expression]',
                'function': self.calculate
            },
            'takescreenshot': {
                'description': 'Take a screenshot',
                'usage': 'takescreenshot [output_file.png]',
                'function': self.take_screenshot
            },
            'weather': {
                'description': 'Check the weather for a city',
                'usage': 'weather [city_name]',
                'function': self.weather
            },
            'currencyconverter': {
                'description': 'Perform currency conversion',
                'usage': 'currencyconverter [amount] [from_currency] [to_currency]',
                'function': self.currency_converter
            },
            'morsecode': {
                'description': 'Translates morse code',
                'usage': 'morsecode [text]',
                'function': self.morse_code
            },
            'translate': {
                'description': 'Translator',
                'usage': 'translatetext [text] [target_language]',
                'function': self.translate_text
            },
            'dbquery': {
                'description': 'Executes in  database',
                'usage': 'dbquery [sql_query]',
                'function': self.execute_database_query
            }, 
            'randompassword': {
                'description': 'Generate a random password',
                'usage': 'randompassword [length]',
                'function': self.random_password
            },
            'listdrives': {
                'description': 'List available drives on the system',
                'usage': 'listdrives',
                'function': self.list_drives
            },
            'printcalendar': {
                'description': 'Print a calendar for a specific year and month',
                'usage': 'printcalendar [year] [month]',
                'function': self.print_calendar
            },
            'sendemail': {
                'description': 'Send an email to a recipient',
                'usage': 'sendemail [recipient] [subject] [message]',
                'function': self.send_email
            },

            'createzip': {
                'description': 'Create a zip file from specified files',
                'usage': 'createzip [output_zip] [file1] [file2] [file3] ...',
                'function': self.create_zip
            },
            'downloadHTML': {
                'description': 'Downloads a Web site html code',
                'usage': 'savepage [url] [output_filename]',
                'function': self.save_page
            },
            'countwords': {
                'description': 'Count words in a text file',
                'usage': 'countwords [text_file]',
                'function': self.count_words
            },
            'findlargestfile': {
                'description': 'Find the largest file in a directory',
                'usage': 'findlargestfile [directory_path]',
                'function': self.findlargestfile
            },
            'searchstackoverflow': {
                'description': 'Search Stack Overflow for a query',
                'usage': 'searchstackoverflow [query]',
                'function': self.search_stackoverflow
            },
            'generateColor': {
                'description': 'Generates random color code',
                'usage': 'generateColor',
                'function': self.generate_random_color
            },
            'ping': {
                'description': 'Ping a host',
                'usage': 'ping [hostname]',
                'function': self.ping
            },

            'systemresources': {
                'description': 'Display CPU and memory usage',
                'usage': 'systemresources',
                'function': self.system_resources
            },
            'createpdf': {
                'description': 'Convert a text file to a PDF',
                'usage': 'createpdf [text_file]',
                'function': self.create_pdf
            },
            'say': {
                'description': 'Says your writings',
                'usage': 'say [...]',
                'function': self.say
            },
            'addvariable': {
                'description': 'Add a variable',
                'usage': 'addvariable [variable] [value]',
                'function': self.add_variable
            },
            
            'listpythonversions': {
                'description': 'List installed Python versions',
                'usage': 'listpythonversions',
                'function': self.list_python_versions
            },
            'generateqrcode': {
                'description': 'Generate a QR code for provided data',
                'usage': 'generateqrcode [data]',
                'function': self.generate_qr_code
            },
            'generateNumber': {
                'description': 'Generate random number',
                'usage': 'generateNumber [min] [max]',
                'function': self.generate_random_number
            },
            'getgithubinfo': {
                'description': 'Get GitHub user information',
                'usage': 'getgithubinfo [username]',
                'function': self.get_github_info
            },
            'listinstalledpackages': {
                'description': 'List installed Python packages',
                'usage': 'listinstalledpackages',
                'function': self.list_installed_packages
            },
            'texttospeech': {
                'description': 'Convert text to speech',
                'usage': 'texttospeech [text_to_speak]',
                'function': self.text_to_speech
            },
            'countdowntimer': {
                'description': 'Set a countdown timer in seconds',
                'usage': 'countdowntimer [seconds]',
                'function': self.countdown_timer
            },
            'loremipsum': {
                'description': 'Generates lorem ipsum',
                'usage': 'loremipsum [paragraph_count]',
                'function': self.generate_lorem_ipsum
            },
            'fileproperties': {
                'description': 'Display file properties (size, creation time, etc.)',
                'usage': 'fileproperties [file_path]',
                'function': self.file_properties
            },
            'md5checksum': {
                'description': 'Calculate MD5 checksum of a file',
                'usage': 'md5checksum [file_path]',
                'function': self.md5_checksum
            },
            'generateuuid': {
                'description': 'Generate a UUID (Universally Unique Identifier)',
                'usage': 'generateuuid',
                'function': self.generate_uuid
            },
            'listusers': {
                'description': 'List users on the system',
                'usage': 'listusers',
                'function': self.list_users
            },
            'converttimezone': {
                'description': 'Converts timezone to another timezone',
                'usage': 'converttimezone [time] [from_timezone] [to_timezone]',
                'function': self.convert_timezone
            },
            'diskspace': {
                'description': 'Check disk space on system partitions',
                'usage': 'diskspace',
                'function': self.disk_space
            },
            'listprocesses': {
                'description': 'List running processes on the system',
                'usage': 'listprocesses',
                'function': self.list_processes
            },
            'searchFile': {
                'description': 'Searchs a file in the path',
                'usage': 'searchFile [directory_path] [file_name]',
                'function': self.search_file
            },
            'processimages': {
                'description': 'Process images in a directory (e.g., resize or apply filters)',
                'usage': 'processimages [directory_path]',
                'function': self.process_images
            },
            'showimage': {
                'description': 'Shows image from Web',
                'usage': 'showimage [image_url]',
                'function': self.show_image
            },
            'listpackages': {
                'description': 'List installed Python packages',
                'usage': 'listpackages',
                'function': self.list_packages
            },
            'creategui': {
                'description': 'Create a simple GUI',
                'usage': 'creategui',
                'function': self.create_gui
            },
            'newdir': {
                'description': 'Create a new directory',
                'usage': 'newdir [directory_name]',
                'function': self.create_directory
            },
            'deldir': {
                'description': 'Delete a directory',
                'usage': 'deldir [directory_name]',
                'function': self.delete_directory
            },
            'delfile': {
                'description': 'Delete a file',
                'usage': 'delfile [file_name]',
                'function': self.delete_file
            },
            'exit': {
                'description': 'Exit from px.',
                'usage': 'exit',
                'function': self.exit
            },
            'newfile': {
                'description': 'Create a new file',
                'usage': 'newfile [file_name]',
                'function': self.create_file
            },
            'listfiles': {
                'description': 'List files in a directory',
                'usage': 'listfiles [directory_path]',
                'function': self.list_files
            },
            'renamefile': {
                'description': 'Rename a file',
                'usage': 'renamefile [old_file_name] [new_file_name]',
                'function': self.rename_file
            },
            'copyfile': {
                'description': 'Copy a file',
                'usage': 'copyfile [source_file] [destination_file]',
                'function': self.copy_file
            },
            'movefile': {
                'description': 'Move a file',
                'usage': 'movefile [source_file] [destination_directory]',
                'function': self.move_file
            },
            'encryptfile': {
                'description': 'Encrypt a file using Fernet encryption',
                'usage': 'encryptfile [input_file] [output_file]',
                'function': self.encrypt_file
            },
            'decryptfile': {
                'description': 'Decrypt a file previously encrypted with Fernet',
                'usage': 'decryptfile [input_file] [output_file]',
                'function': self.decrypt_file
            },
            'update': {
                'description': 'Update pxos',
                'usage': 'update',
                'function': self.updatepx
            },
            'px': {
                'description': 'Shows px text',
                'usage': 'px',
                'function': self.pxfunction
            },
        }
        self.command_history = []
        self.intro_message = "| px by @c4gwn |"
        colorama.init(autoreset=True)
        

    def run(self):
        while True:
            command = input(Fore.CYAN + "px > " + Style.RESET_ALL).strip()
            if command:
                self.execute_command(command)
    def add_custom_command(self, args):
        # userdan çekme
        command_name = input("Enter command: ")
        description = input("Enter description: ")
        usage = input("Enter usage: ")
        function_name = input("Enter Function Name: ")
        function_file_location = input("Enter function file location: ")

        # komut ekle
        new_command_info = {
            'command_name': command_name,
            'description': description,
            'usage': usage,
            'function': function_name,
            'function_file_location': function_file_location
        }
        self.save_command_info(new_command_info)

        #  komutu oku
        function_code = self.read_function_code(function_file_location)


        self.add_custom_command_to_library(new_command_info, function_code)
    def start(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: start [file_dir]" + Style.RESET_ALL)
            return
        path = args[0]
        os.system(path)
        print(Fore.GREEN + f"Started: {path}" + Style.RESET_ALL)
    def take_note(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: takenote [note_text]" + Style.RESET_ALL)
            return
        note_text = ' '.join(args)
        with open('notes.txt', 'a') as file:
            file.write(note_text + '\n')
        print(Fore.GREEN + "Note added!" + Style.RESET_ALL)

    def voice_note(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: voicenote [note_text]" + Style.RESET_ALL)
            return
        note_text = ' '.join(args)
        engine = pyttsx3.init()
        engine.say(note_text)
        engine.runAndWait()
        print(Fore.GREEN + "Voice note recorded!" + Style.RESET_ALL)

    def generate_random_color(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: generaterandomcolor" + Style.RESET_ALL)
            return
        color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        print(Fore.GREEN + f"Random Color: {color}" + Style.RESET_ALL)

    def dialog(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: dialog [messageboxtype(1,2,3)] [title] [message]" + Style.RESET_ALL)
            return
        if len(args) == 1:
            print(Fore.YELLOW + "Usage: dialog [messageboxtype(1,2,3)] [title] [message]" + Style.RESET_ALL)
            return
        if len(args) == 2:
            print(Fore.YELLOW + "Usage: dialog [messageboxtype(1,2,3)] [title] [message]" + Style.RESET_ALL)
            return
        type = args[0]
        title = args[1]
        message = args[2]
        if type == "1":
            Mb.showinfo(title, message)
            print(Fore.GREEN + "Dialog showed!" + Style.RESET_ALL)
        elif type == "2":
            Mb.showwarning(title, message)
            print(Fore.GREEN + "Dialog showed!" + Style.RESET_ALL)
        elif type == "3":
            Mb.showerror(title, message)
            print(Fore.GREEN + "Dialog showed!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Usage: dialog [messageboxtype(1,2,3)] [title] [message]" + Style.RESET_ALL)
            
    def save_command_info(self, command_info):
        # Komut bilgilerini bir JSON dosyasına kaydedin
        with open('commands.json', 'a') as file:
            json.dump(command_info, file)
    
    def pxfunction(self, args):
        os.system('cls' if platform.system() == "Windows" else 'clear')
        print(Fore.GREEN + pxmain + Style.RESET_ALL)

    def read_function_code(self, file_location):
        # Komut fonksiyonunu okuyun ve utf-8 karakter kodlamasıyla açın
        with open(file_location, 'r', encoding='utf-8') as file:
            function_code = file.read()
        return function_code
    def add_custom_command_to_library(self, command_info, function_code):
        # Kullanıcıdan gelen komutu koda ekleyin
        exec(function_code, globals(), locals())

        # Yeni komutu kütüphaneye ekleyin
        self.commands[command_info['command_name']] = {
            'description': command_info['description'],
            'usage': command_info['usage'],
            'function': self.commands[command_info['function']]['function']  # Doğru işlevi alın
        }

    def execute_command(self, command):
        command_parts = command.split()
        command_name = command_parts[0]
        args = command_parts[1:]
        if command_name in self.commands:
            self.commands[command_name]['function'](args)
        else:
            print(Fore.RED + "Invalid command. Type 'help' for a list of available commands." + Style.RESET_ALL)

    def start_app(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: startapp [app_name]" + Style.RESET_ALL)
            return
        supported_apps = ["Msedge", "chrome", "spotify", "explorer", "steam", "cmd", "obs", "riot games", "vscode", "telegram", "discord", "mspaint"]
        app = args[0]
        if app in supported_apps:
            subprocess.Popen([app])
            print(Fore.GREEN + f"Started {app}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"{app} is not a supported application." + Style.RESET_ALL)
    def show_image(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: showimage [image_url]" + Style.RESET_ALL)
            return
        image_url = args[0]

        try:
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image.show()
            print(Fore.GREEN + "Image displayed." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)


    def morse_code(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: morsecode [text]" + Style.RESET_ALL)
            return
        text = args[0].upper()

        try:
            morse_text = ' '.join([morse_code_dict[c] for c in text if c in morse_code_dict])
            print(Fore.GREEN + f"Morse Code for '{text}': {morse_text}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def generate_random_number(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: generaterandom [min_value] [max_value]" + Style.RESET_ALL)
            return
        min_value = int(args[0])
        max_value = int(args[1])
        random_number = random.randint(min_value, max_value)
        print(Fore.GREEN + f"Random Number: {random_number}" + Style.RESET_ALL)


    def generate_lorem_ipsum(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: loremipsum [paragraph_count]" + Style.RESET_ALL)
            return
        paragraph_count = int(args[0])

        try:
            lorem_text = lorem.paragraphs(paragraph_count)
            print(Fore.GREEN + f"Generated Lorem Ipsum Text:\n{lorem_text}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def start_directory(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: startdir [directory_path]" + Style.RESET_ALL)
            return
        directory = args[0]
        if os.path.exists(directory):
            os.chdir(directory)
            print(Fore.GREEN + f"Changed current directory to {directory}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Directory '{directory}' does not exist." + Style.RESET_ALL)

    def search_web(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: searchweb [search_term]" + Style.RESET_ALL)
            return
        search_term = " ".join(args)
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        print(Fore.GREEN + f"Searching the web for: {search_term}" + Style.RESET_ALL)



    def save_page(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: savepage [url] [output_filename]" + Style.RESET_ALL)
            return
        url = args[0]
        output_filename = args[1]
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(output_filename, 'w', encoding='utf-8') as file:
                    file.write(response.text)
                print(Fore.GREEN + f"Page saved as '{output_filename}'" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Failed to retrieve page. Status Code: {response.status_code}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)


    def translate_text(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: translatetext [text] [target_language]" + Style.RESET_ALL)
            return
        text = args[0]
        target_language = args[1]

        translator = Translator()
        translated_text = translator.translate(text, dest=target_language)
        print(Fore.GREEN + f"Translated Text: {translated_text.text}" + Style.RESET_ALL)

    def search_file(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: searchfile [directory_path] [file_name]" + Style.RESET_ALL)
            return
        directory_path = args[0]
        file_name = args[1]
        file_list = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file_name in file:
                    file_list.append(os.path.join(root, file))
        if file_list:
            print(Fore.GREEN + f"Found {len(file_list)} files:")
            for file in file_list:
                print(file)
        else:
            print(Fore.RED + "No files found." + Style.RESET_ALL)

    def list_installed_packages(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: listinstalledpackages" + Style.RESET_ALL)
            return
        try:
            import pip
            from pip._internal.operations.freeze import freeze
            packages = freeze(local_only=True)
            print(Fore.GREEN + "Installed packages:")
            for package in packages:
                print(package)
            print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def say(self, args):
            if len(args) == 0:
                print(Fore.YELLOW + "Usage: say [text]" + Style.RESET_ALL)
                return
            text = " ".join(args)
            print(Fore.GREEN + f"{text}" + Style.RESET_ALL)
    def text_to_speech(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: texttospeech [text_to_speak]" + Style.RESET_ALL)
            return
        text = " ".join(args)
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            print(Fore.GREEN + f"Speaking: {text}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def convert_timezone(self, args):
        if len(args) != 3:
            print(Fore.YELLOW + "Usage: converttimezone [time] [from_timezone] [to_timezone]" + Style.RESET_ALL)
            return
        time_str = args[0]
        from_tz = timezone(args[1])
        to_tz = timezone(args[2])

        try:
            local_time = from_tz.localize(datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
            target_time = local_time.astimezone(to_tz)
            print(Fore.GREEN + f"Converted Time: {target_time}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def file_properties(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: fileproperties [file_path]" + Style.RESET_ALL)
            return
        file_path = args[0]
        try:
            import os
            import platform
            from datetime import datetime
            file_stats = os.stat(file_path)
            file_size = file_stats.st_size
            file_created = datetime.fromtimestamp(file_stats.st_ctime)
            file_modified = datetime.fromtimestamp(file_stats.st_mtime)
            is_directory = "Directory" if os.path.isdir(file_path) else "File"
            platform_info = platform.system()
            print(Fore.GREEN + f"{is_directory} Path: {file_path}\n"
                  f"Size: {file_size} bytes\n"
                  f"Created: {file_created}\n"
                  f"Last Modified: {file_modified}\n"
                  f"Platform: {platform_info}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def analyze_text(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: analyzetext [text]" + Style.RESET_ALL)
            return
        text = args[0]
        word_count = len(text.split())
        character_count = len(text)
        print(Fore.GREEN + f"Word Count: {word_count}, Character Count: {character_count}" + Style.RESET_ALL)

    def md5_checksum(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: md5checksum [file_path]" + Style.RESET_ALL)
            return
        file_path = args[0]
        try:
            import hashlib
            with open(file_path, "rb") as file:
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()
                print(Fore.GREEN + f"MD5 Checksum for {file_path}: {md5_hash}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    
    def updatepx(self, args):
        os.system('cls' if platform.system() == "Windows" else 'clear')
        print(Fore.BLACK + "| INSTALL FIRMWARE MODE | " + Style.RESET_ALL)
        current_time = int(time.time())
        def update():
            quest = input((Fore.YELLOW + """
[1] Download and install
[0] Skip
> """ + Style.RESET_ALL))
            if quest == "1":
                print(Fore.RED + "Updating." + Style.RESET_ALL)
                time.sleep(0.5)
                os.system('cls' if platform.system() == "Windows" else 'clear')
                print(Fore.GREEN + "Updating.." + Style.RESET_ALL)
                time.sleep(0.5)
                os.system('cls' if platform.system() == "Windows" else 'clear')
                print(Fore.BLUE + "Updating..." + Style.RESET_ALL)
                os.system('cls' if platform.system() == "Windows" else 'clear')
                print(Fore.GREEN + "Updated! Please restart PX_OS!" + Style.RESET_ALL)
                time.sleep(1)
                quit()
        if current_time % 2 == 0:
            if current_time > 50:
                print(Fore.YELLOW + "Update 1.08 is available!" + Style.RESET_ALL)
                update()
            elif current_time > 40:
                print(Fore.YELLOW + "Update 1.07 is available!" + Style.RESET_ALL)
                update()
            elif current_time > 30:
                print(Fore.YELLOW + "Update 1.06 is available! " + Style.RESET_ALL)
                update()
            elif current_time > 20:
                print(Fore.YELLOW + "Update 1.05 is available! " + Style.RESET_ALL)
                update()
            elif current_time > 10:
                print(Fore.YELLOW + "Update 1.04 is available!" + Style.RESET_ALL)
                (update)
            else:
                print(Fore.RED + "No update available" + Style.RESET_ALL)
        else:
            print(Fore.RED + "No update available" + Style.RESET_ALL)


    def generate_uuid(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: generateuuid" + Style.RESET_ALL)
            return
        try:
            import uuid
            unique_id = uuid.uuid4()
            print(Fore.GREEN + f"Generated UUID: {unique_id}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def countdown_timer(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: countdowntimer [seconds]" + Style.RESET_ALL)
            return
        seconds = int(args[0])
        try:
            import time
            while seconds > 0:
                print(Fore.GREEN + f"Time remaining: {seconds} seconds" + Style.RESET_ALL)
                time.sleep(1)
                seconds -= 1
            print(Fore.GREEN + "Time's up!" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def list_users(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: listusers" + Style.RESET_ALL)
            return
        try:
            import os
            users = [f.name for f in os.scandir('/home') if f.is_dir()]
            users = ', '.join(users)
            print(Fore.GREEN + f"Users on this system: {users}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def disk_space(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: diskspace" + Style.RESET_ALL)
            return
        try:
            import psutil
            partitions = psutil.disk_partitions()
            for partition in partitions:
                usage = psutil.disk_usage(partition.device)
                print(Fore.GREEN + f"Device: {partition.device}\n"
                      f"Total Space: {usage.total} bytes\n"
                      f"Used Space: {usage.used} bytes\n"
                      f"Free Space: {usage.free} bytes" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def list_processes(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: listprocesses" + Style.RESET_ALL)
            return
        try:
            import psutil
            processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
            for process in processes:
                print(Fore.GREEN + f"PID: {process['pid']}\n"
                      f"Name: {process['name']}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def kill_task(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: killtask [task_name]" + Style.RESET_ALL)
            return
        task_name = args[0]
        try:
            if platform.system() == "Windows":
                subprocess.run(["taskkill", "/F", "/IM", task_name])
            else:
                subprocess.run(["pkill", task_name])
            print(Fore.GREEN + f"Task '{task_name}' has been terminated." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to terminate task '{task_name}': {e}" + Style.RESET_ALL)

    def show_help(self, args):
        print(Fore.GREEN + "Available commands:" + Style.RESET_ALL)
        for command_name, command_info in self.commands.items():
            print(Fore.YELLOW + f"- {command_name}: {command_info['description']}" + Style.RESET_ALL)
            print(Fore.BLUE + f"  Usage: {command_info['usage']}" + Style.RESET_ALL)

    def set_bluetooth(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: setBluetooth [1 or 0]" + Style.RESET_ALL)
            return
        state = args[0]
        if state == "1":
            subprocess.run(["btpair", "on"])
            print(Fore.GREEN + "Bluetooth turned on." + Style.RESET_ALL)
        elif state == "0":
            subprocess.run(["btpair", "off"])
            print(Fore.GREEN + "Bluetooth turned off." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid state. Use '1' to turn on or '0' to turn off." + Style.RESET_ALL)
    def ping(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: ping [hostname]" + Style.RESET_ALL)
            return
        hostname = args[0]
        response = os.system(f"ping -c 4 {hostname}")
        if response == 0:
            print(Fore.GREEN + f"{hostname} is up!" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"{hostname} is down!" + Style.RESET_ALL)

    def fix_cpu(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: fixcpu" + Style.RESET_ALL)
            return
        subprocess.run(["PowerCfg", "/SETACVALUEINDEX", "SCHEME_CURRENT", "SUB_PROCESSOR", "IDLEDISABLE", "000"])
        subprocess.run(["PowerCfg", "/SETACTIVE", "SCHEME_CURRENT"])
        print(Fore.GREEN + "CPU idle disabled for AC power scheme." + Style.RESET_ALL)
    def search_stackoverflow(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: searchstackoverflow [query]" + Style.RESET_ALL)
            return
        query = " ".join(args)
        try:
            import webbrowser
            search_url = f"https://stackoverflow.com/search?q={query}"
            webbrowser.open(search_url)
            print(Fore.GREEN + f"Searching Stack Overflow for: {query}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def system_resources(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: systemresources" + Style.RESET_ALL)
            return
        try:
            import psutil
            cpu_percent = psutil.cpu_percent()
            memory_percent = psutil.virtual_memory().percent
            print(Fore.GREEN + f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_percent}%" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def create_pdf(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: createpdf [text_file]" + Style.RESET_ALL)
            return
        text_file = args[0]
        try:
            from fpdf import FPDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            with open(text_file, "r") as file:
                content = file.read()
                pdf.multi_cell(0, 10, content)
                pdf_file = f"{text_file}.pdf"
                pdf.output(pdf_file)
                print(Fore.GREEN + f"PDF file '{pdf_file}' created." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def change_terminal_color(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: terminalColor [red, blue, green]" + Style.RESET_ALL)
            return
        color = args[0]
        if color == "red":
            print(Fore.RED)
        elif color == "blue":
            print(Fore.BLUE)
        elif color == "green":
            print(Fore.GREEN)
        else:
            print(Fore.RED + f"Invalid color: {color}" + Style.RESET_ALL)

    def open_notepad(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: quicknote" + Style.RESET_ALL)
            return
        subprocess.Popen(["notepad.exe"])
        print(Fore.GREEN + "Notepad opened." + Style.RESET_ALL)

    def shutdown_computer(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: shutdown" + Style.RESET_ALL)
            return
        subprocess.run(["shutdown", "/s", "/t", "0"])
        print(Fore.GREEN + "Shutting down the computer... Goodbye!" + Style.RESET_ALL)

    def restart_computer(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: restart" + Style.RESET_ALL)
            return
        subprocess.run(["shutdown", "/r", "/t", "0"])
        print(Fore.GREEN + "Restarting the computer..." + Style.RESET_ALL)
    def linkshorter(self, args):
        s = pyshorteners.Shortener()
        original_url = args[0]
        short_url = s.tinyurl.short(original_url)

        print(Fore.YELLOW + "Kısaltılmış URL:", short_url + Style.RESET_ALL)
    def clear_terminal(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: cl" + Style.RESET_ALL)
            return
        os.system('cls' if platform.system() == "Windows" else 'clear')

    def exit(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: exit" + Style.RESET_ALL)
            return
        print(Fore.GREEN + "Exiting... Goodbye!" + Style.RESET_ALL)
        quit()
    def empty_recycle_bin(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: trashclear" + Style.RESET_ALL)
            return
        try:
            if platform.system() == "Windows":
                subprocess.run(["cmd", "/c", "rd", "/s", "/q", "$Recycle.Bin"])
            else:
                print(Fore.YELLOW + "Not supported on non-Windows platforms." + Style.RESET_ALL)
            print(Fore.GREEN + "Recycle bin cleared." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to clear the recycle bin: {e}" + Style.RESET_ALL)

    def search_youtube(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: searchYT [search_term]" + Style.RESET_ALL)
            return
        search_term = " ".join(args)
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")
        print(Fore.GREEN + f"Searching YouTube for: {search_term}" + Style.RESET_ALL)
    def list_drives(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: listdrives" + Style.RESET_ALL)
            return
        try:
            import psutil
            drives = psutil.disk_partitions()
            drive_list = [drive.device for drive in drives]
            print(Fore.GREEN + "Available drives:")
            for drive in drive_list:
                print(drive)
            print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def print_calendar(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: printcalendar [year] [month]" + Style.RESET_ALL)
            return
        year = int(args[0])
        month = int(args[1])
        try:
            import calendar
            cal = calendar.month(year, month)
            print(Fore.GREEN + f"Calendar for {calendar.month_name[month]} {year}:\n{cal}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def send_email(self, args):
        if len(args) != 3:
            print(Fore.YELLOW + "Usage: sendemail [recipient] [subject] [message]" + Style.RESET_ALL)
            return
        recipient = args[0]
        subject = args[1]
        message = args[2]
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart

            # Your email configuration
            smtp_server = "smtp.example.com"
            smtp_port = 587
            sender_email = "your_email@example.com"
            sender_password = "your_password"

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient
            message["Subject"] = subject
            message.attach(MIMEText(message, "plain"))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient, message.as_string())

            print(Fore.GREEN + "Email sent successfully." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def export_to_csv(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: exportcsv" + Style.RESET_ALL)
            return
        filename = "px_shell_history.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Command"])
            writer.writerows(self.command_history)
        print(Fore.GREEN + f"Command history exported to {filename}" + Style.RESET_ALL)
    def list_python_versions(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: listpythonversions" + Style.RESET_ALL)
            return
        try:
            import sys
            installed_versions = [f"{v.major}.{v.minor}" for v in sys.version_info[:3]]
            print(Fore.GREEN + "Installed Python versions:")
            for version in installed_versions:
                print(version)
            print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def generate_qr_code(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: generateqrcode [data]" + Style.RESET_ALL)
            return
        data = args[0]
        try:
            import qrcode
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")
            print(Fore.GREEN + "QR code saved as 'qrcode.png'" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def get_github_info(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: getgithubinfo [username]" + Style.RESET_ALL)
            return
        username = args[0]
        try:
            import requests
            response = requests.get(f"https://api.github.com/users/{username}")
            if response.status_code == 200:
                data = response.json()
                public_repos = data.get("public_repos")
                followers = data.get("followers")
                following = data.get("following")
                print(Fore.GREEN + f"GitHub Info for {username}:\n"
                      f"Public Repositories: {public_repos}\n"
                      f"Followers: {followers}\n"
                      f"Following: {following}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "GitHub user not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def encrypt_file(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: encryptfile [input_file] [output_file]" + Style.RESET_ALL)
            return
        input_file = args[0]
        output_file = args[1]
        try:
            import cryptography.fernet
            key = cryptography.fernet.Fernet.generate_key()
            cipher_suite = cryptography.fernet.Fernet(key)
            with open(input_file, "rb") as file:
                plaintext = file.read()
                encrypted_data = cipher_suite.encrypt(plaintext)
                with open(output_file, "wb") as output:
                    output.write(encrypted_data)
            print(Fore.GREEN + f"File '{input_file}' encrypted and saved as '{output_file}'" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def decrypt_file(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: decryptfile [input_file] [output_file]" + Style.RESET_ALL)
            return
        input_file = args[0]
        output_file = args[1]
        try:
            import cryptography.fernet
            key = cryptography.fernet.Fernet.generate_key()
            cipher_suite = cryptography.fernet.Fernet(key)
            with open(input_file, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = cipher_suite.decrypt(encrypted_data)
                with open(output_file, "wb") as output:
                    output.write(decrypted_data)
            print(Fore.GREEN + f"File '{input_file}' decrypted and saved as '{output_file}'" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def system_info(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: systeminfo" + Style.RESET_ALL)
            return
        system_info = f"Operating System: {platform.system()} {platform.release()}\n" \
                      f"Architecture: {platform.machine()}\n" \
                      f"Python Version: {platform.python_version()}\n" \
                      f"Username: {os.getlogin()}\n"
        print(Fore.GREEN + system_info + Style.RESET_ALL)
    def calculate(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: calculate [expression]" + Style.RESET_ALL)
            return
        expression = " ".join(args)
        try:
            result = eval(expression)
            print(Fore.GREEN + f"Result: {result}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def findlargestfile(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: findlargestfile [directory_path]" + Style.RESET_ALL)
            return
        directory_path = args[0]
        try:
            import os
            largest_file = ""
            largest_size = 0

            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    if file_size > largest_size:
                        largest_file = file_path
                        largest_size = file_size

            if largest_file:
                print(Fore.GREEN + f"Largest file in {directory_path}: {largest_file} ({largest_size} bytes)" + Style.RESET_ALL)
            else:
                print(Fore.RED + "No files found in the specified directory." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def process_images(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: processimages [directory_path]" + Style.RESET_ALL)
            return
        directory_path = args[0]
        try:
            import os
            from PIL import Image

            # Ensure the output directory exists
            output_directory = os.path.join(directory_path, "processed_images")
            os.makedirs(output_directory, exist_ok=True)

            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                        file_path = os.path.join(root, file)
                        with Image.open(file_path) as image:
                            # Process the image here, e.g., resize or apply filters
                            processed_image = image  # Replace with your image processing logic
                            processed_file_path = os.path.join(output_directory, file)
                            processed_image.save(processed_file_path)

            print(Fore.GREEN + f"Images processed and saved in {output_directory}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def take_screenshot(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: takescreenshot [output_file.png]" + Style.RESET_ALL)
            return
        output_file = args[0]
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            screenshot.save(output_file)
            print(Fore.GREEN + f"Screenshot saved as '{output_file}'" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def weather(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: weather [city_name]" + Style.RESET_ALL)
            return
        city = args[0]
        try:
            import requests
            api_key = "YOUR_WEATHER_API_KEY"  # Replace with your actual API key
            weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(weather_api_url)
            data = response.json()
            if data.get("weather"):
                description = data["weather"][0]["description"]
                temperature = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
                print(Fore.GREEN + f"Weather in {city}: {description}, Temperature: {temperature:.2f}°C" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Weather data not found for the specified city." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def count_words(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: countwords [text_file]" + Style.RESET_ALL)
            return
        text_file = args[0]
        try:
            with open(text_file, 'r') as file:
                content = file.read()
                words = content.split()
                word_count = len(words)
                print(Fore.GREEN + f"Word count in '{text_file}': {word_count}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def list_packages(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: listpackages" + Style.RESET_ALL)
            return
        try:
            import pip
            installed_packages = [package.key for package in pip.get_installed_distributions()]
            print(Fore.GREEN + "Installed packages:")
            for package in installed_packages:
                print(package)
            print(Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def create_gui(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: creategui" + Style.RESET_ALL)
            return
        try:
            import tkinter as tk
            window = tk.Tk()
            window.title("Pyper's GUI")
            label = tk.Label(window, text="Welcome to Pyper's GUI!")
            label.pack()
            window.mainloop()
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def currency_converter(self, args):
        if len(args) != 3:
            print(Fore.YELLOW + "Usage: currencyconverter [amount] [from_currency] [to_currency]" + Style.RESET_ALL)
            return
        amount = float(args[0])
        from_currency = args[1].upper()
        to_currency = args[2].upper()
        try:
            import forex_python.converter
            converter = forex_python.converter.CurrencyRates()
            result = converter.convert(from_currency, to_currency, amount)
            print(Fore.GREEN + f"{amount} {from_currency} is equal to {result:.2f} {to_currency}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def random_password(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: randompassword [length]" + Style.RESET_ALL)
            return
        length = int(args[0])
        try:
            import random
            import string
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
            print(Fore.GREEN + f"Generated random password: {password}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def create_zip(self, args):
        if len(args) < 2:
            print(Fore.YELLOW + "Usage: createzip [output_zip] [file1] [file2] [file3] ..." + Style.RESET_ALL)
            return
        output_zip = args[0]
        files_to_zip = args[1:]
        try:
            import zipfile
            with zipfile.ZipFile(output_zip, 'w') as zipf:
                for file in files_to_zip:
                    zipf.write(file)
            print(Fore.GREEN + f"Files zipped to '{output_zip}'" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def get_current_time(self, args):
        if len(args) != 0:
            print(Fore.YELLOW + "Usage: currenttime" + Style.RESET_ALL)
            return
        current_time = time.strftime("%Y-%m-d %H:%M:%S", time.localtime())
        print(Fore.GREEN + f"Current Time: {current_time}" + Style.RESET_ALL)

    def create_directory(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: newdir [directory_name]" + Style.RESET_ALL)
            return
        directory_name = args[0]
        try:
            os.mkdir(directory_name)
            print(Fore.GREEN + f"Directory '{directory_name}' created." + Style.RESET_ALL)
        except FileExistsError:
            print(Fore.YELLOW + f"Directory '{directory_name}' already exists." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to create directory '{directory_name}': {e}" + Style.RESET_ALL)

    def delete_directory(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: deldir [directory_name]" + Style.RESET_ALL)
            return
        directory_name = args[0]
        try:
            os.rmdir(directory_name)
            print(Fore.GREEN + f"Directory '{directory_name}' deleted." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.YELLOW + f"Directory '{directory_name}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to delete directory '{directory_name}': {e}" + Style.RESET_ALL)

    def delete_file(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: delfile [file_name]" + Style.RESET_ALL)
            return
        file_name = args[0]
        try:
            os.remove(file_name)
            print(Fore.GREEN + f"File '{file_name}' deleted." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.YELLOW + f"File '{file_name}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to delete file '{file_name}': {e}" + Style.RESET_ALL)

    def create_file(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: newfile [file_name]" + Style.RESET_ALL)
            return
        file_name = args[0]
        try:
            with open(file_name, 'w') as new_file:
                new_file.write("")
            print(Fore.GREEN + f"File '{file_name}' created." + Style.RESET_ALL)
        except FileExistsError:
            print(Fore.YELLOW + f"File '{file_name}' already exists." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to create file '{file_name}': {e}" + Style.RESET_ALL)
    def list_files(self, args):
        if len(args) == 0:
            print(Fore.YELLOW + "Usage: listfiles [directory_path]" + Style.RESET_ALL)
            return
        directory = args[0]
        try:
            files = os.listdir(directory)
            for file in files:
                print(Fore.GREEN + file + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"Directory '{directory}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to list files in '{directory}': {e}" + Style.RESET_ALL)


    def convert_audio(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: convertaudio [input_audio] [output_format]" + Style.RESET_ALL)
            return
        input_audio = args[0]
        output_format = args[1]

        try:
            audio = AudioSegment.from_file(input_audio)
            output_audio = input_audio.replace(input_audio.split('.')[-1], output_format)
            audio.export(output_audio, format=output_format)
            print(Fore.GREEN + f"Audio converted and saved as '{output_audio}'" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
    def add_variable(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: addvariable [variable] [value]" + Style.RESET_ALL)
            return
        variable = args[0]
        value = args[1]
        print("saved")
        
    def rename_file(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: renamefile [old_file_name] [new_file_name]" + Style.RESET_ALL)
            return
        old_file_name = args[0]
        new_file_name = args[1]
        try:
            os.rename(old_file_name, new_file_name)
            print(Fore.GREEN + f"Renamed '{old_file_name}' to '{new_file_name}'." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File '{old_file_name}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to rename file '{old_file_name}': {e}" + Style.RESET_ALL)

    def copy_file(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: copyfile [source_file] [destination_file]" + Style.RESET_ALL)
            return
        source_file = args[0]
        destination_file = args[1]
        try:
            shutil.copy(source_file, destination_file)
            print(Fore.GREEN + f"Copied '{source_file}' to '{destination_file}'." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File '{source_file}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to copy file '{source_file}': {e}" + Style.RESET_ALL)

    def move_file(self, args):
        if len(args) != 2:
            print(Fore.YELLOW + "Usage: movefile [source_file] [destination_directory]" + Style.RESET_ALL)
            return
        source_file = args[0]
        destination_directory = args[1]
        try:
            shutil.move(source_file, destination_directory)
            print(Fore.GREEN + f"Moved '{source_file}' to '{destination_directory}'." + Style.RESET_ALL)
        except FileNotFoundError:
            print(Fore.RED + f"File '{source_file}' not found." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Failed to move file '{source_file}': {e}" + Style.RESET_ALL)
    def execute_database_query(self, args):
        if len(args) != 1:
            print(Fore.YELLOW + "Usage: dbquery [sql_query]" + Style.RESET_ALL)
            return
        sql_query = args[0]

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            conn.close()
            print(Fore.GREEN + f"Query result: {result}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
if __name__ == "__main__":
    shell = PxShell()
    print(Fore.MAGENTA + shell.intro_message + Style.RESET_ALL)
    shell.run()
