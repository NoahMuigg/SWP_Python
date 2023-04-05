public class main {
    public static void main(String[] args) {
        Zentrale z1 = new Zentrale();
        Observer o1 = new Observer1();

        z1.addObserver(o1);

        z1.setNeueWetterdaten(new Wetterdaten(15, 20, 5, Jahreszeiten.Frühling));
        
    }
}
