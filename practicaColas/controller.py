from queue_module import Queue

class TicketController:
    def __init__(self):
        self.queue = Queue()
    
    def add_ticket(self, ticket):
        self.queue.enqueue(ticket)
    
    def next_ticket(self):
        return self.queue.dequeue()
    
    def list_tickets(self):
        return self.queue.list_all()