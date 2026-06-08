### build app

poetry run pyinstaller --onefile `
  --name vpn-panel `
  --add-data "config;config" `
  src/app/main.py

poetry run pyinstaller `
  --onefile `
  --name panel-launcher `
  --add-data "config;config" `
  src/app/bootstrap/cli.py

poetry run pyinstaller `
  --onefile `
  --name panel-launcher `
  src/app/bootstrap/cli.py  