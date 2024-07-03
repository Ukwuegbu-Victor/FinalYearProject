def input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        outpfn = lines[0].split()[0]
        xl = float(lines[1].split()[0])
        yl = float(lines[2].split()[0])
        nx = int(lines[3].split()[0])
        ny = int(lines[4].split()[0])
    return outpfn, xl, yl, nx, ny
