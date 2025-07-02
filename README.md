# Portfolio Web App

This is a Django-based portfolio web application for showcasing projects, skills, and blog posts. It uses Bootstrap 5 for styling and supports image uploads for projects and skills.

## Features

- Project showcase with images, descriptions, GitHub and live links
- Skills listing with proficiency levels and icons
- Blog post support (optional)
- Responsive design using Bootstrap 5
- Admin interface for content management
- Logging to `django_debug.log`

## Project Structure

```
capstone/
    capstone/         # Django project settings and URLs
    mywebsite/        # Main app: models, views, templates, static
    media/            # Uploaded images (projects, skills, blog)
    staticfiles/      # Collected static files for production
    db.sqlite3        # SQLite database
    manage.py
    requirements.txt
```

## Setup

1. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

2. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

3. **Create a superuser**
   ```sh
   python manage.py createsuperuser
   ```

4. **Run the development server**
   ```sh
   python manage.py runserver
   ```

5. **Access the site**
   - Main site: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Static & Media Files

- Place static files in `mywebsite/static/mywebsite/`
- Place uploaded images in `media/projects/` and `media/skills/`
- For production, run:
  ```sh
  python manage.py collectstatic
  ```
  and configure your web server to serve `/static/` from `staticfiles/` and `/media/` from `media/`.

## Environment Variables

- `DJANGO_SECRET_KEY`: Secret key for Django
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Deployment

- Use a WSGI server like Gunicorn or Waitress.
- **Important:** In production (`DEBUG = False`), Django does not serve static or media files. Use Nginx or Apache for this.

## License

See individual licenses for third-party libraries in the `staticfiles/admin/` directories.

---

Built with Django 4.2 and Bootstrap 5.