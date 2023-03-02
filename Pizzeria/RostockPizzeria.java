import PizzaPackage.*;

public class RostockPizzeria extends PizzaFactory{
    @Override
    protected Pizza erstellPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Rostock Salami")){
            pizza = new RoststockSalami();
        }
        else if(pizzaname.equals("Rostock Hawaii")){
            pizza = new RoststockHawaii();
        }
        else if(pizzaname.equals("Rostock Calzone")){
            pizza = new RoststockCalzone();
        }
        else if(pizzaname.equals("Rostock Quattro Stationi")){
            pizza = new RoststockQuattroStationi();
        }
        else{
            System.out.println("Falsche eingabe!");
        }

        return pizza;

    }
}
