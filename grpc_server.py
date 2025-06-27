import grpc
from concurrent import futures
import access_pb2, access_pb2_grpc

from repo_info import build_opa_repo_access_inputs
from accessible_repos import get_user_accessible_repos

from config import ORG_NAME

class AccessCheckerServicer(access_pb2_grpc.AccessCheckerServicer):
    def GetAccessibleRepos(self, request, context):
        username = request.username
        opa_inputs = build_opa_repo_access_inputs(str(ORG_NAME))
        repos = get_user_accessible_repos(username, opa_inputs)
        return access_pb2.RepoList(repositories=repos)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    access_pb2_grpc.add_AccessCheckerServicer_to_server(AccessCheckerServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
