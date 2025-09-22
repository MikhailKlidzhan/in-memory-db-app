from collections import defaultdict


class InMemoryDB:
    """Main class to represent DB logic"""
    def __init__(self):
        self.db = {}
        self.counts = defaultdict(int)
        self.transaction_stack = []

    def set_cmd(self, key, value):
        old_value = self.db.get(key)

        if old_value is not None:
            self.counts[old_value] -= 1

        self.db[key] = value
        self.counts[value] += 1

        if self.transaction_stack:
            self.transaction_stack[-1][key] = old_value

    def get_cmd(self, key):
        return self.db.get(key, "NULL")
    
    def unset_cmd(self, key):
        if key in self.db:
            value = self.db[key]
            del self.db[key]
            
            self.counts[value] -= 1

            if self.transaction_stack:
                self.transaction_stack[-1][key] = value

    def counts_cmd(self, value):
        return self.counts.get(value, 0)
    
    def find_cmd(self, value):
        return [k for k, v in self.db.items() if v == value]
    
    # transaction methods
    def begin(self):
        return self.transaction_stack.append({})
    
    def rollback(self):
        if not self.transaction_stack:
            return "NO TRANSACTION"
        
        transaction = self.transaction_stack.pop()

        for key, old_value in transaction.items():
            current_value = self.db.get(key)  
            if current_value is not None:
                self.counts[current_value] -= 1
            if old_value is not None:
                self.db[key] = old_value
                self.counts[old_value] += 1
            else:
                if key in self.db:
                    del self.db[key]
        
        return None
    
    def commit(self):
        if not self.transaction_stack:
            return "NO TRANSACTION"
        
        current_transaction = self.transaction_stack.pop()

        if self.transaction_stack:
            parent_transaction = self.transaction_stack[-1]
            for key, old_value in current_transaction.items():
                if key not in parent_transaction:
                    parent_transaction[key] = old_value

        return None





