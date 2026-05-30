import time

class ScanDetector:
    def __init__(self, threshold, time_window):
        self.threshold = threshold
        self.time_window = time_window
        self.tracker = {}

    def process_event(self, src_ip, dst_port):

        current_time = time.time()

        if src_ip not in self.tracker:
            self.tracker[src_ip] = []

        self.tracker[src_ip].append(
            (dst_port, current_time)
        )

        self.tracker[src_ip] = [
            (port, ts)
            for port, ts in self.tracker[src_ip]
            if current_time - ts <= self.time_window
        ]

        unique_ports = {
            port
            for port, ts in self.tracker[src_ip]
        }

        if len(unique_ports) > self.threshold:
            return True

        return False