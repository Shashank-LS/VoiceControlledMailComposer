import speech_recognition as sr
import time
import pyautogui

MAIL_APP_NAME = 'Mail'
WAIT_TIME_SHORT = 1
WAIT_TIME_LONG = 5
STOP_COMMAND = "stop typing"
SEND_MAIL_COMMAND = "send mail"
CANCEL_MAIL_COMMAND = "cancel mail"
STOP_EXECUTION_COMMAND = "stop execution"
COMPOSE_BUTTON_IMAGE_PATH = "C:\\Users\\shash\\Pictures\\Screenshots\\Screenshot 2023-11-24 172528.png"
SEND_BUTTON_IMAGE_PATH = "C:\\Users\\shash\\Pictures\\Screenshots\\Screenshot 2023-11-24 232628.png"
CANCEL_BUTTON_IMAGE_PATH = "C:\\Users\\shash\\Pictures\\Screenshots\\Screenshot 2023-11-24 232639.png"
TO_SECTION_COORDINATES = (1261, 472)
MAIL_SECTION_COORDINATES = (1238, 591)

# Declare global variables
send_mail = False
cancel_mail = False


def open_mail_app(app_name=MAIL_APP_NAME):
    pyautogui.press('win')
    time.sleep(WAIT_TIME_SHORT)
    pyautogui.write(app_name)
    pyautogui.press('enter')
    time.sleep(WAIT_TIME_LONG)


def locate_and_click(image_path, message):
    location = None
    max_attempts = 10
    for _ in range(max_attempts):
        location = pyautogui.locateOnScreen(image_path)
        if location:
            break
        time.sleep(1)

    if location:
        pyautogui.click(location)
        print(f"{message} found and clicked.")
        time.sleep(WAIT_TIME_SHORT)
    else:
        print(f"{message} not found on the screen. Check the image path and try again.")


def open_compose_section():
    locate_and_click(COMPOSE_BUTTON_IMAGE_PATH, "Compose button")


def listen_continuous():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening for content...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=None)
                content = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {content}")
                return content

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                print("User interrupted the program. Exiting...")
                exit()

    return None


def type_to_content():
    global send_mail, cancel_mail  # Declare the variables as global

    pyautogui.click(TO_SECTION_COORDINATES)
    time.sleep(WAIT_TIME_SHORT)

    stop_typing = False

    while not stop_typing:
        content = listen_continuous()
        if content:
            content = content.strip().lower()

            if STOP_COMMAND in content:
                print("Stop command detected in 'To' section. Moving to 'Mail' section...")
                stop_typing = True
            elif CANCEL_MAIL_COMMAND in content:
                print("Cancel mail command detected. Canceling the mail...")
                cancel_mail_function()
                cancel_mail = True
                break  # Exit the loop immediately when cancel mail command is detected
            elif SEND_MAIL_COMMAND in content:
                print("Send mail command detected. Sending the mail...")
                send_mail_function()
                send_mail = True
                break  # Exit the loop immediately when send mail command is detected
            elif STOP_EXECUTION_COMMAND in content:
                print("Stop execution command detected. Exiting...")
                exit()  # Exit the program when stop execution command is detected
            else:
                # Remove spaces in the email address
                content = content.replace(" ", "")
                # Replace "atgmail" with "@gmail.com"
                content = content.replace("atgmail", "@gmail.com")

                print(f"Typing content: {content}")
                pyautogui.write(content)
                time.sleep(WAIT_TIME_SHORT)

    if not cancel_mail and not send_mail:
        pyautogui.click(MAIL_SECTION_COORDINATES)
        time.sleep(WAIT_TIME_SHORT)

        while True:
            content = listen_continuous()
            if content:
                content = content.strip().lower()
                if STOP_COMMAND in content:
                    print("Stop command detected in 'Mail' section.")
                    break
                elif CANCEL_MAIL_COMMAND in content:
                    print("Cancel mail command detected. Canceling the mail...")
                    cancel_mail_function()
                    cancel_mail = True
                    break  # Exit the loop immediately when cancel mail command is detected
                elif SEND_MAIL_COMMAND in content:
                    print("Send mail command detected. Sending the mail...")
                    send_mail_function()
                    send_mail = True
                    break  # Exit the loop immediately when send mail command is detected
                elif STOP_EXECUTION_COMMAND in content:
                    print("Stop execution command detected. Exiting...")
                    exit()  # Exit the program when stop execution command is detected
                print(f"Typing content: {content}")
                pyautogui.write(content)
                time.sleep(WAIT_TIME_SHORT)

    # Call the corresponding functions based on flags
    if not cancel_mail and not send_mail:
        send_mail_function()

    # Reset flags after processing the commands
    send_mail = False
    cancel_mail = False


def send_mail_function():
    locate_and_click(SEND_BUTTON_IMAGE_PATH, "Send button")


def cancel_mail_function():
    locate_and_click(CANCEL_BUTTON_IMAGE_PATH, "Cancel button")


def execute_command(command):
    command = command.lower()  # Convert the command to lowercase for case-insensitive comparison
    if command == "open mail":
        open_mail_app()
    elif command == "compose":
        open_compose_section()
        type_to_content()
    elif command == "type mail":
        type_to_content()
    elif command == "send mail":
        send_mail_function()
    elif command == "cancel mail":
        cancel_mail_function()
    elif command == "stop typing":
        print("Stopping content typing...")
        # Additional actions if needed
    elif command == STOP_EXECUTION_COMMAND:
        print("Stop execution command detected. Exiting...")
        exit()


def main():
    print("Waiting for 'open mail' command...")
    while True:
        command = listen_continuous()
        if command and command == "open mail":
            break

    open_mail_app()
    while True:
        command = listen_continuous()
        if command:
            print(f"Command received: {command}")
            execute_command(command)


if __name__ == "__main__":
    main()
