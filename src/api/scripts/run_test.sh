# docker compose -f production.yml run django pytest -v -s --tb=long /app/bot_xsmb/crawler/tests
docker compose -f production.yml run django pytest -v -s --tb=long /app/bot_xsmb/bots/tests/test_bot_features.py
# docker compose -f production.yml run django pytest -v -s --tb=long /app/bot_xsmb/kq_xo_so/tests/test_analysis.py