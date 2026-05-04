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

## ❓ Часто задаваемые вопросы (FAQ)

---

### 📦 Почему файл стал больше?

**Обфускация добавляет дополнительные слои кодирования и сжатия.** Чем больше слоёв — тем больше итоговый размер.

| Метод | Изменение размера |
|-------|-------------------|
| Zlib / Gzip / Lzma | **-70%** (уменьшение) |
| Base64 | **+33%** |
| Marshal | **+10%** |
| Multi-Layer (8+) | **+50–70%** |

---

### 🚀 Можно ли использовать для `.exe`?

**Да!** Проект поддерживает конвертацию EXE в Python-загрузчики.

| Режим | Описание |
|-------|----------|
| **9** | EXE → Python Stager (простой загрузчик) |
| **10** | EXE → Resource Injector (XOR шифрование) |
| **11** | EXE → Shellcode Embedder (фрагментированный) |

---

### 🔑 Как изменить XOR ключ?

По умолчанию используется ключ `b'STATIC_KEY_2024'`. **Рекомендуется заменить его** на свой.

1. Откройте файл `*_stager.py`
2. Найдите функцию `decrypt(data)`
3. Замените строку:

```python
# Было
key = hashlib.sha256(b'STATIC_KEY_2024').digest()

# Стало
key = hashlib.sha256(b'MY_SUPER_SECRET_KEY').digest()