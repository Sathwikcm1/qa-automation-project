# QA Automation Project - Selenium + Pytest

## 🔧 Tools Used
- Selenium (Firefox WebDriver)
- Pytest
- pytest-html (for reports)
- Python 3.x

## 📄 Test Cases
1. Invalid Login - Shows error
2. Valid Login - Logs in successfully and shows dashboard

## 🚀 To Run Tests
```bash
pip install -r requirements.txt
pytest test_login.py --html=reports/report_$(date +%Y%m%d_%H%M%S).html

