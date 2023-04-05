public class ProxyDrucker implements Drucker{
    private Drucker drucker;

    public ProxyDrucker(){
        drucker = new FarbDrucker();
    }

    public void switchToSW(){
        drucker = new SWDrucker();
    }

    public void switchToFarbe(){
        drucker = new FarbDrucker();
    }

    public void drucken(String Nachricht){
        drucker.drucken(Nachricht);
    }
}
