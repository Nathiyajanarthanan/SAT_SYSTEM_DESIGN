
class EmergencyRequest:
    def __init__(self, request_id, user_id, latitude, longitude):
        self.request_id = request_id
        self.user_id = user_id
        self.latitude = latitude
        self.longitude = longitude
        self.ambulance_id = 201
        self.status = "ASSIGNED"


class AmbulanceDispatch:
    def __init__(self):
        self.requests = {}

    def request_ambulance(self, user_id, lat, lon):
        request_id = len(self.requests) + 501
        request = EmergencyRequest(request_id, user_id, lat, lon)
        self.requests[request_id] = request

        print("Request ID:", request.request_id)
        print("Ambulance ID:", request.ambulance_id)
        print("Status:", request.status)

    def get_ambulance_details(self, ambulance_id):
        print("Ambulance ID:", ambulance_id)
        print("Status: Assigned")

    def get_ambulance_location(self, ambulance_id):
        print("Ambulance ID:", ambulance_id)
        print("Latitude: 11.0168, Longitude: 76.9558")

    def get_emergency_status(self, request_id):
        request = self.requests.get(request_id)
        print(request.status if request else "Request Not Found")

    def cancel_request(self, request_id):
        request = self.requests.get(request_id)
        if request:
            request.status = "CANCELLED"
            print("Request cancelled successfully")
        else:
            print("Request not found")


if __name__ == "__main__":
    system = AmbulanceDispatch()

    system.request_ambulance(101, 11.0168, 76.9558)
    system.get_ambulance_details(201)
    system.get_ambulance_location(201)
    system.get_emergency_status(501)
    system.cancel_request(501)
