public interface Wetterstation {
    public abstract void addObserver(Observer o);
    public abstract void deleteObserver(Observer o);
    public abstract void alleBenachrichten(Wetterdaten w);
}
