#Definisi kelas karyawan
class Employee:
  def __init__(self, emp_id, name, position, salary):
    self.emp_id = emp_id          # ID Karyawan unik
    self.name = name              # Nama karyawan
    self.position = position      # Posisi karyawan
    self.salary = salary          # Gaji karyawan
    self.tasks = []               # Tugas yang di-assign ke karyawan

  # Menambah tugas ke karyawan
  def assign_task(self, task):
    self.tasks.append(task)

  # Menampilkan informasi karyawan
  def display_info(self):
    print(f"Karyawan ID: {self.emp_id}, Nama: {self.name}, Posisi: {self.position}, Gaji: {self.salary}")
    print("Tugas:")
    for task in self.tasks:
      print(f" - {task.title} (Deadline: {task.deadline}) ")

# Definisi kelas Tugas
class Task:
  def __init__(self, task_id, title, description, deadline):
    self.task_id = task_id              # ID tugask unik
    self.title = title                  # Judul tugas
    self.description = description      # Deskripsi tugas
    self.deadline = deadline            # Deadline tugas

  # Menampilkan detail tugas
  def display_task(self):
    print(f"Tugas ID: {self.task_id}, Judul: {self.title}, Deskripsi: {self.description}, Deadline: {self.deadline}")

# Definisi kelas Proyek
class Project:
  def __init__(self, project_id, name, description, start_date, end_date):
    self.project_id = project_id          # ID proyek unik
    self.name = name                      # Nama proyek
    self.description = description        # Deskripsi proyek
    self.start_date = start_date          # Tanggal mulai proyek
    self.end_date = end_date              # Tanggal akhir proyek
    self.team = []                        # Tim yang menangani proyek
    self.tasks = []                       # Tugas yang ada di dalam proyek

  # manambah karyawab ke proyek
  def add_employee(self, employee):
    self.team.append(employee)

  # Menambah tugas ke proyek
  def add_task(self, task):
    self.tasks.append(task)

  # Menampilkan detail proyek
  def display_project(self):
    print(f"Proyek ID: {self.project_id}, Nama: {self.name}")
    print(f"Deskripsi: {self.description}")
    print(f"Durasi: {self.start_date} hingga {self.end_date}")
    print("Tim Proyek:")
    for member in self.team:
      print(f" - {member.name} ({member.position})")
    print("Tugas Proyek:")
    for task in self.tasks:
      print(f"  - {task.title} (Deadline: {task.deadline})")

# Definisi kelas Sistem Manajemen
class BusinessManagementSystem:
  def __init__(self):
    self.employees = {}            # Data karyawan (key: emp_id)
    self.projects = {}            # Data proyek (key: project_id)
    self.tasks = {}               # Data tugas (key: task_id)

  # Menambah karyawan
  def add_employee(self, emp_id, name, position, salary):
    employee = Employee(emp_id, name, position, salary)
    self.employees[emp_id] = employee
    print(f"Karyawan {name} telah ditambahkan.")

  # Menambah proyek
  def add_project(self, project_id, name, description, start_date, end_date):
    project = Project(project_id, name, description, start_date, end_date)
    self.projects[project_id] = project
    print(f"Proyek {name} telah ditambahkan.")

  # Menambah tugas ke proyek dan karyawan
  def add_task(self, task_id, title, description, deadline, project_id, emp_id):
    task = Task(task_id, title, description, deadline)
    self.tasks[task_id] = task
    # Assign tugas ke proyek
    if project_id in self.projects:
      self.projects[project_id].add_task(task)
    
    # Assign tugas ke karyawan
    if emp_id in self.employees:
      self.employees[emp_id].assign_task(task)
      print(f"Tugas {title} telah ditambahkan dan di-assign ke karyawan serta proyek.")

  # Menampilkan laporan kinerja karyawan
  def display_employee_report(self, emp_id):
    if emp_id in self.employees:
      employee = self.employees[emp_id]
      employee.display_info()
    else:
      print(f"Karyawan dengan ID {emp_id} tidak ditemukan.")

  # Menammpilkan detail proyek
  def display_project_report(self, project_id):
    if project_id in self.projects:
      project = self.projects[project_id]
      project.display_project()
    else:
      print(f"Proyek dengan Id {project_id} tidak ditemukan.")

# Inisialisasi sitem
bms = BusinessManagementSystem()

# Menambah beberapa karyawan
bms.add_employee(1, "Alice", "Manager", 5000)
bms.add_employee(2, "Bob", "Developer", 4000)
bms.add_employee(3, "Charlie", "Tester", 3500)

#Menambah proyek
bms.add_project(101, "Proyek A", "Pengembangan aplikasi web", "2024-01-01", "2024-12-31")

# Menambah tugas dan mengassign ke proyek dan karyawan
bms.add_task(1001, "Desain UI", "Membuat desain antarmuka pengguna", "2024-03-01", 101, 2)
bms.add_task(1002, "Pengujian Fungsional", "Melakukan pengujian fungsional pada modul", "2024-05-01", 101, 3)

# Menampilkan laporan karyawan
print("\nLaporan Karyawan:")
bms.display_employee_report(2)

# Menampilkan laporan proyek
print("\nLaporan Proyek:")
bms.display_project_report(101)