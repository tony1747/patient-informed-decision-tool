namespace simulator;

public class Schedule
{
    public Schedule(List<Treatment> treatments)
    {
        Treatments = treatments;
    }

    public List<Treatment> Treatments { get; init; }

    public override string ToString()
    {
        string res = "";
        for (int i = 0; i < Treatments.Count; i++)
        {
            res += $"Treatment {i + 1}: {Treatments[i]}\n";
        }
        return res;
    }
}