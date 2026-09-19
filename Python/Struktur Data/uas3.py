def sort_branches_by_sales(data):
    return sorted(data.items(), key=lambda x: x[1][1], reverse=True)


def find_highest_lowest_sales(data):
    highest = max(data.items(), key=lambda x: x[1][1])
    lowest = min(data.items(), key=lambda x: x[1][1])
    return highest, lowest


def generate_report(data):
    total_sales = sum(info[1] for info in data.values())
    avg_sales = total_sales / len(data)

    highest, lowest = find_highest_lowest_sales(data)
    contribution_highest = (highest[1][1] / total_sales) * 100

    print("----- Laporan Penjualan Cabang -----")
    print(f"Total Penjualan: {total_sales}")
    print(f"Rata-rata Penjualan: {avg_sales:.2f}\n")

    print("Daftar Cabang Berdasarkan Penjualan (Descending):")
    sorted_data = sort_branches_by_sales(data)
    for cabang, info in sorted_data:
        print(f"Cabang {info[0]} (ID: {cabang}) : Penjualan {info[1]}")

    print("\n----- Rekomendasi -----")
    if avg_sales < 4500:
        print("Rata-rata penjualan masih rendah.")
        print("Rekomendasi: Tingkatkan promosi dan evaluasi cabang.")
    else:
        print("Rata-rata penjualan sudah baik.")
        print("Rekomendasi: Pertahankan dan tingkatkan cabang unggulan.")

    print("\nCabang Penjualan Tertinggi:")
    print(f"{highest[0]} ({highest[1][0]}): {highest[1][1]}")

    print("Cabang Penjualan Terendah:")
    print(f"{lowest[0]} ({lowest[1][0]}): {lowest[1][1]}")

    print(f"\nKontribusi Cabang Tertinggi: {contribution_highest:.2f}%")


# ===== PROGRAM UTAMA =====
data_penjualan = {
    "C01": ["Jakarta", 5000],
    "C02": ["Bandung", 4200],
    "C03": ["Surabaya", 6100],
    "C04": ["Medan", 3800],
    "C05": ["Padang", 3500],
    "C06": ["Makassar", 3700],
    "C07": ["Semarang", 3600],
    "C08": ["Aceh", 3200],
    "C09": ["Kupang", 2900],
    "C10": ["Palangkaraya", 3300],
}

generate_report(data_penjualan)