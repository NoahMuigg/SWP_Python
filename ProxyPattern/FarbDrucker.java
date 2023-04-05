public class FarbDrucker implements Drucker{
    @Override
    public void drucken(String Nachricht){
        System.out.println("Folgendes wird in Farbe gedruckt: " + Nachricht);
    } 
}
