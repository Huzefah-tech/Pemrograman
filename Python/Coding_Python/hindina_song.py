import time
import sys

def jalanin_lirik():
    lirik = [
        ("Hindi na ", 0.055),
        ("Ma,", 0.06),
        ("Kalaya,", 0.13),
        ("Dina da law mo", 0.1)
    ]

    for kata, jeda in lirik:
        for huruf in kata:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(jeda)
        sys.stdout.write(" ")

    print("\nSelesai!")

jalanin_lirik()
