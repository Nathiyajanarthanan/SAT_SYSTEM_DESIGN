
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class EmergencyService:
    def __init__(self):
        self.requests = {}
        self.locations = {}
        self.lock = Lock()
        self.executor = ThreadPoolExecutor(max_workers=10)

    def request_ambulance(self, request_id):
        self.executor.submit(self._assign_ambulance, request_id)

    def _assign_ambulance(self, request_id):
        with self.lock:
            self.requests[request_id] = "AMBULANCE_ASSIGNED"
        print("Ambulance assigned to request", request_id)

    def update_location(self, ambulance_id, location):
        with self.lock:
            self.locations[ambulance_id] = location

    def get_status(self, request_id):
        with self.lock:
            return self.requests.get(request_id, "NOT_FOUND")

    def get_location(self, ambulance_id):
        with self.lock:
            return self.locations.get(
                ambulance_id, "LOCATION_UNAVAILABLE"
            )

    def shutdown(self):
        self.executor.shutdown(wait=True)


if __name__ == "__main__":
    service = EmergencyService()

    service.update_location(201, "11.0168, 76.9558")
    service.request_ambulance(501)

    service.shutdown()

    print("Status:", service.get_status(501))
    print("Location:", service.get_location(201))
