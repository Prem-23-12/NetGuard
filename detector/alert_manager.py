from datetime import datetime
import os

class AlertManager:

    def __init__(self, log_file):

        self.log_file = log_file

        os.makedirs(
            os.path.dirname(log_file),
            exist_ok=True
        )

    def alert(self, src_ip):

        message = (
            f"{datetime.now()} | "
            f"Possible Port Scan Detected "
            f"from {src_ip}"
        )

        print(message)

        with open(self.log_file, "a") as file:
            file.write(message + "\n")