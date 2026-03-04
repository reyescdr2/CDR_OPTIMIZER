@echo off
echo Compilando cdr_engine.cpp a cdr_engine.dll...
C:\ProgramData\mingw64\mingw64\bin\g++.exe -O3 -shared -o cdr_engine.dll cdr_engine.cpp "-Wl,--subsystem,windows" -lpsapi -ladvapi32
if %errorlevel% neq 0 (
    echo Error durante la compilacion.
    exit /b %errorlevel%
)
echo Compilacion exitosa.
