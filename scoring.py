import growth_model as gm
import tox_model as tm
import scheduler as sch
import file_manipulation as fm
import numpy as np

def score(config, plan):
    schedule = sch.plan_to_schedule(
        *plan, config["start_strike"], config["start_cycle"]
    )
    duration = int(sch.duration(schedule))
    toxicities = fm.get_toxicities(config)
    tox, breaks = tm.RunToxDifferenceEquation(
        config["toxicity"], 0, duration, schedule, toxicities, config["r"], 10.0
    )
    new_schedule = tm.GenNewSched(schedule, breaks)
    growth_solution = gm.tumour_growth(
        config["burden"], duration, new_schedule, config["a"], plan
    )
    return {
        "plan": plan,
        "schedule": new_schedule,
        "toxicity_sol": tox,
        "burden_sol": growth_solution,
    }


def score_burden(burden_sol):
    return gm.final_tumour_volume(burden_sol)


def score_toxicity(toxicity_sol):
    return np.mean(toxicity_sol)


def score_total(toxicity, burden):
    return burden - toxicity