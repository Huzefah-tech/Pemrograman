def sort_branches_by_sales(data):
    # Merungurutkan data bedasarkan penjualan secara descending
    sorted_data = sorted(data.items(), key=lambda x: x[1][1], reverse=True)
    return sorted_data
    
def find_highest_lowest_sales(data):
    # Cabang dengan penjualan tertinggi dan terendah
    highest = max(data.items(), key=lambda x: x[1][1])
    lowest = min(data.items(), key=lambda x: x[1][1])
    return highest, lowest

def generate_report(data):
    total_sales = sum([info[1] for info in data.values()])
    avg_sales = total_sales / len(data)
    highest, lowest = find_highest_lowest_sales(data)
    contribution_highest = (highest[1][1] / total_sales) * 100
    print("----- Laporan Penjualan cabang -----")
    print(f"Total Penjualan: {total_sales}")
    print(f"Rata-rata Penjualan: {avg_sales:.2f}\n")
    print("Daftar Cabang Berdasarkan Penjualan (Descending):")
    sorted_data = sort_branches_by_sales(data)
    for cabang, info in sorted_data:
        print(f"{info[0]} (ID: {cabang}): penjualan {info[1]}")
    print("\n----- Rekomendasi -----")
    if avg_sales < 4500:
         print("Rata-rata penjualan masih rendah. Perlu strategi peningkatan penjualan.")
    else:
        print("Penjualan rata-rata sudah baik. Pertahankan dan tingkatkan cabang dengan penjualan rendah.")
    print(f"Cabang dengan penjualan tertinggi: Cabang {highest[1][0]} (ID: {highest[0]}) dengan penjualan {highest[1][1]}, kontribusi terhadap total penjualan: {contribution_highest:.2f}%")
    print(f"Cabang dengan penjualan terendah: Cabang {lowest[1][0]} (ID: {lowest[0]}) dengan penjualan {lowest[1][1]}.")

if __name__ == "__main__":
    # Data penjualan cabang dalam format {ID Cabang: [Nama Cabang, Penjualan]}
    sales_data = {
        "C001": ["Cabang A", 5000],
        "C002": ["Cabang B", 3000],
        "C003": ["Cabang C", 7000],
        "C004": ["Cabang D", 2000],
        "C005": ["Cabang E", 4000],
    }
    generate_report(sales_data)