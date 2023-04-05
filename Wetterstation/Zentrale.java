public class Zentrale extends Wetterstation1{
    private Wetterdaten neueWetterdaten;

    public void setNeueWetterdaten(Wetterdaten w){
        this.neueWetterdaten = w;
        alleBenachrichten(neueWetterdaten);
    }

    public Wetterdaten getNeueWetterdaten(){
        return neueWetterdaten;
    }
}
