# VoiceControlledMailComposer

VoiceControlledMailComposer is a Python script that enables users to compose and send emails using speech recognition and automation. The project utilizes the SpeechRecognition library for voice input and PyAutoGUI for automating mouse and keyboard actions.

## Features

- **Speech Recognition:** Converts spoken words into text for email composition.
- **Automation:** Automates the process of typing and sending emails based on voice commands.
- **Interactive:** Responds to voice commands in real-time for a hands-free email composition experience.

## Prerequisites

- Python 3.x
- Install required Python packages using `pip install -r requirements.txt`

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/Shashank-LS/VoiceControlledMailComposer.git
    cd VoiceControlledMailComposer
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python voice_mail_composer.py
    ```

4. Follow the on-screen instructions to open the mail app and compose/send/cancel emails using voice commands.

## Usage

- **Open Mail App:** Say "Open Mail" to launch the specified mail application.
- **Compose Email:** Say "Compose" to open the compose section and start dictating the email content.
- **Type Email:** Use the script to continue typing and send or cancel the email.

## Commands

- **Open Mail:** Say "Open Mail" to open the mail application.
- **Mail Composing:** Say "Compose" to Write the mail.
- **Stop Typing:** Say "Stop Typing" to exit the current typing mode and to enter next.
- **"While typing the content say @gmal insted of @gmail.com"**
- **Send Email:** Say "Send Mail" to send the composed email.
- **Cancel Email:** Say "Cancel Mail" to cancel the email composition.

## Contributing

Contributions are welcome! If you have ideas for improvements, open an issue or create a pull request.

## License

This project is licensed under the GUN v3.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)

