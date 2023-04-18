public class SeniorenTicketStrategy implements TicketStrategy{
    public double steuersatz;

    public SeniorenTicketStrategy(double st){
        this.steuersatz = st;
    }

    @Override
    public void ticketPreis(double grundpreis){
        double preis = grundpreis * (1+steuersatz);
        System.out.println("Ein Seniorenticket kostet:" + preis);
    }
}
