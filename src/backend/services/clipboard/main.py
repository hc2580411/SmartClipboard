import pyperclip as pc
import time 

#the phrase clipboard is abbreviated to cb

def main():
    previous_cb_content = ""
    
    try:
        while True:
            current_cb_cotent = pc.paste()

            if current_cb_cotent != previous_cb_content:
                print(current_cb_cotent)
                previous_cb_content = current_cb_cotent
            time.sleep(1)
    
    except Exception as e:
        print("error: " + e)

if __name__ == "__main__":
    main()
            

            