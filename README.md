
# 📸 Insta-OSINT

A powerful and beginner-friendly **Instagram OSINT (Open Source Intelligence) tool** that fetches key account information using the `Instaloader` library and other utilities. Useful for gathering insights about public Instagram profiles, including account type, user ID, creation trends, and more.

---

## 🚀 Features

- 🔍 Fetch public profile data by username
- 🆔 Estimate user ID and account creation year
- 🏷️ Detect account type (Personal / Creator / Business)
- 🖼️ Download profile picture and basic metadata
- 🎨 Fancy terminal banners using `pyfiglet`
- 📦 Easy setup with `requirements.txt`
- 💡 OSINT-ready — suitable for investigative, research, or cybersecurity tasks

---

## 🧠 How It Works

The tool uses:
- `Instaloader`: To fetch public Instagram profile data
- `Requests`: For any HTTP operations
- `PyFiglet`: For stylized terminal banners
- Python standard libraries like `json`, `os`, `random`, `string`, `time`

It also includes a data-based estimation of Instagram user ID ranges from **2010 to 2025**, enabling approximate account creation year lookup by user ID.

---

## 🛠️ Installation

```bash
git clone https://github.com/ankucode/insta-osint.git
cd insta-osint
pip install -r req.txt
python insta.py
```

---

## 📦 Requirements

- Python 3.7+
- `requests`
- `pyfiglet`
- `instaloader`

Install all dependencies with:

```bash
pip install -r req.txt
```

---

## 📸 Usage

```bash
python insta.py
```

You will be prompted to enter an Instagram username. The tool will then:

- Fetch the user ID
- Detect account type
- Estimate creation year (based on user ID ranges)
- Display and save profile data locally

---

## 🔐 Disclaimer

This tool only works with **public Instagram profiles**. It does not bypass authentication or access private user data. Use responsibly and in compliance with [Instagram’s Terms of Service](https://help.instagram.com/581066165581870).

---

## 👨‍💻 Developer

- 👤 **@Ankucode**
- 💬 Telegram: [@ankucode](https://t.me/ankucode)
- 🌐 GitHub: [github.com/ankucode](https://github.com/ankucode)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it with proper attribution.

---

## ⭐️ Support & Feedback

If you find this tool useful, please consider giving a ⭐️ to the repo and sharing it with others. For feedback or feature requests, contact me on Telegram: [@ankucode](https://t.me/ankucode)

