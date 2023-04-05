public class Observer1 implements Observer {
    
    @Override
    public void update(Wetterdaten w){
        System.out.println("Es werden folgende Daten an den Observer1 gesendet: " 
                            + w.getLuft() + "% ," + w.getTemp() + "C° ," + w.getWind() + "km/h ," + w.getJahrZeit());
    }
}
