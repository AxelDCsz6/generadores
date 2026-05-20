@echo off
echo === Compilando Generador de Obra para Windows ===
echo.

:: Verificar que Python este instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado.
    echo Descargalo desde https://www.python.org/downloads/
    echo Asegurate de marcar "Add Python to PATH" al instalar.
    pause
    exit /b 1
)

echo Instalando dependencias...
pip install pyperclip pyinstaller --quiet

echo.
echo Compilando ejecutable...
python -m PyInstaller --onefile --console --name "GeneradorDeObra" generadores.py

echo.
if exist "dist\GeneradorDeObra.exe" (
    echo Listo! El archivo esta en: dist\GeneradorDeObra.exe
    echo Puedes copiar ese archivo a cualquier PC con Windows.
) else (
    echo Algo salio mal. Revisa los mensajes de error arriba.
)

pause
