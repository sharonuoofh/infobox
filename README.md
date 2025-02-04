# InfoBox

InfoBox is a Python program designed to provide easy-to-use encryption for files and folders, helping to secure your data on Windows devices. This lightweight tool uses symmetric encryption to protect your files from unauthorized access.

## Features

- Encrypt individual files or entire folders
- Decrypt individual files or entire folders
- Generates a unique encryption key for each session
- Saves the encryption key to a specified file for future use
- Supports any file type

## Prerequisites

- Python 3.6 or later
- `cryptography` library (`pip install cryptography`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/infobox.git
   ```

2. Navigate to the project directory:

   ```bash
   cd infobox
   ```

3. Install required dependencies:

   ```bash
   pip install cryptography
   ```

## Usage

To use InfoBox, run the script with the following command:

```bash
python infobox.py <encrypt/decrypt> <file/folder path> <key file>
```

- `<encrypt/decrypt>`: Specify whether you want to encrypt or decrypt.
- `<file/folder path>`: Path to the file or folder you want to process.
- `<key file>`: Path to the file where the encryption key will be saved or loaded from.

### Example

To encrypt a folder:

```bash
python infobox.py encrypt "C:/path/to/your/folder" "C:/path/to/keyfile.key"
```

To decrypt the same folder:

```bash
python infobox.py decrypt "C:/path/to/your/folder" "C:/path/to/keyfile.key"
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is meant for educational purposes only. Use it responsibly and ensure you comply with all local laws and regulations regarding data encryption.