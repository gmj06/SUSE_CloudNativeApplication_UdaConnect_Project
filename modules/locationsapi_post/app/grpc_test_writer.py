import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel('localhost:5005', options=(('grpc.enable_http_proxy', 0),))

#channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    person_id=2,
    longitude="37.55363",
    latitude="-122.290883"
)


response = stub.Create(location)
