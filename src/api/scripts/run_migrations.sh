docker compose -f production.yml run django python3 /app/manage.py makemigrations users
docker compose -f production.yml run django python3 /app/manage.py makemigrations render_image
docker compose -f production.yml run django python3 /app/manage.py migrate