# Saalaya - Phishing URL Masking Tool (For Educational Use Only)

**Saalaya** is a Python-based tool that allows you to generate masked phishing URLs by combining a shortened malicious link with a legitimate-looking domain and optional social engineering keywords. **This tool is intended for educational purposes only** and should be used to raise awareness of phishing techniques and how to defend against them.

## Features

- Validates the format of both phishing and masking URLs.
- Shortens the phishing URL using the `is.gd` URL shortening service.
- Allows you to mask the phishing URL with a legitimate-looking domain.
- Optionally adds social engineering keywords to make the link appear more convincing.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Educational Use Only](#educational-use-only)
- [License](#license)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Sayuru99/saalaya.git
   cd saalaya
   ```

2. **Install Dependencies:**
   The script requires Python 3.x and the `requests` library to make HTTP requests.

   You can install the required package using pip:

   ```bash
   pip install requests
   ```

## Usage

Run the Python script and follow the prompts:

```bash
python saalaya.py
```

### Prompts:

1. **Phishing URL**: Paste the malicious URL (must start with `http` or `https`).
2. **Masking Domain**: Enter a legitimate-looking domain (e.g., `https://google.com`) to mask the phishing URL.
3. **Social Engineering Words**: Optionally, provide social engineering words (e.g., `free-money`) to make the link more enticing. Avoid using spaces; use hyphens (`-`) instead.

### Example

**Input phishing URL**:  
`http://malicious-site.com`

**Shortened URL**:  
`https://is.gd/abc123`

**Masking domain**:  
`https://google.com`

**Social engineering words**:  
`free-money`

**Generated masked phishing URL**:  
`https://google.com-free-money@is.gd/abc123`

## Educational Use Only

This tool is strictly for educational purposes. It is designed to help cybersecurity professionals and educators understand phishing techniques, demonstrate how attackers can manipulate URLs, and raise awareness of how to defend against these types of attacks.

### Disclaimer:

- **Do not use this tool for illegal or unethical activities**. Phishing is a criminal activity, and unauthorized use of this tool for creating malicious URLs could result in legal consequences.
- This tool should only be used in controlled environments (e.g., security research, penetration testing with permission) or for educational demonstrations with the clear goal of raising awareness.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
