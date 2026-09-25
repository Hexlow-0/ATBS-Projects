
from pathlib import Path
from datetime import datetime


path = Path("C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2508.4.0_x64__8wekyb3d8bbwe\CalculatorApp.exe")

print("=" * 40)
print("FILE INSPECTOR".center(40))
print("=" * 40)
print()

col1 = 12

modified = datetime.fromtimestamp(path.stat().st_mtime)
created = datetime.fromtimestamp(path.stat().st_ctime)
accessed = datetime.fromtimestamp(path.stat().st_atime)

print(f"File:".ljust(col1) + f"{path.name}")
print(f"Size:".ljust(col1) + f"{path.stat().st_size:,} bytes")
print(f"".ljust(col1) + f"{path.stat().st_size / 1024:.2f} KB")
print(f"".ljust(col1) + f"{path.stat().st_size / (1024 * 1024):.4f} MB\n")
print(f"Modified:".ljust(col1) + f"{modified.strftime('%d %B %Y, %H:%M')}")
print(f"Created:".ljust(col1) + f"{created.strftime('%d %B %Y, %H:%M')}")
print(f"Accessed:".ljust(col1) + f"{accessed.strftime('%d %B %Y, %H:%M')}\n")

print("=" * 40)
