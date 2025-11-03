# Definisi kelas Karyawan (Employee)
class Employee:
    def __init__(self, name, position):
        self.name = name              # Nama karyawan
        self.position = position      # Posisi karyawan dalam organisasi
        self.subordinates = []        # Daftar bawahan (subordinate)

    # Menambahkan bawahan (subordinate) ke karyawan
    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    # Menampilkan struktur organisasi secara rekursif
    def display_structure(self, level=0):
        indent = "   " * level  # Indentasi untuk merepresentasikan level hirarki
        print(f"{indent}- {self.name} ({self.position})")
        for subordinate in self.subordinates:
            subordinate.display_structure(level + 1)


# Fungsi untuk membangun struktur organisasi
def build_organization():
    # Membuat CEO
    ceo = Employee("Alice", "CEO")

    # Membuat VP (Wakil Presiden) untuk beberapa divisi
    vp_sales = Employee("Bob", "VP of Sales")
    vp_engineering = Employee("Charlie", "VP of Engineering")
    vp_hr = Employee("Diana", "VP of HR")

    # Menambah VP sebagai bawahan dari CEO
    ceo.add_subordinate(vp_sales)
    ceo.add_subordinate(vp_engineering)
    ceo.add_subordinate(vp_hr)

    # Membuat manajer (Manager) dan menambah mereka sebagai bawahan VP
    sales_manager = Employee("Eve", "Sales Manager")
    vp_sales.add_subordinate(sales_manager)

    engineering_manager_1 = Employee("Frank", "Engineering Manager 1")
    engineering_manager_2 = Employee("Grace", "Engineering Manager 2")
    vp_engineering.add_subordinate(engineering_manager_1)
    vp_engineering.add_subordinate(engineering_manager_2)

    hr_manager = Employee("Heidi", "HR Manager")
    vp_hr.add_subordinate(hr_manager)

    # Membuat beberapa karyawan dan menambah mereka sebagai bawahan manajer
    sales_rep_1 = Employee("Ivy", "Sales Representative")
    sales_rep_2 = Employee("Jack", "Sales Representative")
    sales_manager.add_subordinate(sales_rep_1)
    sales_manager.add_subordinate(sales_rep_2)

    engineer_1 = Employee("Kevin", "Engineer 1")
    engineer_2 = Employee("Lily", "Engineer 2")
    engineering_manager_1.add_subordinate(engineer_1)
    engineering_manager_2.add_subordinate(engineer_2)

    # Mengembalikan CEO sebagai root dari pohon organisasi
    return ceo


# Membuat struktur organisasi
org_root = build_organization()

# Menampilkan struktur organisasi
print("Struktur Organisasi:")
org_root.display_structure()
