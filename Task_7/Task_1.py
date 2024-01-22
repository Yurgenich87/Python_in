import os

def rename_files(desired_name="", num_digits=3, source_ext="", target_ext="", name_range=None):
    if not os.path.exists("test_folder"):
        print("Папка 'test_folder' не найдена.")
        return

    files = [f for f in os.listdir("test_folder") if
             os.path.isfile(os.path.join("test_folder", f)) and f.endswith(f".{source_ext}")]

    if not files:
        print("")
        return

    for i, file in enumerate(sorted(files)):
        original_name = file.split(".")[0]
        original_name_part = original_name[name_range[0] - 1:name_range[1]] if name_range else original_name
        new_name = f"{desired_name}{i + 1:0{num_digits}d}.{target_ext}"
        os.rename(os.path.join("test_folder", file), os.path.join("test_folder", new_name))


# Пример использования
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", name_range=[3, 6])
