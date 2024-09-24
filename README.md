
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

Before running the tool, you'll need to configure the following settings in the `configuration` section:

- `email_address`: Your email address
- `password`: Your email password
- `toaddr`: The email address you want to send the screenshots to
- `file_path`: The local directory where the screenshots will be saved
- `interval`: The interval in seconds between each screenshot capture

Make sure to update these values with your own information.

## Usage

To run the Xtractshot, simply execute the `screenshot.py` script:

```
python screenshot.py
```

The tool will start capturing screenshots at the specified interval and send them to the configured email address. If there are any issues, the tool will log the errors and send an email notification.

You can stop the script by pressing `Ctrl+C` in the terminal or command prompt.

## Disclaimer

The Xtractshot is designed for ethical hacking and system auditing purposes. It should only be used with proper consent and in compliance with local laws, regulations, and privacy standards. Any unauthorized use of this tool for malicious intent is strictly prohibited and punishable by law.

I, Mubbashirul Islam, will not be responsible for any misuse or illegal activities conducted with this tool. It is your responsibility to ensure that your usage of this tool is within the boundaries of ethical and legal practices.

## Acknowledgements

Created by **Mubbashirul Islam** (a.k.a **X3NIDE**), using my own knowledge and with the assistance of AI.

Feel free to contribute or reach out for further improvements!


