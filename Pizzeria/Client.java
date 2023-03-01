import PizzaBackage.Pizza;
import PizzeriaBackage.Pizzeria;

public class Client{
    public static void main(String[] args) {

        Pizzeria pizzeria = new PizzaFactory();

        Pizza pizzaa = pizzeria.newPizza("Calzone");
        Pizza pizzab = pizzeria.newPizza("Salami");

    }
}