# 🛡️ Cyber Security Web Programs

> **Experiment 8** — Web Scraping & Website Monitoring using Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-green?style=for-the-badge)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

## 📋 Overview

This repository contains Python programs for **Experiment 8** of the Cyber Security lab, focusing on **web scraping** techniques and **website change monitoring** — essential skills in cybersecurity for reconnaissance and threat detection.

---

## 📁 Programs

### 🔹 Part A — Web Scraping with BeautifulSoup

| File | Description |
|------|-------------|
| [`exp8a1.py`](exp8a1.py) | Scrapes and displays the **full HTML content** of a webpage using `prettify()` |
| [`exp8a2.py`](exp8a2.py) | Extracts all **`<p>` paragraph tags** and retrieves clean text without HTML markup |
| [`exp8a3.py`](exp8a3.py) | Finds elements by **ID and class selectors** to extract specific sections of a page |

### 🔹 Part B — Website Change Monitoring

| File | Description |
|------|-------------|
| [`exp8b1.py`](exp8b1.py) | Monitors a website for changes by comparing **SHA-224 hashes** at regular intervals |

---

## ⚙️ How It Works

### 🕷️ Web Scraping (Part A)

```
Website URL → HTTP GET Request → Parse HTML with BeautifulSoup → Extract & Display Data
```

All three programs scrape [Wikipedia's Main Page](https://en.wikipedia.org/wiki/Main_Page) and demonstrate different levels of data extraction:

1. **Full page dump** — view the entire HTML structure
2. **Tag-based filtering** — extract all paragraphs
3. **Targeted extraction** — find specific elements by ID/class

### 🔍 Website Monitoring (Part B)

```
Fetch Page → Generate SHA-224 Hash → Wait 30s → Re-fetch → Compare Hashes
                                                                |
                                              Match? → Continue monitoring
                                           No Match? → Alert "something changed"
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install beautifulsoup4 requests
```

### Run any program

```bash
python exp8a1.py    # Full HTML scrape
python exp8a2.py    # Extract paragraphs
python exp8a3.py    # Extract by ID/class
python exp8b1.py    # Monitor for changes (runs continuously)
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core programming language |
| **BeautifulSoup4** | HTML parsing and data extraction |
| **Requests** | HTTP requests to fetch web pages |
| **Hashlib** | SHA-224 hashing for change detection |
| **urllib** | URL handling and SSL context |

---

## 📖 Key Concepts

- **Web Scraping** — Automated extraction of data from websites, widely used in OSINT (Open Source Intelligence)
- **HTML Parsing** — Navigating the DOM tree to locate and extract specific elements
- **Integrity Monitoring** — Detecting unauthorized changes to web content using cryptographic hashes
- **SHA-224 Hashing** — A secure hash algorithm used to create a unique fingerprint of web content

---

## 👤 Author

**Dhineshkumar** — Cyber Security Student

---

<p align="center">
  <i>⭐ Star this repo if you found it helpful!</i>
</p>