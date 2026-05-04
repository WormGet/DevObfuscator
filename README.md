# 🜁 Advanced Obfuscator v2.0

**Многофункциональный обфускатор Python и EXE файлов с поддержкой различных методов шифрования и генерации загрузчиков.**

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

---

## 📌 Возможности

### 🔧 Для Python файлов:
- Marshal кодирование
- Zlib/Lzma/Gzip компрессия
- Base16/Base32/Base64 кодирование
- Многослойная обфускация (до 40 комбинаций)
- Автоматическая компиляция в `.pyc`

### 🚀 Для EXE файлов:
- **Режим 9:** EXE → Python Stager (Zlib + Base64)
- **Режим 10:** EXE → Resource Injector (XOR + Zlib + Base64)
- **Режим 11:** EXE → Shellcode Embedder (Чанковая обфускация)

---

## 📦 Установка

```bash
# Клонирование репозитория
git clone https://github.com/yourusername/advanced-obfuscator.git
cd advanced-obfuscator

# Установка зависимостей
pip install pyinstaller  # Для сборки загрузчиков (опционально)

# 🎮 Использование

## 🚀 Запуск

```bash
python obfuscator.py



╔══════════════════════════════════════════════════════════════╗
║                      🜁 MAIN MENU 🜁                         ║
╠══════════════════════════════════════════════════════════════╣
║  [1]  Encode Marshal (PY)                                    ║
║  [2]  Encode Zlib (PY)                                       ║
║  [3]  Encode Base16 (PY)                                     ║
║  [4]  Encode Base32 (PY)                                     ║
║  [5]  Encode Base64 (PY)                                     ║
║  [6]  Encode Lzma (PY)                                       ║
║  [7]  Encode Gzip (PY)                                       ║
║  [8]  Multi-Layer Encode (PY)                                ║
║  [9]  EXE -> Python Stager (PY)                              ║
║ [10]  EXE -> Resource Injector (EXE)                         ║
║ [11]  EXE -> Shellcode Embedder (PY)                         ║
║ [12]  Exit                                                   ║
╚══════════════════════════════════════════════════════════════╝


<details> <summary><b>Почему файл стал больше?</b></summary> <br> Обфускация добавляет дополнительные слои кодирования/сжатия. Multi-Layer методы могут увеличить размер на 50-70%. </details><details> <summary><b>Можно ли использовать для .exe?</b></summary> <br> Да! Режимы 9, 10, 11 специально для конвертации EXE в Python загрузчики. </details><details> <summary><b>Как изменить XOR ключ?</b></summary> <br> В файле замените `b'STATIC_KEY_2024'` на свой ключ в функции `decrypt()`. </details>