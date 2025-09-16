from src.core.rpc import RPCWorker

class APIService:
    def __init__(self, worker: RPCWorker):
        self.worker = worker
