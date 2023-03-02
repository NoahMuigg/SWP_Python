import PizzaPackage.*;

public class HamburgPizzeria extends PizzaFactory{
    @Override
    protected Pizza erstellPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Hamburg Salami")){
            pizza = new HamburgSalami();
        }
        else if(pizzaname.equals("Hamburg Hawaii")){
            pizza = new HamburgHawaii();
        }
        else if(pizzaname.equals("Hamburg Calzone")){
            pizza = new HamburgClazone();
        }
        else if(pizzaname.equals("Hamburg Quattro Stationi")){
            pizza = new HamburgQuattroStationi();
        }
        else{
            System.out.println("Falsche eingabe!");
        }

        return pizza;

    }
}
