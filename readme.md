# Caesar Cipher Program 🛡️

This project implements a classic Caesar cipher, allowing users to encrypt and decrypt text by shifting letters a specified number of positions in the alphabet. It provides a command-line interface for easy interaction and utilizes modular design for maintainability and readability. This program is designed to be a simple, educational tool for understanding basic cryptography.

## 🚀 Features

- **Encryption:** Encodes text by shifting each letter forward by a specified number of positions. Special characters remain unchanged.
- **Decryption:** Decodes text by shifting each letter backward by the specified number of positions. Special characters remain unchanged.
- **User-Friendly Interface:** Provides a command-line interface for easy interaction.
- **Modular Design:** Separates core cipher logic from user interface and data storage.
- **Special Character Handling:** Ignores special characters during encryption and decryption.
- **Alphabet Wrapping:** Handles shifting beyond the end of the alphabet by wrapping around to the beginning.
- **Input Validation:** Checks if the direction given is either "encode" or "decode".

## 🛠️ Tech Stack

- **Language:** Python 🐍
- **Core Logic:** `ceaser_cipher` function
- **Alphabet & Special Characters:** `mywordslist.py`
- **ASCII Art:** `arts.py`

## 📦 Installation

### Prerequisites

- Python 3.x installed on your system.

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd caesar-cipher
    ```

2.  No additional dependencies need to be installed as all the dependencies are in-house.

## 💻 Usage

1.  Run the `main.py` file:

    ```bash
    python main.py
    ```

2.  Follow the prompts to enter the desired operation (encode/decode), text, and shift value.

## 📂 Project Structure

```
caesar-cipher/
├── main.py          # Main program file with user interface and logic
├── mywordslist.py   # Defines the alphabet and special characters
├── arts.py          # Contains ASCII art for the program
└── README.md        # Documentation for the project
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests with improvements or bug fixes.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes.
4.  Push to the branch.
5.  Submit a pull request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Muhammad-Ali-5331/Caesar-Cipher-Tool-Python/blob/main/LICENSE) file for details.

## 📬 Contact

If you have any questions or suggestions, feel free to contact me at [malitariq5324@gmail.com](mailto:malitariq5324@gmail.com).

## 💖 Thanks Message

Thank you for checking out this Caesar Cipher program! I hope you find it useful and educational.
