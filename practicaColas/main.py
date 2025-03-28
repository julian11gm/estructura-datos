from typing import Union
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI(
    title="Sistema de Atención - Banco Miguelito",
    description="API para gestionar turnos y atención a clientes utilizando colas implementadas con nodos",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

@app.get("/ticketForm")
def ticket_form(request: Request):
    return templates.TemplateResponse("ticket_form.html", {"request": request})

@app.post("/ticketCreateForm")
def crear_turno_form(
    request: Request,
    name: str = Form(...),
    document: str = Form(...),
    attention_type: str = Form(...),
    age: int = Form(...),
    priority: bool = Form(False)
):
    ticket = Ticket(
        name=name,
        document=document,
        attention_type=attention_type,
        age=age,
        priority=priority
    )
    add_queue(ticket, ticketTypes)
    return templates.TemplateResponse("ticket_created.html", {"request": request, "ticket": ticket})

@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    controller = ticketTypes.get(tipo)
    if controller:
        next_turn = controller.next_ticket()
        return {"mensaje": "El siguiente turno es", "datos_turno": next_turn}
    return {"mensaje": "Tipo de atención no encontrado"}

@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    controller = ticketTypes.get(tipo)
    if controller:
        tickets = controller.list_tickets()
        return {"mensaje": "Lista de turnos en cola", "datos_turnos": tickets}
    return {"mensaje": "Tipo de atención no encontrado"}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
