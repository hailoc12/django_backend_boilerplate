docker compose -f production.yml run django python3 /app/manage.py makemigrations
docker compose -f production.yml run django python3 /app/manage.py migrate