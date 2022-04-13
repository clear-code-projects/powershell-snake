if (![System.IO.Directory]::Exists("venv")) {
    Write-Host "creating virtual environment..."
    python3 -m venv venv

    Write-Host "installing dependencies..."
    .\venv\scripts\activate
    pip3 install -r requirements.txt
    deactivate
}

Write-Host "starting snek..."
[Console]::CursorVisible = $false
.\venv\Scripts\python.exe snake.py
[Console]::CursorVisible = $true
