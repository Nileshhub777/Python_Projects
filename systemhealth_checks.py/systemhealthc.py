import psutil
import shutil
import logging
import datetime

# Setup logging
logging.basicConfig(filename="system_health.log", level=logging.INFO)

def check_cpu(threshold=80):
    usage = psutil.cpu_percent(interval=1)
    if usage > threshold:
        alert(f"High CPU usage: {usage}%")
    return usage

def check_memory(threshold=80):
    mem = psutil.virtual_memory()
    if mem.percent > threshold:
        alert(f"High Memory usage: {mem.percent}%")
    return mem.percent

def check_disk(threshold=80):
    total, used, free = shutil.disk_usage("/")
    usage = used / total * 100
    if usage > threshold:
        alert(f"High Disk usage: {usage:.2f}%")
    return usage

def alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.warning(f"{timestamp} - ALERT: {message}")
    print(f"[ALERT] {message}")

def main():
    print("Running health checks...")
    cpu = check_cpu()
    mem = check_memory()
    disk = check_disk()
    print(f"CPU Usage: {cpu}% | Memory Usage: {mem}% | Disk Usage: {disk:.2f}%")

if __name__ == "__main__":
    main()
