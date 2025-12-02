class InMemoryDB:
    def __init__(self):
        self.main_state = {}
        self.transaction_state = None  
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Transaction already in progress")
        self.transaction_state = {}
        self.in_transaction = True

    def put(self, key: str, value: int):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.transaction_state[key] = value

    def get(self, key: str):
        return self.main_state.get(key, None)

    def commit(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        for k, v in self.transaction_state.items():
            self.main_state[k] = v
        self.transaction_state = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress")
        self.transaction_state = None
        self.in_transaction = False
