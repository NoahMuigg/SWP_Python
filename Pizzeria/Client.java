import PizzaPackage.Pizza;

public class Client{
    public static void main(String[] args) {

        PizzaFactory pizzeria = new Pizzeria();
        Pizza pizzaa = pizzeria.newPizza("Calzone");
        Pizza pizzab = pizzeria.newPizza("Salami");

        PizzaFactory pizzeriaH = new HamburgPizzeria();
        Pizza pizzaH = pizzeriaH.newPizza("Hamburg Calzone");

    }
}