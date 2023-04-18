import java.util.ArrayList;
import java.util.List;

public class Kassa {
    List<Ticket> tickets;

    public Kassa(){
        this.tickets = new ArrayList<>();
    }

    public void addTicket(Ticket ticket){
        this.tickets.add(ticket);
    }

    public void removeTicket(Ticket ticket){
        this.tickets.remove(ticket);
    }

    public double zahlen(){
        double gesamt = 0;
        for(Ticket ticket : tickets){
            gesamt += ticket.getZuZahlen();
        }
        return gesamt;
    }

    public void ticket(TicketStrategy ticketStrategy){
        double preis = zahlen();
        ticketStrategy.ticketPreis(preis);
    }
}
