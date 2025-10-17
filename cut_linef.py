# SAMPLE

# PATH_ORGNS = r"C:\Users\User\Desktop\tmp\Organisations\orgns.txt"
# PATH_OUT = r"C:\Users\User\Desktop\tmp\Organisations"
# SIZE_CHUNK = 1000
# PREFIX_FILE = "orgns"

with open(PATH_ORGNS, 'r') as f:
    lines = f.readlines()
    j = 1
    for i in range(0, len(lines), SIZE_CHUNK):
        chunk = lines[i:i + SIZE_CHUNK]
        with open(f"{PATH_OUT}\\{PREFIX_FILE}_{j}.txt", 'w') as f:
            j += 1
            f.writelines(chunk)
