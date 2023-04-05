public class main {
    public static void main(String[] args) {
        ProxyDrucker druckerProxy = new ProxyDrucker();

        druckerProxy.drucken("Hallo");
        druckerProxy.switchToSW();
        druckerProxy.drucken("Mein Name ist");
        druckerProxy.switchToFarbe();
        druckerProxy.drucken("Noah");
        
    }
}
