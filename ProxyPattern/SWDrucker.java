public class SWDrucker implements Drucker{
    @Override
    public void drucken(String Nachricht){
        System.out.println("Folgendes wird in Schwarz-Weiß gedruckt: " + Nachricht);
    } 
}
