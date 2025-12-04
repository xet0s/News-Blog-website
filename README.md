# Haber/Blog sitesi

Bu proje Hitit Üniversitesi Bilgisayar Mühendisliği bölümü Web Teknolojileri dersi kapsamında geliştirilmiş bir projedir.
Projedeki ana amaç özel yetkilendirilmiş kullanıcıların girdi girmesi sayesinde oluşacak bir haber veya blog sitesi oluşumudur. 
Projede konu etiketleri statik olmak yerine dinamik şekilde admin panelinden düzenlenmektedir. Aynı zamanda içeriklerin okura düşmesinden önce admin panelde yönetici onayı beklemesi için ayarlanmış bir sistem bulunmaktadır.

🔗 **Canlı Demo** https://e-shiro.com/

## Kullanılan Teknolojiler
**Frontend:** Bootstrap 
**Backend:** Django
**Veritabanı:** MySql

## Mevcut ve Eklenecen özellikler

✅ Kullanıcı kayıt ve giriş formu

✅ Basit içerik ekleme formu

## Kurulum

Projeyi kendi cihazınıza kurmak için sırasıyla:
1-Projeyi klonlayın

2-Sanal ortam kurun
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3-requirements.txt dosyasını 

    ```bash
    pip install -r requirements.txt
    ```

4-Projeyi aşağıdaki kod ile başlatın:

    ```bash
    python manage.py runserver
    # or
    python3 manage.py runserver
    # or
    py manage.py runserver
    ```
5-Verilen localhost linkini tarayıcıda açın
    `http://127.0.0.1:8000/`
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# News & Blog Platform

This project was developed within the scope of the **Web Technologies** course at **Hitit University, Computer Engineering Department**.

## 📄 About

The main goal of this project is to create a news or blog platform where specifically authorized users can submit content.

**Key Highlights:**
* **Dynamic Tags:** Subject tags are not static; they are managed dynamically via the admin panel.
* **Approval System:** Content does not go live immediately. There is a workflow requiring administrator approval in the admin panel before posts are published to readers.

🔗 **Live Demo:** [https://e-shiro.com/](https://e-shiro.com/)

## 🛠️ Tech Stack

* **Frontend:** Bootstrap
* **Backend:** Django
* **Database:** MySQL

## 🚀 Features

* ✅ User registration and login forms
* ✅ Simple content submission form
* *(More features to be added)*

## 💻 Installation

Follow these steps to set up the project on your local machine:

1.  **Clone the project:**


2.  **Set up a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the server:**
    Use one of the following commands depending on your Python installation:
    ```bash
    python manage.py runserver
    # or
    python3 manage.py runserver
    # or
    py manage.py runserver
    ```

5.  **View the app:**
    Open the provided localhost link (usually `http://127.0.0.1:8000/`) in your browser
   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
