import pyperclip as pc
import json
import time
import os
import sys
from googletrans import Translator
from translate import translate

# Get the project root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

# initialise translator
translator = Translator()

# The phrase clipboard is abbreviated to cb

# this is to get the language of the content from clipboard
def load_config():
    try:
        config_path = os.path.join(PROJECT_ROOT, 'config', 'config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {str(e)}")
        sys.exit(1)

# The main function that runs forever to monitor clipboard
def main():
    previous_cb_content = ""
    config = load_config()

    try:
        while True:
            current_cb_content = pc.paste()

            # Print configured language
            if config['general']['language'] != translator.detect(current_cb_content).lang:
                translate(current_cb_content)

            if current_cb_content != previous_cb_content:
                print(current_cb_content)
                previous_cb_content = current_cb_content
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nClipboard monitoring stopped.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
            

            