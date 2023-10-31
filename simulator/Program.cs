// See https://aka.ms/new-console-template for more information

using System.Diagnostics;
using simulator;

// Create a new Stopwatch instance
Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();

const int STEPS = 4;

var allTreatments =
    from dose in Enum.GetValues<Dose>()
    from period in Enum.GetValues<Period>()
    select new Treatment(dose, period);
var treatmentList = allTreatments.ToList();
    
// Create a product of all treatments
var allSchedules = 
    from t1 in treatmentList
    from t2 in treatmentList
    from t3 in treatmentList
    from t4 in treatmentList
    select new Schedule(new List<Treatment> { t1, t2, t3, t4 });

var scoredSchedules = allSchedules.Select(sch => (sch, Scoring.Score(sch))).ToList();

// Find where benefit - cost is max
var bestSchedule = scoredSchedules.MaxBy(sch => sch.Item2.Item2 - sch.Item2.Item1);


stopwatch.Stop();

// Get the elapsed time as a TimeSpan
TimeSpan elapsed = stopwatch.Elapsed;

// Access seconds and milliseconds
int seconds = elapsed.Seconds;
int milliseconds = elapsed.Milliseconds;
Console.WriteLine($"Tested {scoredSchedules.Count} treatment schedules.");
Console.WriteLine($"Elapsed Time: {seconds} seconds {milliseconds} milliseconds");
Console.WriteLine($"Best schedule: {bestSchedule.Item1}Cost: {bestSchedule.Item2.Item1}\nBenefit: {bestSchedule.Item2.Item2}");
