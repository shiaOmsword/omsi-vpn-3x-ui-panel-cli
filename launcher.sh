#!/usr/bin/env bash

# включаем выход при ошибке
set -e

# переходим в папку, где лежит сам .sh файл
cd "$(dirname "$0")"

# заголовок терминала, работает не везде, но обычно ок
printf '\033]0;Panel Launcher\007'

poetry run launch menu --config config/local.yml

echo
echo "Launcher finished."

read -r -p "Press Enter to exit..."