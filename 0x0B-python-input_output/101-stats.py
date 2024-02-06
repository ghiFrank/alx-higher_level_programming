import sys

def print_metrics(metrics):
    total_file_size = metrics['total_file_size']
    status_codes = sorted(metrics['status_codes'].items())
    
    print(f"Total file size: {total_file_size}")
    for code, count in status_codes:
        print(f"{code}: {count}")

def process_line(line, metrics):
    parts = line.split()
    if len(parts) < 9:
        return
    
    try:
        status_code = int(parts[8])
        file_size = int(parts[9])
        metrics['total_file_size'] += file_size
        metrics['status_codes'][status_code] = metrics['status_codes'].get(status_code, 0) + 1
    except ValueError:
        pass

def main():
    metrics = {'total_file_size': 0, 'status_codes': {}}
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        process_line(line, metrics)
        line_count += 1
        
        if line_count % 10 == 0:
            print_metrics(metrics)

if __name__ == "__main__":
    main()
