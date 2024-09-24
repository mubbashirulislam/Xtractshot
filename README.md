
# Xtractshot

The Xtractshot is a Python-based utility designed for ethical hacking and system auditing purposes. It allows you to automatically capture and send screenshots of your system at a specified interval to a designated email address.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [Acknowledgements](#acknowledgements)

## Installation

To use the Xtractshot, you'll need to have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install the required dependencies using pip. Create a new file named `requirements.txt` in the project directory and add the following contents:

```
Pillow==9.5.0
smtplib==3.13.0
email-mime-multipart==3.0.8
email-mime-base==3.0.8
email-mime-text==3.0.8
```

Then, open a terminal or command prompt, navigate to the project directory, and run the following command:

```
pip install -r requirements.txt
```

This will install all the necessary dependencies for the X3NIDE Screenshot Capture Tool.

## Configuration

Before running the tool, you'll need to configure the following settings in the `config.py` file:

- `email_address`: Your email address
- `password`: Your email password
- `toaddr`: The email address you want to send the screenshots to
- `file_path`: The local directory where the screenshots will be saved
- `interval`: The interval in seconds between each screenshot capture

Make sure to update these values with your own information.

## Usage

To run the X3NIDE Screenshot Capture Tool, simply execute the `screenshot.py` script:

```
python screenshot.py
```

The tool will start capturing screenshots at the specified interval and send them to the configured email address. If there are any issues, the tool will log the errors and send an email notification.

You can stop the script by pressing `Ctrl+C` in the terminal or command prompt.

## Disclaimer

The X3NIDE Screenshot Capture Tool is designed for ethical hacking and system auditing purposes. It should only be used with proper consent and in compliance with local laws, regulations, and privacy standards. Any unauthorized use of this tool for malicious intent is strictly prohibited and punishable by law.

I, the developer, will not be responsible for any misuse or illegal activities conducted with this tool. It is your responsibility to ensure that your usage of this tool is within the boundaries of ethical and legal practices.

## Acknowledgements

This project was developed with the help of an AI assistant. The AI provided guidance and suggestions to enhance the functionality, optimize the code, and create a comprehensive README file.

I would like to acknowledge the valuable contribution of the AI assistant in the development of the X3NIDE Screenshot Capture Tool.
```

This README file covers the following:

1. **Installation**: Provides instructions on how to install the necessary Python dependencies using a `requirements.txt` file.
2. **Configuration**: Explains the configuration settings that need to be updated in the `config.py` file.
3. **Usage**: Describes how to run the `screenshot.py` script and stop the tool.
4. **Disclaimer**: Includes a clear disclaimer about the intended use of the tool and the developer's non-responsibility for any misuse or illegal activities.
5. **Acknowledgements**: Acknowledges the contribution of the AI assistant in the development of the tool.
