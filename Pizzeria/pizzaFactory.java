import PizzaPackage.Pizza;

public abstract class PizzaFactory{

    public Pizza newPizza(String pizzaname){

        Pizza pizza = erstellPizza(pizzaname);
        pizza.backen();
        pizza.einpacken();
        pizza.schneiden();
        
        return pizza;
    }

    protected abstract Pizza erstellPizza(String pizzaname);

}
