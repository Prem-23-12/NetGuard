import socket
import json
import os

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}


class PortMonitor:

    def __init__(self, report_file):

        self.report_file = report_file

        os.makedirs(
            os.path.dirname(report_file),
            exist_ok=True
        )

    def scan_ports(self):

        open_ports = []

        for port, service in COMMON_PORTS.items():

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.5)

            result = sock.connect_ex(
                ("127.0.0.1", port)
            )

            if result == 0:

                open_ports.append(
                    {
                        "port": port,
                        "service": service,
                        "status": "Open"
                    }
                )

            sock.close()

        with open(
            self.report_file,
            "w"
        ) as file:

            json.dump(
                open_ports,
                file,
                indent=4
            )

        return open_ports