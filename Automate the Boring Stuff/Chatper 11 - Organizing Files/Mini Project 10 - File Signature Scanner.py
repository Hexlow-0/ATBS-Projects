
from pathlib import Path

base = Path.home() / "Documents" / "python_sandbox" / "test"

SIGNATURES = {
    b'\x89PNG\r\n\x1a\n': 'PNG image',
    b'\xff\xd8\xff'      : 'JPEG image',
    b'PK\x03\x04'        : 'ZIP file (or .docx/.xlsx/.jar)',
    b'%PDF'              : 'PDF document',
    b'MZ'                : 'Windows executable',
    b'\x7fELF'           : 'Linux executable',
    b'GIF87a'            : 'GIF image',
    b'GIF89a'            : 'GIF image',
    b'\x1f\x8b'          : 'GZIP archive',
    b'BM'                : 'BMP image',
}

def collect_data(file):

    with open(file, 'rb') as f:
        header = f.read(8)

        for sig, file_type in SIGNATURES.items():
            if header.startswith(sig):
                return {'ok': True,
                        'data': {'file_name': file.name[:11], 'ext': file.suffix.replace('.', ''), 'file_type': file_type}
                        }

        return {'ok': False,
        'data': {'file_name': file.name[:11], 'ext': file.suffix.replace('.', ''), 'file_type': 'Unknown'}
        }

def write_report(errors, processed):

    with open('File_Sig_Report.txt', 'w', encoding='utf-8') as f:

        print("  FINDINGS  ".center(40, '='), file=f)
        print(file=f)

        for item in processed:

            name = item.get('data', {}).get('file_name', 'unknown')
            ext = item.get('data', {}).get('ext', 'unknown')
            header = item.get('data', {}).get('file_type', 'unknown')

            print(f"{name:<13} | {ext:<5} | {header}", file=f)

        print(file=f)
        print("  ERRORS  ".center(40, '='), file=f)
        print(file=f)

        for item in errors:

            name = item.get('data', {}).get('file_name', 'unknown')
            ext = item.get('data', {}).get('ext', 'unknown')
            header = item.get('data', {}).get('file_type', 'unknown')

            print(f"{name:<13} | {ext:<5} | {header}", file=f)

def main():

    errors = []
    processed = []

    print("Collecting data...")

    for file in base.rglob('*'):
        if file.is_file():
            results = collect_data(file)

            if not results['ok']:
                errors.append(results)
                continue

            processed.append(results)

    print("Finished! Writing report...")

    write_report(errors, processed)

main()
