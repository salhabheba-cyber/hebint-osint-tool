# 🕵️ HEBINT - Advanced OSINT Investigation Tool

<div align="center">
  
  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
  [![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
  [![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-orange?style=for-the-badge)]()
  [![OSINT](https://img.shields.io/badge/OSINT-Username%20%7C%20Email%20%7C%20Phone-red?style=for-the-badge)]()
  
  <h3>🔍 Search 150+ platforms for usernames, emails, and phone numbers</h3>
  <p><i>Built with ❤️ in Beirut, Lebanon</i></p>
  
</div>

---




<div align="center">
  
### Main Interface
<img src="screenshots/01.png" width="600"/>

### Facebook Search Links
<img src="screenshots/02.png" width="600"/>

### Results Summary
<img src="screenshots/03.png" width="600"/>

### Email Module Working
<img src="screenshots/04.png" width="600"/>

### Phone Module Working
<img src="screenshots/05.png" width="600"/>

### Colors Complete
<img src="screenshots/06.png" width="600"/>

### Username Search
<img src="screenshots/07.png" width="600"/>

### Recording Demo
<img src="screenshots/08.png" width="600"/>

### Working Results
<img src="screenshots/09.png" width="600"/>

</div>

---

## 📋 Overview

**HEBINT** (pronounced "Heh-bint", short for **He**ba **B**eirut **INT**elligence) is a powerful OSINT tool that automates the process of searching for usernames, emails, and phone numbers across **150+ platforms**. It's designed for security researchers, investigators, and cybersecurity professionals.

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| **150+ Platforms** | Social media, coding sites, gaming, Arabic platforms |
| **Arabic Support** | **UNIQUE!** Searches Anazahra, ArabChat, Mawada, DubaiChat |
| **Colored Output** | Beautiful terminal output with color-coded results |
| **JSON Export** | All results saved to structured JSON files |
| **Facebook Links** | Always visible even without profiles |
| **Concurrent Checks** | 20 simultaneous connections for speed |
| **Email Module** | Email investigation capabilities |
| **Phone Module** | Phone number lookup |

---



![Uploading email.py.png…]()


## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/hebint.git
cd hebint

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run the tool
python modules/hebint_username.py
