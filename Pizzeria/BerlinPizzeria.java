import PizzaPackage.*;

public class BerlinPizzeria extends PizzaFactory{

    @Override
    protected Pizza erstellPizza(String pizzaname){

        Pizza pizza = null;

        if(pizzaname.equals("Berlin Calzone")){
            pizza = new BerlinCalzone();
        }
        else if(pizzaname.equals("Berlin Hawaii")){
            pizza = new BerlinHawaii();
        }
        else if(pizzaname.equals("Berlin Calzone")){
            pizza = new BerlinCalzone();
        }
        else if(pizzaname.equals("Berlin Quattro Stationi")){
            pizza = new BerlinQuattroStationi();
        }
        else{
            System.out.println("Falsche eingabe!");
        }

        return pizza;

    }


}
