public class Ticket {
    private double grundpreis;

    public Ticket(double gp){
        this.grundpreis = gp;
    }

    public double getZuZahlen(){
        return grundpreis;
    }
}
