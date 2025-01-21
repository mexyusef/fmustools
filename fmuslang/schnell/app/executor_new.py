import os
import re
import subprocess

if __name__ == '__main__':
    import sys
    from dotenv import load_dotenv
    load_dotenv(r"C:\Users\usef\work\sidoarjo\schnell\.env.crypt")
    sys.path.insert(0, r"c:\users\usef\work\sidoarjo")

from schnell.app.dirutils import tempdir, timestamp
from schnell.app.fileutils import copy_content

class FileExecutor:
    def __init__(self, language='py', base_dir=None):
        self.language = self.cleanup_language(language)
        self.assign(base_dir)

    def assign(self, base_dir=None):
        self.folder = base_dir if base_dir and os.path.isdir(base_dir) else tempdir()
        self.filename_noext = f'delete_{timestamp()}'
        self.filename = f'{self.filename_noext}.{self.get_extension(self.language)}'
        self.filepath = os.path.join(self.folder, self.filename)

    def cleanup_language(self, language):
        lang_map = {'py': 'python', 'rs': 'rust', 'cpp': 'cpp', 'clang': 'clang', 'java': 'java', 'kt': 'kotlin', 'cs': 'csharp', 'clj': 'clojure', 'js': 'javascript', 'sh': 'shell', 'hs': 'haskell', 'scala': 'scala'}
        return lang_map.get(language, language)

    def get_extension(self, language):
        ext_map = {'python': 'py', 'rust': 'rs', 'cpp': 'cpp', 'clang': 'cpp', 'java': 'java', 'kotlin': 'kt', 'csharp': 'cs', 'clojure': 'clj', 'javascript': 'js', 'shell': 'sh', 'haskell': 'hs', 'scala': 'scala'}
        return ext_map.get(language, 'txt')

    def exec_file(self, filepath):
        copy_content(filepath)
        self.execute()

    def execute(self, language=None, content=None):
        if language:
            self.language = self.cleanup_language(language)
            self.assign()

        handler = getattr(self, f'handle_{self.language}', None)
        if handler:
            handler(content)
        else:
            print(f"No handler for language: {self.language}")

    def handle_python(self, content=None):
        self.run_command(f'python {self.filepath}', content)

    def handle_rust(self, content=None):
        self.run_command(f'rustc {self.filepath} && {self.filename_noext}', content)

    def handle_cpp(self, content=None):
        output_filepath = f'{self.filename_noext}.exe'
        self.run_command(f'g++ {self.filepath} -o {output_filepath} && {output_filepath}', content)

    def handle_clang(self, content=None):
        output_filepath = f'{self.filename_noext}.exe'
        self.run_command(f'clang++ {self.filepath} -o {output_filepath} && {output_filepath}', content)

    # Add similar handle methods for other languages...
    def extract_class_name(self, content, keyword):
        match = re.search(rf'{keyword}\s+([A-Za-z_][A-Za-z0-9_]*)', content)
        return match.group(1) if match else None

    # def handle_java(self, content=None):
    #     self.run_command(f'javac {self.filepath} && java -cp {self.folder} {self.filename_noext}', content)

    # def handle_kotlin(self, content=None):
    #     self.run_command(f'kotlinc {self.filepath} -include-runtime -d {self.filename_noext}.jar && java -jar {self.filename_noext}.jar', content)
    def handle_java(self, content=None):
        class_name = self.extract_class_name(content, 'class')
        if class_name:
            self.filename_noext = class_name
            self.filename = f'{self.filename_noext}.java'
            self.filepath = os.path.join(self.folder, self.filename)
            self.run_command(f'javac {self.filepath} && java -cp {self.folder} {self.filename_noext}', content)

    def handle_kotlin(self, content=None):
        class_name = self.extract_class_name(content, 'class')
        if class_name:
            self.filename_noext = class_name
            self.filename = f'{self.filename_noext}.kt'
            self.filepath = os.path.join(self.folder, self.filename)
            self.run_command(f'kotlinc {self.filepath} -include-runtime -d {self.filename_noext}.jar && java -jar {self.filename_noext}.jar', content)

    def handle_csharp(self, content=None):
        self.run_command(f'csc {self.filepath} && mono {self.filename_noext}.exe', content)

    def handle_clojure(self, content=None):
        self.run_command(f'clojure {self.filepath}', content)

    def handle_javascript(self, content=None):
        self.run_command(f'node {self.filepath}', content)

    def handle_shell(self, content=None):
        self.run_command(f'bash {self.filepath}', content)

    def handle_haskell(self, content=None):
        output_filepath = f'{self.filename_noext}'
        self.run_command(f'ghc {self.filepath} -o {output_filepath} && ./{output_filepath}', content)

    # def handle_scala(self, content=None):
    #     self.run_command(f'scalac {self.filepath} && scala {self.filename_noext}', content)
    def handle_scala(self, content=None):
        class_name = self.extract_class_name(content, 'object')
        if class_name:
            self.filename_noext = class_name
            self.filename = f'{self.filename_noext}.scala'
            self.filepath = os.path.join(self.folder, self.filename)
            self.run_command(f'scalac {self.filepath} && scala -cp {self.folder} {self.filename_noext}', content)

    def run_command(self, command, content=None):
        if content:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        print(f"Running command: {command}")
        subprocess.run(command, shell=True, check=True)

# Usage example
executor = FileExecutor()

# Python example
executor.execute('py', 'print("Hello, Python World!")')

# C++ example
executor.execute('cpp', '#include <iostream>\nint main() { std::cout << "Hello, C++ World!"; return 0; }')

# Rust example
executor.execute('rs', 'fn main() { println!("Hello, Rust World!"); }')

# Java example
executor.execute('java', 'public class HelloWorld { public static void main(String[] args) { System.out.println("Hello, Java World!"); } }')

# Kotlin example
executor.execute('kt', 'fun main() { println("Hello, Kotlin World!") }')

# # C# example
# executor.execute('cs', 'using System; class Program { static void Main() { Console.WriteLine("Hello, C# World!"); } }')

# # Clojure example
# executor.execute('clj', '(println "Hello, Clojure World!")')

# JavaScript example
executor.execute('js', 'console.log("Hello, JavaScript World!")')

# # Shell example
# executor.execute('sh', 'echo "Hello, Shell World!"')

# # Haskell example
# executor.execute('hs', 'main = putStrLn "Hello, Haskell World!"')

# Scala example
executor.execute('scala', 'object HelloWorld extends App { println("Hello, Scala World!") }')
