start "env Elementar" cmd.exe @cmd /K "cd elementar && virtualenv venv && cd venv/Scripts && activate && cd ../../ && pip install -r requirements.txt && app.py"

start "env Logs" cmd.exe @cmd /K "cd logs && virtualenv venv && cd venv/Scripts && activate && cd ../../ && pip install -r requirements.txt && app.py"

start "env Transcendental" cmd.exe @cmd /K "cd transcendental && virtualenv venv && cd venv/Scripts && activate && cd ../../ && pip install -r requirements.txt && app.py"

start "env Gateway" cmd.exe @cmd /K "cd gateway && virtualenv venv && cd venv/Scripts && activate && cd ../../ && pip install -r requirements.txt && app.py"

start "env Aplicação" cmd.exe @cmd /K "cd app && virtualenv venv && cd venv/Scripts && activate && cd ../../ && pip install -r requirements.txt && app.py"