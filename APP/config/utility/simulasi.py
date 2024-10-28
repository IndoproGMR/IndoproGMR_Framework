import time
import concurrent.futures
from math import factorial
import sys

sys.set_int_max_str_digits(10**6)


# Simulasi tugas berat (misalnya perhitungan besar)
def heavy_computation(n: int):
    print(f"Memulai proses berat untuk {n}")
    start_time = time.time()
    result = factorial(n)  # Mensimulasikan proses berat dengan menghitung faktorial
    end_time = time.time()
    print(f"Proses selesai untuk {n} dalam {end_time - start_time} detik")
    return result


# Fungsi utama untuk menjalankan simulasi
def start_heavy_process():
    # Gunakan ThreadPoolExecutor agar proses berat tidak memblokir event loop utama
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Menjalankan beberapa tugas berat secara bersamaan
        futures = [
            executor.submit(heavy_computation, n) for n in [600_000, 700_000, 800_000]
        ]

        # Mengambil hasil dari tugas-tugas tersebut
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()  # Ambil hasil perhitungan

                # print(f"Hasil: {result}")
            except Exception as e:
                print(f"Error dalam proses: {e}")
