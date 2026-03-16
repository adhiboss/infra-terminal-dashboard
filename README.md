# Infra Terminal Dashboard

Infra Terminal Dashboard is a real-time infrastructure monitoring interface that runs entirely inside the terminal. It visualizes key system metrics and provides a minimal dashboard for observing system behavior.

The project was built to explore how monitoring tools work under the hood and how system metrics can be visualized in a terminal environment.

## Features

- Real-time CPU usage monitoring
- Memory utilization tracking
- Disk usage visualization
- Live updating terminal dashboard
- Minimal and readable terminal interface

The dashboard updates continuously, allowing users to observe system performance as it changes.

## Why This Project Exists

Modern infrastructure relies heavily on observability and monitoring. Engineers constantly inspect system metrics to detect performance issues, resource exhaustion, or abnormal behavior.

This project is an experiment in building a simple monitoring interface that runs directly in the terminal without requiring a full graphical interface.

## Example Dashboard
Infrastructure Dashboard

CPU Usage 12%
Memory Usage 35%
Disk Usage 48%


The dashboard updates every second to reflect current system conditions.

## Technologies Used

- Python
- psutil (system metrics)
- rich (terminal UI rendering)

## Run the Dashboard
python dashboard.py


## Learning Goals

This project explores:

- terminal user interface design
- system monitoring concepts
- infrastructure observability
- Python-based system tools
