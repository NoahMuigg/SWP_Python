import Pizza.calzone;
import Pizza.hawaii;
import Pizza.pizza;
import Pizza.quattroStationi;
import Pizza.salami;


public class pizzaFactory {

    public pizza newPizza(String pizzaname){

        pizza pizza = null;

        if(pizzaname.equals("Calzone")){
            pizza = new calzone();
        }
        else if(pizzaname.equals("Salami")){
            pizza = new salami();
        }
        else if(pizzaname.equals("Hawaii")){
            pizza = new hawaii();
        }
        else if(pizzaname.equals("Quattro Stationi")){
            pizza = new quattroStationi();
        }

        return pizza;

    }

}
