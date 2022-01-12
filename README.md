# url-shortener

ACE Coding Exercise: URL Shortener

Required packages

```bash
Django==3.2.7
django-environ==0.6.0
google-cloud-secret-manager==2.7.0
numpy==1.21.2
```

---

Steps required to run locally after pulling code:

1. Run Django migrations to setup models

   ```bash
   python manage.py makemigrations
   python manage.py makemigrations shrinker
   python manage.py migrate
   ```
2. Start Django web server

   ```bash
   python manage.py runserver
   ```
3. Open generated link and enjoy shrinking urls!

---

Steps to run local tests:

```bash
python manage.py test shrinker.tests
```
