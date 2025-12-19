import time
import sys
import os
from colorama import Fore, Style, init

init(autoreset=True)

# Fungsi untuk menampilkan teks perlahan seperti mesin tik
def type_text(text, color=Fore.LIGHTMAGENTA_EX, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Fungsi animasi loading bar
def loading_bar(text="Processing", length=25, color=Fore.MAGENTA):
    sys.stdout.write(color + text + " [")
    for i in range(length):
        sys.stdout.write("█")
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write("] Done!\n\n")

# Kelas Waifu
class Waifu:
    def __init__(self, name):
        self.name = name

# Fungsi utama
def wish(waifu):
    os.system("cls" if os.name == "nt" else "clear")

    type_text(">>> Initializing birthday protocol...", Fore.LIGHTCYAN_EX)
    time.sleep(0.8)
    loading_bar("Loading magical data")

    type_text(f">>> Target identified: {waifu.name}", Fore.LIGHTMAGENTA_EX)
    time.sleep(0.6)
    type_text(">>> Channeling mana into message stream...", Fore.CYAN)
    loading_bar("Compiling message", 20)

    # Pesan utama
    type_text("🎂✨ SYSTEM MESSAGE ✨🎂", Fore.LIGHTWHITE_EX, 0.06)
    time.sleep(0.5)
    type_text(f"Happy Birthday, {waifu.name}! 💜", Fore.MAGENTA, 0.08)
    time.sleep(0.5)
    type_text("May your journey be filled with magic, kindness, and adventure.", Fore.LIGHTWHITE_EX, 0.05)
    time.sleep(1)
    type_text("From a programmer who believes in your story and your smile. 💻🪄", Fore.LIGHTCYAN_EX, 0.05)

    time.sleep(1.2)
    print()
    type_text(">>> Mission complete. The world feels lighter today... ☁️", Fore.LIGHTBLACK_EX, 0.05)
    type_text(f"💜 Happy Birthday once again, {waifu.name}.", Fore.LIGHTMAGENTA_EX, 0.06)
    type_text("return 0;", Fore.LIGHTBLACK_EX, 0.06)

if __name__ == "__main__":
    elaina = Waifu("Elaina")
    wish(elaina)
