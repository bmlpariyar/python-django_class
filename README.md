# Python/Django Class Repository

## Project Overview
This repository contains materials for a Python class and each classes code will be proviede here.
## Project Slides
The project slides can be accessed through the following Google Drive link:
```bash
https://drive.google.com/drive/folders/1IXeVHChPpSF_rpQ8qGsvT3wpNnuZzSBu?usp=sharing
```
## Installation Guide

### 1. Installing Python
To get started, ensure you have Python installed on your computer:

- Download the latest version of Python from the [official Python website](https://www.python.org/downloads/)
- During installation, **check the option "`Add Python to PATH`"** to avoid any setup issues
- Verify installation by opening a terminal/command prompt and running:
  ```bash
  python --version
  # this should return:
  # python 3.x.x (latest version of python)
  ```

### 2. Installing Visual Studio Code (VS Code)
- Download VS Code from the [official VS Code website](https://code.visualstudio.com/)
- Follow the installation instructions for your operating system
- Complete the installation process

### 3. Installing the Python Extension for VS Code
- Open VS Code
- Navigate to the Extensions marketplace:
  - Windows/Linux: `Ctrl + Shift + X`
  - MacOS: `Cmd + Shift + X`
- Search for "Python"
- Click **Install** on the official Python extension by Microsoft

### 4. Cloning the Repository
There are two primary methods to clone the repository:

#### Using HTTPS:
```bash
git clone https://github.com/bmlpariyar/python-django_class
```
## Repository Structure
```
book_review_platform/
├── book_review_platform/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
```


## Django Project Setup

### Installing Django
First, ensure you have pip installed:
```bash
python -m pip install --upgrade pip
```

### Creating a Django Project

1. Create a Django Project Folder
```bash
mkdir Django
cd Django
```

2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
Note: The terminal should have venv at the start like:
```bash
(venv) path/to/your/project
```

3. Install Django:
```bash
pip install django
```

4. Verify Django Admin Commands
```bash
# Show all available Django admin commands
django-admin -h
```

5. Create Django Project
```bash
# Create a new Django project
django-admin startproject book_review_platform
```

6. Run Development Server
```bash
# Start the development server
python manage.py runserver
```
---
