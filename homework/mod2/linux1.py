import os

BASE_DIR= os.path.dirname(os.path.abspath(__file__))
FILE_PATH= os.path.join(BASE_DIR,'output_file.txt')

def get_summary_rss(FILE_PATH):
    rss = 0

    try:
        with open(FILE_PATH) as output_file:
            lines = output_file.readlines()[1:]

            for line in lines:
                columns = line.split()

                if len(columns) >= 6:
                    rss_value = int(columns[5])
                    rss += rss_value
                    return convert_bytes(rss)
    except FileNotFoundError:
        return None

def convert_bytes(bytes):
    for type in ['B','KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0 or type == 'TB':
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {type}"

if __name__ == "__main__":
    result = get_summary_rss(FILE_PATH)
    print(result)