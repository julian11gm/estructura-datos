from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    document: str
    attention_type: str
    age: int
    priority: bool = False