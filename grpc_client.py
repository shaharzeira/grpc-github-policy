import argparse
import grpc
import pb.access_pb2 as access_pb2
import pb.access_pb2_grpc as access_pb2_grpc

def main(username: str):
    # Set up gRPC channel and stub
    channel = grpc.insecure_channel("localhost:50051")
    stub = access_pb2_grpc.AccessCheckerStub(channel)

    # Make the request
    request = access_pb2.UserRequest(username=username)
    response = stub.GetAccessibleRepos(request)

    # Display results
    if response.repositories:
        print(f"✅ User '{username}' has access to:")
        for repo in response.repositories:
            print(f"  - {repo}")
    else:
        print(f"❌ User '{username}' has no access to any repositories.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check repo access via gRPC.")
    parser.add_argument("username", help="GitHub username to check")
    args = parser.parse_args()

    main(args.username)
