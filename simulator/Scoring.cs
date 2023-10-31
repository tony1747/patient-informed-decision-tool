namespace simulator;

public abstract class Scoring
{
    private static readonly Random Rnd = new Random(42);
    
    static double Cost(Treatment treatment)
    {
        double result = 0;

        result = Rnd.NextDouble();
        
        return result;
    }
    
    static double Benefit(Treatment treatment)
    {
        double result = 0;

        result = Rnd.NextDouble();
        
        return result;
    }
    
    public static (double, double) Score(Schedule schedule)
    {
        double cost = 0;
        double benefit = 0;

        foreach (var treatment in schedule.Treatments)
        {
            cost += Cost(treatment);
            benefit += Benefit(treatment);
        }

        return (cost, benefit);
    }
}