docker compose -f production.yml run django python3 /app/manage.py makemigrations bots
docker compose -f production.yml run django python3 /app/manage.py makemigrations kq_xo_so
docker compose -f production.yml run django python3 /app/manage.py migrate