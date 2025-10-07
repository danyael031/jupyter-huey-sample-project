import os
import zipfile

def zip_folders(folder_paths, output_zip):

    os.makedirs(os.path.dirname(output_zip), exist_ok=True)
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folder_paths:
            folder = os.path.abspath(folder)
            if not os.path.isdir(folder):
                continue

            for root, _, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(folder))
                    zipf.write(file_path, arcname)

