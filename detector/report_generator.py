import json
import os
from datetime import datetime

class ReportGenerator:

    def __init__(self, report_file):

        self.report_file = report_file

        os.makedirs(
            os.path.dirname(report_file),
            exist_ok=True
        )

        if not os.path.exists(report_file):
            with open(report_file, "w") as file:
                json.dump([], file)

    def add_report(self, src_ip):

        with open(self.report_file, "r") as file:
            reports = json.load(file)

        reports.append(
            {
                "ip": src_ip,
                "timestamp": str(datetime.now())
            }
        )

        with open(self.report_file, "w") as file:
            json.dump(
                reports,
                file,
                indent=4
            )