from config import *

from detector.scan_detector import ScanDetector
from detector.alert_manager import AlertManager
from detector.report_generator import ReportGenerator
from detector.port_monitor import PortMonitor

detector = ScanDetector(
    THRESHOLD,
    TIME_WINDOW
)
port_monitor = PortMonitor(
    OPEN_PORT_REPORT
)

alerter = AlertManager(LOG_FILE)

reporter = ReportGenerator(
    REPORT_FILE
)

events = [
    ("192.168.1.50", 22),
    ("192.168.1.50", 80),
    ("192.168.1.50", 443),
    ("192.168.1.50", 8080),
    ("192.168.1.50", 3306),
    ("192.168.1.50", 5432)
]

for ip, port in events:

    if detector.process_event(
        ip,
        port
    ):

        alerter.alert(ip)

        reporter.add_report(ip)
print("\nScanning local ports...\n")

ports = port_monitor.scan_ports()

for port in ports:

    print(
        f"Port {port['port']} "
        f"({port['service']}) "
        f"is OPEN"
    )