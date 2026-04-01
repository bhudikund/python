import sys


def get_mean_size(lines):
    total_size=0
    file_count=0


    for line in lines:
        columns=line.split()

        if len(columns) >= 9 and not columns[0].startswith('d'):
            size = int(columns[4])
            total_size += size
            file_count += 1


    return convert_bytes(total_size / file_count)

def convert_bytes(bytes):
    for type in ['B','KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0 or type == 'TB':
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {type}"

if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    if not lines:
        print("Нет файлов")
        exit()
    print(get_mean_size(lines))