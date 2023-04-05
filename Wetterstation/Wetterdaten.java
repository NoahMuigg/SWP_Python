public class Wetterdaten {
    private double Temperatur;
    private double Luftfeuchtigkeit;
    private double Windstärke;
    private Jahreszeiten Jahreszeit;

    public Wetterdaten(double Temperatur, double Luftfeuchtigkeit, double Windstärke, Jahreszeiten Jahreszeit){
        this.Temperatur = Temperatur;
        this.Luftfeuchtigkeit = Luftfeuchtigkeit;
        this.Windstärke = Windstärke;
        this.Jahreszeit = Jahreszeit;
    }

    public double getTemp(){
        return Temperatur;
    }

    public double getLuft(){
        return Luftfeuchtigkeit;
    }

    public double getWind(){
        return Windstärke;
    }

    public Jahreszeiten getJahrZeit(){
        return Jahreszeit;
    }
}
