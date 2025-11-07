# Лабораторная работа №5 — Знакомство с CI/CD (GitHub Actions) для проекта `geom2d`

Этот репозиторий продолжает ЛР4: те же тесты `unittest`, плюс настроен workflow `main.yml`,
который запускается на **ubuntu-latest** и **windows-latest** после каждого `push` и `pull_request`.

## Запуск локально
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
