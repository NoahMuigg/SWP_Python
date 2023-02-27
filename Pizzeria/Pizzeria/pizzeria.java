package Pizzeria;

import Pizza.pizza;

public abstract class pizzeria {
    
    public pizza newPizza(String pizzaname){

        pizza pizza = erstellPizza(pizzaname);
        pizza.backen();
        pizza.einpacken();
        pizza.schneiden();
        return pizza;
    }

    abstract pizza erstellPizza(String pizzaname);

    
}
