from rich.live import Live
from rich.table import Table
import psutil
import time

def generate_table():
    table = Table(title="Infrastructure Dashboard")

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row("CPU Usage", f"{psutil.cpu_percent()} %")
    table.add_row("Memory Usage", f"{psutil.virtual_memory().percent} %")
    table.add_row("Disk Usage", f"{psutil.disk_usage('/').percent} %")

    return table

with Live(generate_table(), refresh_per_second=1) as live:
    while True:
        live.update(generate_table())
        time.sleep(1)
