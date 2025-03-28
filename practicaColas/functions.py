def add_queue(ticket, ticketControllers):
    controller = ticketControllers.get(ticket.attention_type)
    if controller:
        # Si el usuario no especificó prioridad y su edad es mayor a 60, se asigna prioridad.
        if not ticket.priority and ticket.age > 60:
            ticket.priority = True
        controller.add_ticket(ticket)