import PizzaBackage.Calzone;
import PizzaBackage.Hawaii;
import PizzaBackage.Pizza;
import PizzaBackage.QuattroStationi;
import PizzaBackage.Salami;
import PizzeriaBackage.Pizzeria;


class PizzaFactory extends Pizzeria{

    @Override
    protected Pizza erstellPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Calzone")){
            pizza = new Calzone();
        }
        else if(pizzaname.equals("Salami")){
            pizza = new Salami();
        }
        else if(pizzaname.equals("Hawaii")){
            pizza = new Hawaii();
        }
        else if(pizzaname.equals("Quattro Stationi")){
            pizza = new QuattroStationi();
        }
        else{
            System.out.println("Falsche eingabe!");
        }

        return pizza;

    }

}
