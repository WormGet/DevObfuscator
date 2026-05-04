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


<details>
<summary><b>❓ Почему файл стал больше?</b></summary>
<br>
Обфускация добавляет дополнительные слои кодирования и сжатия. Чем больше слоёв — тем больше итоговый размер.
<br><br>
📊 <b>Ориентировочное увеличение:</b>
<ul>
  <li>Zlib/Gzip/Lzma: -70% (размер уменьшается)</li>
  <li>Base64: +33% (увеличивается)</li>
  <li>Marshal: +10%</li>
  <li>Multi-Layer (8+ слоёв): +50-70%</li>
</ul>
</details>

<br>

<details>
<summary><b>❓ Можно ли использовать для .exe?</b></summary>
<br>
Да! Проект поддерживает конвертацию EXE файлов в Python загрузчики.
<br><br>
⚙️ <b>Доступные режимы:</b>
<ul>
  <li><b>Режим 9</b> — EXE → Python Stager (простой загрузчик)</li>
  <li><b>Режим 10</b> — EXE → Resource Injector (XOR шифрование)</li>
  <li><b>Режим 11</b> — EXE → Shellcode Embedder (фрагментированный)</li>
</ul>
</details>

<br>

<details>
<summary><b>❓ Как изменить XOR ключ?</b></summary>
<br>
По умолчанию используется ключ <code>b'STATIC_KEY_2024'</code>. Для повышения безопасности рекомендуется его заменить.
<br><br>
🔧 <b>Как изменить:</b>
<ol>
  <li>Откройте сгенерированный файл <code>*_stager.py</code></li>
  <li>Найдите функцию <code>decrypt(data)</code></li>
  <li>Замените строку:</li>
</ol>

```python
# Было:
key = hashlib.sha256(b'STATIC_KEY_2024').digest()

# Стало (пример):
key = hashlib.sha256(b'MY_SUPER_SECRET_KEY_9876').digest()
