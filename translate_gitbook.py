#!/usr/bin/env python3
"""
GitBook Markdown Translation Script for Ukrainian
Preserves technical terms, code blocks, and formatting
Usage: python translate_gitbook.py [directory]
"""

import os
import re
import json
import time
import argparse
import frontmatter
from pathlib import Path
from deep_translator import DeeplTranslator, GoogleTranslator

class GitBookTranslator:
    def __init__(self, use_deepl=True):
        # Technical terms that should NOT be translated
        self.protected_terms = {
            # Assembly instructions
            'mov', 'push', 'pop', 'jmp', 'call', 'ret', 'add', 'sub', 'mul', 'div',
            'cmp', 'test', 'lea', 'xor', 'and', 'or', 'not', 'shl', 'shr', 'inc', 'dec',
            'nop', 'int', 'syscall', 'cpuid', 'rdtsc', 'hlt', 'cli', 'sti',
            
            # Registers (x86/x64)
            'eax', 'ebx', 'ecx', 'edx', 'esi', 'edi', 'esp', 'ebp', 'eip',
            'rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi', 'rsp', 'rbp', 'rip',
            'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15',
            'al', 'bl', 'cl', 'dl', 'ah', 'bh', 'ch', 'dh',
            'ax', 'bx', 'cx', 'dx', 'si', 'di', 'sp', 'bp',
            'cs', 'ds', 'es', 'fs', 'gs', 'ss',
            
            # ARM registers
            'r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10',
            'r11', 'r12', 'r13', 'r14', 'r15', 'sp', 'lr', 'pc', 'cpsr',
            'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9',
            'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17', 'x18',
            'x19', 'x20', 'x21', 'x22', 'x23', 'x24', 'x25', 'x26', 'x27',
            'x28', 'x29', 'x30',
            
            # Tools and technologies
            'gdb', 'lldb', 'radare2', 'r2', 'ida', 'ida pro', 'ghidra',
            'objdump', 'readelf', 'nm', 'strings', 'file', 'hexdump', 'xxd',
            'strace', 'ltrace', 'valgrind', 'perf', 'ltrace',
            'wireshark', 'tcpdump', 'netstat', 'ss', 'lsof',
            'python', 'perl', 'bash', 'sh', 'powershell', 'cmd',
            
            # Architectures and formats
            'x86', 'x64', 'x86_64', 'i386', 'amd64',
            'arm', 'arm64', 'aarch64', 'armv7', 'armv8',
            'mips', 'mips64', 'powerpc', 'ppc', 'sparc',
            'elf', 'pe', 'coff', 'macho', 'a.out',
            'got', 'plt', 'aslr', 'dep', 'nx', 'pie', 'relro',
            
            # Libraries and APIs
            'libc', 'glibc', 'musl', 'msvcrt', 'ucrtbase',
            'kernel32', 'ntdll', 'user32', 'advapi32',
            'malloc', 'free', 'printf', 'scanf', 'strcpy', 'strlen',
            'memcpy', 'memset', 'mmap', 'mprotect', 'execve',
            
            # File extensions and formats
            '.exe', '.dll', '.so', '.dylib', '.a', '.o', '.obj',
            '.c', '.cpp', '.h', '.hpp', '.py', '.pl', '.sh',
            '.asm', '.s', '.nasm', '.gas',
            
            # Protocols and standards
            'tcp', 'udp', 'ip', 'icmp', 'http', 'https', 'ftp', 'ssh',
            'ssl', 'tls', 'dns', 'dhcp', 'arp', 'rarp',
            
            # File systems and OS concepts
            'ext4', 'ntfs', 'fat32', 'hfs+', 'apfs',
            'proc', 'sys', 'dev', 'tmp', 'var', 'usr', 'opt',
            'windows', 'linux', 'macos', 'freebsd', 'openbsd',
            
            # Cryptographic terms (keep English for international consistency)
            'md5', 'sha1', 'sha256', 'sha512', 'crc32',
            'aes', 'des', '3des', 'rsa', 'dsa', 'ecdsa',
            'hmac', 'pbkdf2', 'scrypt', 'bcrypt',
        }
        
        # Ukrainian terminology mapping
        self.terminology_map = {
            'reverse engineering': 'зворотна інженерія',
            'reverse engineer': 'фахівець зі зворотної інженерії',
            'assembly language': 'мова асемблера',
            'assembly code': 'код асемблера',
            'assembly instruction': 'інструкція асемблера',
            'machine code': 'машинний код',
            'machine language': 'машинна мова',
            'debugging': 'налагодження',
            'debugger': 'налагоджувач',
            'debug': 'налагоджувати',
            'disassembly': 'дизасемблювання',
            'disassemble': 'дизасемблювати',
            'disassembler': 'дизасемблер',
            'decompilation': 'декомпіляція',
            'decompile': 'декомпілювати',
            'decompiler': 'декомпілятор',
            'binary analysis': 'аналіз бінарних файлів',
            'binary file': 'бінарний файл',
            'static analysis': 'статичний аналіз',
            'dynamic analysis': 'динамічний аналіз',
            'malware analysis': 'аналіз шкідливого ПЗ',
            'malware': 'шкідливе ПЗ',
            'executable': 'виконуваний файл',
            'library': 'бібліотека',
            'shared library': 'спільна бібліотека',
            'static library': 'статична бібліотека',
            'dynamic library': 'динамічна бібліотека',
            'instruction': 'інструкція',
            'opcode': 'код операції',
            'operand': 'операнд',
            'register': 'регістр',
            'memory': "пам'ять",
            'memory address': 'адреса пам\'яті',
            'address': 'адреса',
            'pointer': 'вказівник',
            'reference': 'посилання',
            'dereference': 'розіменування',
            'stack': 'стек',
            'stack frame': 'кадр стека',
            'stack pointer': 'вказівник стека',
            'heap': 'купа',
            'buffer': 'буфер',
            'overflow': 'переповнення',
            'buffer overflow': 'переповнення буфера',
            'stack overflow': 'переповнення стека',
            'heap overflow': 'переповнення купи',
            'underflow': 'антипереповнення',
            'shellcode': 'шелл-код',
            'payload': 'корисне навантаження',
            'exploit': 'експлойт',
            'vulnerability': 'вразливість',
            'security vulnerability': 'уразливість безпеки',
            'backdoor': 'чорний хід',
            'trojan': 'троян',
            'trojan horse': 'троянський кінь',
            'virus': 'вірус',
            'worm': 'мережевий черв\'як',
            'rootkit': 'руткіт',
            'spyware': 'шпигунське ПЗ',
            'adware': 'рекламне ПЗ',
            'ransomware': 'програма-вимагач',
            'encryption': 'шифрування',
            'decrypt': 'розшифровувати',
            'decryption': 'розшифрування',
            'encrypt': 'шифрувати',
            'cryptography': 'криптографія',
            'cryptographic': 'криптографічний',
            'hash': 'хеш',
            'hash function': 'хеш-функція',
            'checksum': 'контрольна сума',
            'digital signature': 'цифровий підпис',
            'signature': 'підпис',
            'certificate': 'сертифікат',
            'packer': 'пакувальник',
            'unpacker': 'розпакувальник',
            'packed': 'упакований',
            'unpacked': 'розпакований',
            'obfuscation': 'обфускація',
            'obfuscated': 'обфускований',
            'anti-debugging': 'протидія налагодженню',
            'anti-analysis': 'протидія аналізу',
            'evasion': 'ухилення',
            'sandbox': 'пісочниця',
            'virtual machine': 'віртуальна машина',
            'emulator': 'емулятор',
            'emulation': 'емуляція',
            'simulation': 'симуляція',
            'compiler': 'компілятор',
            'compilation': 'компіляція',
            'linker': 'компонувальник',
            'linking': 'компонування',
            'loader': 'завантажувач',
            'loading': 'завантаження',
            'runtime': 'середовище виконання',
            'function': 'функція',
            'procedure': 'процедура',
            'subroutine': 'підпрограма',
            'method': 'метод',
            'class': 'клас',
            'object': "об'єкт",
            'variable': 'змінна',
            'constant': 'константа',
            'parameter': 'параметр',
            'argument': 'аргумент',
            'return value': 'значення повернення',
            'calling convention': 'конвенція виклику',
            'system call': 'системний виклик',
            'api call': 'виклик API',
            'interrupt': 'переривання',
            'exception': 'виняток',
            'signal': 'сигнал',
            'process': 'процес',
            'thread': 'потік',
            'multithreading': 'багатопоточність',
            'synchronization': 'синхронізація',
            'mutex': 'мютекс',
            'semaphore': 'семафор',
            'race condition': 'стан гонитви',
            'deadlock': 'взаємоблокування',
            'file system': 'файлова система',
            'directory': 'каталог',
            'folder': 'папка',
            'permission': 'дозвіл',
            'privilege': 'привілей',
            'access control': 'контроль доступу',
            'authentication': 'автентифікація',
            'authorization': 'авторизація',
            'network': 'мережа',
            'networking': 'мережевий зв\'язок',
            'protocol': 'протокол',
            'packet': 'пакет',
            'frame': 'кадр',
            'header': 'заголовок',
            'footer': 'нижній колонтитул',
            'checksum': 'контрольна сума',
            'error correction': 'виправлення помилок',
            'compression': 'стиснення',
            'decompression': 'розпакування',
            'archive': 'архів',
            'backup': 'резервна копія',
            'restore': 'відновлення',
            'recovery': 'відновлення',
            'forensics': 'цифрова криміналістика',
            'forensic analysis': 'криміналістичний аналіз',
            'incident response': 'реагування на інциденти',
            'penetration testing': 'тестування на проникнення',
            'ethical hacking': 'етичний хакінг',
            'white hat': 'білий хакер',
            'black hat': 'чорний хакер',
            'gray hat': 'сірий хакер',
            'social engineering': 'соціальна інженерія',
            'phishing': 'фішинг',
            'spoofing': 'спуфінг',
            'man-in-the-middle': 'людина посередині',
            'denial of service': 'відмова в обслуговуванні',
            'distributed denial of service': 'розподілена відмова в обслуговуванні',
            'firewall': 'брандмауер',
            'intrusion detection': 'виявлення вторгнень',
            'intrusion prevention': 'запобігання вторгненням',
            'antivirus': 'антивірус',
            'anti-malware': 'анти-малвер',
            'endpoint protection': 'захист кінцевих точок',
        }
        
        # Initialize translator
        try:
            if use_deepl:
                self.translator = DeeplTranslator(source='en', target='uk')
            else:
                raise Exception("Using Google Translate as fallback")
        except:
            print("Deepl not available, using Google Translate...")
            self.translator = GoogleTranslator(source='en', target='uk')
        
        self.placeholders = {}
        self.placeholder_counter = 0
    
    def create_placeholder(self, content):
        """Create a unique placeholder for protected content"""
        placeholder = f"⟦PH_{self.placeholder_counter}⟧"
        self.placeholders[placeholder] = content
        self.placeholder_counter += 1
        return placeholder
    
    def protect_markdown_elements(self, text):
        """Protect various markdown elements from translation"""

        # Protect YAML/JSON frontmatter
        text = re.sub(r'^---[\s\S]*?---', lambda m: self.create_placeholder(m.group(0)), text, flags=re.MULTILINE)

        # Protect Markdown links (both text and URL)
        def protect_link(match):
            link_text = match.group(1)
            link_url = match.group(2)
            return self.create_placeholder(f"[{link_text}]({link_url})")

        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', protect_link, text)

        # Protect fenced code blocks
        text = re.sub(r'```[\s\S]*?```', lambda m: self.create_placeholder(m.group(0)), text)

        # Protect inline code
        text = re.sub(r'`[^`\n]+`', lambda m: self.create_placeholder(m.group(0)), text)

        # Protect HTML tags
        text = re.sub(r'<[^>]+>', lambda m: self.create_placeholder(m.group(0)), text)

        # Protect images (full syntax)
        text = re.sub(r'!\[[^\]]*\]\([^\)]+\)', lambda m: self.create_placeholder(m.group(0)), text)

        # Protect standalone URLs
        text = re.sub(r'https?://[^\s\)\]\}]+', lambda m: self.create_placeholder(m.group(0)), text)

        # Protect email addresses
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', lambda m: self.create_placeholder(m.group(0)), text)

        # Protect markdown headers (# only)
        text = re.sub(r'^(#{1,6})\s*', lambda m: self.create_placeholder(m.group(0)) + ' ', text, flags=re.MULTILINE)

        # Protect numbered lists
        text = re.sub(r'^(\d+\.)\s', lambda m: self.create_placeholder(m.group(1)) + ' ', text, flags=re.MULTILINE)

        # Protect bullet points
        text = re.sub(r'^([-*+])\s', lambda m: self.create_placeholder(m.group(1)) + ' ', text, flags=re.MULTILINE)

        # Protect blockquotes
        text = re.sub(r'^(>+)\s?', lambda m: self.create_placeholder(m.group(1)) + ' ', text, flags=re.MULTILINE)

        return text
    
    def protect_technical_terms(self, text):
        """Protect technical terms from translation"""
        for term in self.protected_terms:
            pattern = r'\b' + re.escape(term) + r'\b'
            text = re.sub(pattern, lambda m: self.create_placeholder(m.group(0)), text, flags=re.IGNORECASE)
        return text
    
    def apply_terminology_mapping(self, text):
        """Apply custom Ukrainian terminology"""
        for english, ukrainian in self.terminology_map.items():
            pattern = r'\b' + re.escape(english) + r'\b'
            text = re.sub(pattern, ukrainian, text, flags=re.IGNORECASE)
        return text
    
    def restore_placeholders(self, text):
        """Restore all protected content"""
        for placeholder, original in self.placeholders.items():
            text = text.replace(placeholder, original)
        return text
    
    def translate_text_chunk(self, text, max_length=4000):
        """Translate a chunk of text"""
        if len(text) <= max_length:
            try:
                return self.translator.translate(text)
            except Exception as e:
                print(f"Translation error: {e}")
                return text
        else:
            # Split into sentences and group them into chunks
            sentences = re.split(r'(?<=[.!?])\s+', text)
            chunks = []
            current_chunk = ""
            
            for sentence in sentences:
                if len(current_chunk + sentence) > max_length:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                        current_chunk = sentence
                    else:
                        # Single sentence is too long, split it further
                        chunks.append(sentence[:max_length])
                        current_chunk = sentence[max_length:]
                else:
                    current_chunk += " " + sentence if current_chunk else sentence
            
            if current_chunk:
                chunks.append(current_chunk.strip())
            
            # Translate each chunk
            translated_chunks = []
            for chunk in chunks:
                try:
                    translated = self.translator.translate(chunk)
                    translated_chunks.append(translated)
                    time.sleep(1)  # Rate limiting
                except Exception as e:
                    print(f"Translation error for chunk: {e}")
                    translated_chunks.append(chunk)
            
            return ' '.join(translated_chunks)
    
    def translate_content(self, text):
        """Main translation function with corrected order of operations."""
        if not text or not text.strip():
            return text
 
        # Reset placeholders for each content piece
        self.placeholders = {}
        self.placeholder_counter = 0
 
        try:
            # Step 1: Protect all non-translatable Markdown elements and URLs first.
            # This isolates the text that needs translation.
            protected_structure_text = self.protect_markdown_elements(text)
 
            # Step 2: NOW, protect the technical terms within the remaining text.
            protected_final_text = self.protect_technical_terms(protected_structure_text)
 
            # Step 3: Translate the text. The translation engine will not see
            # any of our placeholders, preventing them from being corrupted.
            translated_text = self.translate_text_chunk(protected_final_text)
 
            # Step 4: Restore all placeholders. The order of restoration doesn't matter.
            restored_text = self.restore_placeholders(translated_text)
 
            # Step 5: Finally, apply the terminology map to the fully translated text.
            # This ensures terms like "reverse engineering" are consistently translated.
            final_text = self.apply_terminology_mapping(restored_text)
 
            return final_text
 
        except Exception as e:
            print(f"Error translating content: {e}")
            # On error, try to restore what we can to avoid losing content
            return self.restore_placeholders(text)
 
    def process_markdown_file(self, file_path, backup=True):
        """Process a single markdown file"""
        print(f"Processing: {file_path}")
        
        # Create backup if requested
        if backup:
            backup_path = Path(str(file_path) + '.backup')
            if not backup_path.exists():
                import shutil
                shutil.copy2(file_path, backup_path)
                print(f"  Backup created: {backup_path}")
        
        try:
            # Read file with frontmatter support
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    post = frontmatter.load(f)
                    has_frontmatter = True
                except:
                    # Fallback to regular text file
                    f.seek(0)
                    content = f.read()
                    post = type('Post', (), {'content': content, 'metadata': {}})()
                    has_frontmatter = False
            
            # Translate main content
            if post.content.strip():
                print("  Translating content...")
                translated_content = self.translate_content(post.content)
            else:
                translated_content = post.content
            
            # Translate frontmatter if it exists
            if has_frontmatter and hasattr(post, 'metadata'):
                translated_metadata = {}
                for key, value in post.metadata.items():
                    if isinstance(value, str) and key in ['title', 'description', 'summary']:
                        print(f"  Translating {key}...")
                        translated_metadata[key] = self.translate_content(value)
                    else:
                        translated_metadata[key] = value
                post.metadata = translated_metadata
            
            # Write translated file
            with open(file_path, 'w', encoding='utf-8') as f:
                if has_frontmatter:
                    new_post = frontmatter.Post(translated_content, **post.metadata)
                    f.write(frontmatter.dumps(new_post))
                else:
                    f.write(translated_content)
            
            print(f"  ✓ Completed: {file_path}")
            time.sleep(2)  # Rate limiting between files
            
        except Exception as e:
            print(f"  ✗ Error processing {file_path}: {e}")
    
    def translate_gitbook(self, root_dir=".", skip_files=None, only_files=None):
        """Translate entire GitBook project"""
        root_path = Path(root_dir).resolve()
        print(f"Starting translation of GitBook at: {root_path}")
        
        skip_files = skip_files or []
        skip_files.extend(['.backup', 'node_modules', '.git', '_book', '.gitbook'])
        
        # Find all markdown files
        md_files = []
        
        if only_files:
            # Process only specified files
            for file_pattern in only_files:
                if '*' in file_pattern:
                    md_files.extend(root_path.glob(file_pattern))
                else:
                    file_path = root_path / file_pattern
                    if file_path.exists():
                        md_files.append(file_path)
        else:
            # Process all markdown files
            for md_file in root_path.rglob('*.md'):
                # Skip files in excluded directories
                if any(skip in str(md_file) for skip in skip_files):
                    continue
                md_files.append(md_file)
        
        print(f"Found {len(md_files)} markdown files to translate")
        
        # Process each file
        for i, md_file in enumerate(md_files, 1):
            print(f"\n[{i}/{len(md_files)}] {md_file.relative_to(root_path)}")
            self.process_markdown_file(md_file)
        
        print(f"\n✓ Translation completed! Processed {len(md_files)} files.")
        print("Don't forget to:")
        print("1. Review the translated content")
        print("2. Update book.json with Ukrainian settings")
        print("3. Test the GitBook build")
        print("4. Commit your changes")

def main():
    parser = argparse.ArgumentParser(
        description="Translate GitBook markdown files to Ukrainian"
    )
    parser.add_argument('directory', nargs='?', default='.', help='Directory containing the GitBook')
    parser.add_argument('--use-google', action='store_true', help='Use Google Translate instead of Deepl')
    parser.add_argument('--no-backup', action='store_true', help='Skip creating backup files')
    parser.add_argument('--only', nargs='+', help='Only translate specified files (supports wildcards)')
    parser.add_argument('--skip', nargs='+', default=[], help='Skip files/directories containing these patterns')
    
    args = parser.parse_args()
    use_deepl = not args.use_google
    translator = GitBookTranslator(use_deepl=use_deepl)
    translator.translate_gitbook(root_dir=args.directory, skip_files=args.skip, only_files=args.only)

if __name__ == "__main__":
    main()
