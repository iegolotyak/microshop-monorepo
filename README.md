# Microshop Monorepo — ПЗ №3

Учебный Python-проект с микросервисами и автоматическим CI-конвейером в GitHub Actions.

## Структура

- `api_gateway/` — API Gateway (порт 5000, учебный маршрут `/health`)
- `products_service/` — каталог товаров (порт 5001)
- `customers_service/` — покупатели (порт 5002)
- `orders_service/` — заказы (порт 5003)
- `web_app/` — простая HTML-страница
- `test_products.py` — автоматические тесты API товаров
- `.github/workflows/ci_pipeline.yml` — GitHub Actions CI

## Запуск в PyCharm

1. Распакуйте архив, откройте папку `microshop-monorepo` через **File → Open**.
2. Выберите Python-интерпретатор, желательно Python 3.12.
3. Установите зависимости: `python -m pip install -r requirements.txt`.
4. Запустите тесты: `python -m pytest -v`.
5. Для запуска сервиса товаров: `python products_service/app.py`.

## Отправка в GitHub

В терминале PyCharm:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/iegolotyak/microshop-monorepo.git
git push -u origin main
```

Если Git уже был и `origin` существует, используйте `git remote set-url origin https://github.com/iegolotyak/microshop-monorepo.git`.

После первого push вкладка **Actions** запустит проверки Flake8 и Pytest автоматически.

## Проверка реакции CI на ошибку

В `products_service/app.py` временно измените строку импорта
`from flask import Flask, jsonify` на
`from flask import Flask, jsonify, nonexistent_function`.

Затем:

```powershell
git add products_service/app.py
git commit -m "Test CI import failure"
git push origin main
```

В GitHub Actions проверка `Run Unit Tests` должна завершиться с ошибкой импорта.
После демонстрации удалите `, nonexistent_function` и отправьте исправление.
