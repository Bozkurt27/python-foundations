from pathlib import Path

data_folder = Path("data")
print(data_folder)
print(type(data_folder))

file_path = Path("data") / "sales.txt"

print(file_path)


current_folder = Path.cwd()
print(current_folder)


file = open("data/study_notes.txt", "r", encoding = "utf-8")
content = file.read()
print(content)
file.close()



with open("data/study_notes.txt", "r", encoding = "utf-8") as file:
    for line in file:
        print(line.strip())

output_path = Path("data") / "result.txt"
with open(output_path, "w", encoding = "utf-8") as file:
    file.write("İlk dosyam")

with open(output_path, "a", encoding = "utf-8") as file:
    file.write("\nikinci satır")


file_path = Path("data") / "study_notes.txt"
print(file_path.exists())


    