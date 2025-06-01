# 🔍 Web Scraper - First <h1> Text with Selenium

This Python script uses **Selenium** to launch a browser, open a specified webpage, and extract the **first `<h1>` tag's text** from that page.

---

## 🚀 Features

- Launches a Chrome browser using `webdriver-manager`
- Opens a target URL (default: [pondit.com](https://www.pondit.com/))
- Extracts and prints the page title
- Extracts and prints the **first `<h1>` tag** text
- Gracefully closes the browser

---

## 🛠️ Requirements

Make sure you have Python installed. Then install the required Python packages:

```bash
pip install selenium webdriver-manager
