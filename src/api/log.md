============================= test session starts ==============================
platform linux -- Python 3.10.4, pytest-7.1.2, pluggy-1.0.0 -- /usr/bin/python3
cachedir: .pytest_cache
django: settings: config.settings.test (from option)
rootdir: /app, configfile: pytest.ini
plugins: django-4.5.2
collecting ... collected 2 items

bot_xsmb/crawler/tests/test_task.py::TestCrawlTasks::test_crawl_xsmb_today_result_task 

=============================== warnings summary ===============================
../usr/local/lib/python3.10/dist-packages/kombu/utils/compat.py:82
  /usr/local/lib/python3.10/dist-packages/kombu/utils/compat.py:82: DeprecationWarning: SelectableGroups dict interface is deprecated. Use select.
    for ep in importlib_metadata.entry_points().get(namespace, [])

../usr/local/lib/python3.10/dist-packages/django/apps/registry.py:91
  /usr/local/lib/python3.10/dist-packages/django/apps/registry.py:91: RemovedInDjango41Warning: 'django_better_admin_arrayfield' defines default_app_config = 'django_better_admin_arrayfield.apps.DjangoBetterAdminArrayfieldConfig'. Django now detects this configuration automatically. You can remove default_app_config.
    app_config = AppConfig.create(entry)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================= 2 warnings in 1.03s ==============================
