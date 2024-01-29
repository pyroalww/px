# px
An open source Python based shell
# Px Shell Documentation

## Introduction

Welcome to Px Shell, a Python-based command-line utility with a variety of features and functionalities. Px Shell allows you to perform a wide range of tasks, from system operations to web searches and utility functions. This documentation provides an overview of how to use Px Shell, its features, and a list of available commands.
![image](https://github.com/pyroalww/px/assets/134533935/ea3cb12b-b8a8-42df-a92a-e68007879828)
## Getting Started

### Installation

1. Download the Px Shell script from the [GitHub repository](https://github.com/pyroalww).
2. Make sure you have Python installed on your system.
3. Run the script using the Python interpreter.


```bash
python px_shell.py
```

### Overview

Px Shell provides a command-line interface with a set of commands that perform different tasks. It displays a custom ASCII art and information about the system upon startup.

## Commands

### General Commands

1. **startapp**
   - Description: Start an application.
   - Usage: `startapp [app_name]`

2. **startdir**
   - Description: Change the current directory.
   - Usage: `startdir [directory_path]`

3. **start**
   - Description: Starts a file.
   - Usage: `start [file_dir]`

4. **searchweb**
   - Description: Search the web using your default browser.
   - Usage: `searchweb [search_term]`

5. **killtask**
   - Description: Terminate a running task.
   - Usage: `killtask [task_name]`

6. **dialog**
   - Description: Starts a messagebox.
   - Usage: `dialog [dialogtype(1/2/3)] [title] [message]`

7. **help**
   - Description: Display a list of available commands.
   - Usage: `help`

8. **setBluetooth**
   - Description: Turn Bluetooth on (1) or off (0).
   - Usage: `setBluetooth [1 or 0]`

9. **installPlugin**
   - Description: Installs .px extension to px shell. (Working on it! Hard to use.)
   - Usage: `installPlugin [px file location]`

10. **fixcpu**
    - Description: Optimize CPU performance for AC power scheme.
    - Usage: `fixcpu`

11. **terminalColor**
    - Description: Change terminal text color.
    - Usage: `terminalColor [red, blue, green]`

12. **quicknote**
    - Description: Open Notepad.
    - Usage: `quicknote`

13. **takenote**
    - Description: Quick note.
    - Usage: `takenote [note]`

14. **voicenote**
    - Description: Read your note with voice.
    - Usage: `voiceenote [note]`

15. **shutdown**
    - Description: Shutdown the computer.
    - Usage: `shutdown`

16. **restart**
    - Description: Restart the computer.
    - Usage: `restart`

17. **cl**
    - Description: Clear the terminal screen.
    - Usage: `cl`

18. **trashclear**
    - Description: Empty the recycle bin (Windows only).
    - Usage: `trashclear`

19. **searchYT**
    - Description: Search YouTube and open the results in your default browser.
    - Usage: `searchYT [search_term]`

20. **shortlink**
    - Description: Makes your link shorter.
    - Usage: `shortlink [long_url]`

21. **exportcsv**
    - Description: Export command history to a CSV file.
    - Usage: `exportcsv`

22. **convertAudio**
    - Description: Converts audio to another format.
    - Usage: `convertAudio [input_audio] [output_format]`

23. **systeminfo**
    - Description: Display system information.
    - Usage: `systeminfo`

24. **analyzetest**
    - Description: Analyzes text.
    - Usage: `analyzetest [path]`

25. **currenttime**
    - Description: Display the current time.
    - Usage: `currenttime`

26. **calculate**
    - Description: Perform a calculation.
    - Usage: `calculate [expression]`

27. **takescreenshot**
    - Description: Take a screenshot.
    - Usage: `takescreenshot [output_file.png]`

28. **weather**
    - Description: Check the weather for a city.
    - Usage: `weather [city_name]`

29. **currencyconverter**
    - Description: Perform currency conversion.
    - Usage: `currencyconverter [amount] [from_currency] [to_currency]`

30. **morsecode**
    - Description: Translates morse code.
    - Usage: `morsecode [text]`

31. **translate**
    - Description: Translator.
    - Usage: `translatetext [text] [target_language]`

32. **dbquery**
    - Description: Executes in the database.
    - Usage: `dbquery [sql_query]`

33. **randompassword**
    - Description: Generate a random password.
    - Usage: `randompassword [length]`

34. **listdrives**
    - Description: List available drives on the system.
    - Usage: `listdrives`

35. **printcalendar**
    - Description: Print a calendar for a specific year and month.
    - Usage: `printcalendar [year] [month]`

36. **sendemail**
    - Description: Send an email to a recipient.
    - Usage: `sendemail [recipient] [subject] [message]`

37. **createzip**
    - Description: Create a zip file from specified files.
    - Usage: `createzip [output_zip] [file1] [file2] [file3] ...`

38. **downloadHTML**
    - Description: Downloads a website HTML code.
    - Usage: `savepage [url] [output_filename]`

39. **countwords**
    - Description: Count words in a text file.
    - Usage: `countwords [text_file]`

40. **findlargestfile**
    - Description: Find the largest file in a directory.
    - Usage: `findlargestfile [directory_path]`

41. **searchstackoverflow**
    - Description: Search Stack Overflow for a query.
    - Usage: `searchstackoverflow [query]`

42. **generateColor**
    - Description: Generates random color code.
    - Usage: `generateColor`

43. **ping**
    - Description: Ping a host.
    - Usage: `ping [hostname]`

44. **systemresources**
    - Description: Display CPU and memory usage.
    - Usage: `systemresources`

45. **createpdf**
    - Description: Convert a text file to a PDF.
    - Usage: `createpdf [text_file]`

46. **say**
    - Description: Says your writings.
    - Usage: `say [...]`

47. **addvariable**
    - Description: Add a variable.
    - Usage: `addvariable [variable] [value]`

48. **listpythonversions**
    - Description: List installed Python versions.
    - Usage: `listpythonversions`

49. **generateqrcode**
    - Description: Generate a QR code for provided data.
    - Usage: `generateqrcode [

data]`

50. **generateNumber**
    - Description: Generate a random number.
    - Usage: `generateNumber [min] [max]`

51. **getgithubinfo**
    - Description: Get GitHub user information.
    - Usage: `getgithubinfo [username]`

52. **listinstalledpackages**
    - Description: List installed Python packages.
    - Usage: `listinstalledpackages`

53. **texttospeech**
    - Description: Convert text to speech.
    - Usage: `texttospeech [text_to_speak]`

54. **countdowntimer**
    - Description: Set a countdown timer in seconds.
    - Usage: `countdowntimer [seconds]`

55. **loremipsum**
    - Description: Generates lorem ipsum.
    - Usage: `loremipsum [paragraph_count]`

56. **fileproperties**
    - Description: Display file properties (size, creation time, etc.).
    - Usage: `fileproperties [file_path]`

57. **md5checksum**
    - Description: Calculate MD5 checksum of a file.
    - Usage: `md5checksum [file_path]`

58. **generateuuid**
    - Description: Generate a UUID (Universally Unique Identifier).
    - Usage: `generateuuid`

59. **listusers**
    - Description: List users on the system.
    - Usage: `listusers`

60. **converttimezone**
    - Description: Converts timezone to another timezone.
    - Usage: `converttimezone [time] [from_timezone] [to_timezone]`

61. **diskspace**
    - Description: Check disk space on system partitions.
    - Usage: `diskspace`

62. **listprocesses**
    - Description: List running processes on the system.
    - Usage: `listprocesses`

63. **searchFile**
    - Description: Search a file in the path.
    - Usage: `searchFile [directory_path] [file_name]`

64. **processimages**
    - Description: Process images in a directory (e.g., resize or apply filters).
    - Usage: `processimages [directory_path]`

65. **showimage**
    - Description: Shows an image from the web.
    - Usage: `showimage [image_url]`

66. **listpackages**
    - Description: List installed Python packages.
    - Usage: `listpackages`

67. **creategui**
    - Description: Create a simple GUI.
    - Usage: `creategui`

68. **newdir**
    - Description: Create a new directory.
    - Usage: `newdir [directory_name]`

69. **deldir**
    - Description: Delete a directory.
    - Usage: `deldir [directory_name]`

70. **delfile**
    - Description: Delete a file.
    - Usage: `delfile [file_name]`

71. **exit**
    - Description: Exit from px.
    - Usage: `exit`

72. **newfile**
    - Description: Create a new file.
    - Usage: `newfile [file_name]`

73. **listfiles**
    - Description: List files in a directory.
    - Usage: `listfiles [directory_path]`

74. **renamefile**
    - Description: Rename a file.
    - Usage: `renamefile [old_file_name] [new_file_name]`

75. **copyfile**
    - Description: Copy a file.
    - Usage: `copyfile [source_file] [destination_file]`

76. **movefile**
    - Description: Move a file.
    - Usage: `movefile [source_file] [destination_directory]`

77. **encryptfile**
    - Description: Encrypt a file using Fernet encryption.
    - Usage: `encryptfile [input_file] [output_file]`

78. **decryptfile**
    - Description: Decrypt a file previously encrypted with Fernet.
    - Usage: `decryptfile [input_file] [output_file]`

79. **update**
    - Description: Update pxos.
    - Usage: `update`

80. **px**
    - Description: Shows px text.
    - Usage: `px`

## Conclusion

Px Shell provides a powerful and versatile command-line interface for various tasks. Experiment with different commands to explore the capabilities of Px Shell. If you encounter any issues or have suggestions for improvement, please refer to the [GitHub repository](https://github.com/pyroalww) for support and updates.
