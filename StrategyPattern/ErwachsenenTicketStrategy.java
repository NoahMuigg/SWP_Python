public class ErwachsenenTicketStrategy implements TicketStrategy{
    private double steuersatz;

    public ErwachsenenTicketStrategy(double st){
        this.steuersatz = st;
    }

    @Override
    public void ticketPreis(double grundpreis){
        double preis = grundpreis * (1+steuersatz);
        System.out.println("Ein Erwachsenesticket kostet:" + preis);
    }
}
