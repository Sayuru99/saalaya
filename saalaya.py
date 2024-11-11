import re
import requests

def url_checker(url):
    """Validate if the URL starts with http or https."""
    pattern = re.compile(r"^https?://")
    if not pattern.match(url):
        raise ValueError("Invalid URL. Please use a valid URL that starts with http or https.")

def shorten_url(phish_url):
    """Shorten the phishing URL using is.gd service."""
    try:
        response = requests.get(f"https://is.gd/create.php?format=simple&url={phish_url}")
        if response.status_code == 200:
            return response.text
        else:
            raise ConnectionError(f"Failed to shorten URL. Status code: {response.status_code}")
    except requests.RequestException as e:
        raise ConnectionError(f"Error shortening URL: {e}")

def generate_masked_url(mask, words, shortened_url):
    """Generate the masked phishing URL using a legitimate domain and social engineering words."""
    short_url = shortened_url.replace("https://", "").replace("http://", "")
    
    if words:
        return f"{mask}-{words}@{short_url}"
    else:
        return f"{mask}@{short_url}"

def main():
    print("\n###### Phishing URL Masking Tool ######")
    
    phish_url = input("Paste the phishing URL (must start with http or https): ").strip()
    
    try:
        url_checker(phish_url)
    except ValueError as ve:
        print(f"[!] {ve}")
        return
    
    try:
        print("Shortening the phishing URL...")
        short_url = shorten_url(phish_url)
    except ConnectionError as ce:
        print(f"[!] {ce}")
        return
    
    print(f"[+] Shortened URL: {short_url}")
    
    mask = input("Enter the domain to mask the phishing URL (e.g., https://google.com): ").strip()
    
    try:
        url_checker(mask)
    except ValueError as ve:
        print(f"[!] {ve}")
        return
    
    print('Enter social engineering words (e.g., free-money, best-pubg-tricks):')
    print("[!] Don't use spaces; use '-' instead of spaces.")
    words = input("Social engineering words: ").strip()
    
    if ' ' in words:
        print("[!] Invalid input: Social engineering words should not contain spaces.")
        return
    
    masked_url = generate_masked_url(mask, words, short_url)
    
    print("\n[+] Generated Masked Phishing URL:")
    print(f"{masked_url}\n")

if __name__ == "__main__":
    main()
