import java.util.List;
import java.util.ArrayList;

public abstract class Wetterstation1 implements Wetterstation{

    private List<Observer> Observers = new ArrayList<Observer>();
    
    @Override
    public void addObserver(Observer o){
        Observers.add(o);
    }

    @Override
    public void deleteObserver(Observer o){
        Observers.remove(o);
    }

    @Override
    public void alleBenachrichten(Wetterdaten w){
        for(Observer o : Observers){
            o.update(w);
        }
    }

}