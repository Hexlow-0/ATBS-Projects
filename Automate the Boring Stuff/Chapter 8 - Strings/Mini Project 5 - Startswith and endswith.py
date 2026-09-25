
files = [
    "report_2026.pdf",
    "image_01.png",
    "report_2024.docx",
    "notes.txt",
    "image_02.jpg",
    "budget_2026.xlsx",
    "report_2025.pdf",
    "temp_notes.txt",
    "image_03.png",
    "archive.zip"
]



reports = [file for file in files if file.startswith('report_')]
images = [file for file in files if file.startswith('image_')]
specific_ext = [file for file in files if file.endswith(('.pdf', '.docx', '.txt'))]

others = []

for file in files:
    if file.startswith('report_'):
        pass
    elif file.startswith('image_'):
        pass
    elif file.endswith(('.pdf', '.docx', '.txt')):
        pass
    else:
        others.append(file)

print(reports)
print(images)
print(specific_ext)
print(others)
