public class main {
    public static void main(String[] args) {
        Kassa kassa1 = new Kassa();

        Ticket t1 = new Ticket(20);
        Ticket t2 = new Ticket(50);

        kassa1.addTicket(t2);
        kassa1.addTicket(t1);

        kassa1.ticket(new ErwachsenenTicketStrategy(0.2));

    }

}
