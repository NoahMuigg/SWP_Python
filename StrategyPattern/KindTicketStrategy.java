public class KindTicketStrategy implements TicketStrategy{
    private double steuersatz;

    public KindTicketStrategy(double st){
        this.steuersatz = st;
    }
   
    @Override
    public void ticketPreis(double grundpreis){
        double preis = grundpreis * (1+steuersatz);
        System.out.println("Ein Kinderticket kostet:" + preis);
    }
}
