import google.generativeai as genai
import pyautogui
import pyperclip
import time
import os

def code():
    def chatbot():
        # Ensure pyautogui failsafe is on
        pyautogui.FAILSAFE = True

        # Click on the icon at (1060, 1034)
        pyautogui.click(1060, 1034)

        # Small delay to allow any UI to update/open
        time.sleep(1)

        # Drag from (827, 229) to (1845, 933)
        pyautogui.moveTo(827, 500)
        pyautogui.dragTo(1825, 900, duration=1.5, button='left')

        # Press 'Ctrl+C' to copy the selected text
        pyautogui.hotkey('ctrl', 'c')

        # Small delay to ensure clipboard is updated
        time.sleep(0.5)
        pyautogui.click(1085, 958)

        # Get the copied text from the clipboard
        copied_text = pyperclip.paste()

        # Print the copied text to verify
        #print("Copied text:", copied_text)
        
        return copied_text


    t=chatbot()
    


    def is_last_message_from_other(chat_text, my_name):
    # Split the chat text into lines
        lines = chat_text.strip().split('\n')
        
        # Iterate over the lines in reverse order to find the last non-empty message
        for line in reversed(lines):
            # Check if the line is not empty
            if line.strip():
                # Split the line into parts based on the last occurrence of a colon
                parts = line.rsplit(':', 2)
                if len(parts) > 2:
                    # Extract sender name by removing the date part
                    sender_info = parts[1].strip().split(']', 1)[-1].strip()
                    print("Sender:", sender_info)  # For debugging purposes
                    # Return whether the sender is different from the specified person
                    return sender_info != my_name
        
        # Return False if no valid message found
        return False


        




    def AI(t):  

    # Ensure the API key is set as an environment variable
        os.environ["API_KEY"] = "AIzaSyCAPnaXsnmKh8ZQeTzwjYwVZ2IK183o4oM"  # You might want to set this outside the script for security reasons

        try:
            # Configure the API key
            genai.configure(api_key=os.environ["API_KEY"])

            # Create a model instance (assuming this is the correct way to initialize the model)
            model = genai.GenerativeModel('gemini-1.5-flash')

            # Generate content
            response = model.generate_content("this is the whatsapp chat between other person (other person is my friend) and me as (MOHD HAMD) so you have to reply to that person on behalf of me and   and this is the chat :"+t+"write a chat on behalf on me of max 3 line and not give time and date with text and one more thing that don't give me a suggestion for reply")

            # Print the response
            return response.text
            #print(response.text)
        
            
        except KeyError:
            print("API key not found. Please set the API key in the environment variables.")
        except AttributeError as e:
            print(f"Attribute error: {e}. Check the method and attribute names.")
        except Exception as e:
            print(f"An error occurred: {e}") 


    print(t,is_last_message_from_other(t,"MOHD HAMD"))
    if  is_last_message_from_other(t,"MOHD HAMD"):
        AI(t)
        pyperclip.copy(AI(t))
        pyautogui.hotkey('ctrl', 'v')
        
        # Small delay to ensure the text is pasted
        time.sleep(0.5)
        
        # Press the Enter key
        pyautogui.press('enter')


def call_function_for_duration(func, interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        
        func() 
        pyautogui.click(1060, 1034)

        time.sleep(interval)


call_function_for_duration(code, interval=3, duration=600)











