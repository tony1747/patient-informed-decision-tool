import pandas as pd


def cycles_to_df(cycles):
    df = pd.DataFrame(
        cycles,
        columns=["strike", "dose", "start", "end"]
    )
    df = df.astype({"strike": int, "dose": float, "start": int, "end": int})
    return df


def cycles_df_to_report(df):
    plan = {}
    for _, row in df.iterrows():
        strike = row["strike"]
        dose = row["dose"]
        start = row["start"]
        end = row["end"]
        if strike not in plan:
            plan[strike] = [{"dose": dose, "start": start, "end": end}]
        else:
            last_cycle = plan[strike][-1]
            if start > last_cycle["end"]:
                plan[strike].append(
                    {"dose": "break", "start": last_cycle["end"], "end": start}
                )
            plan[strike].append({"dose": dose, "start": start, "end": end})
    return plan


def report_to_df(plan):
    schedule = []
    for strike, cycles in plan.items():
        for cycle in cycles:
            schedule.append([strike, cycle["dose"], cycle["end"] - cycle["start"]])
    df = pd.DataFrame(schedule, columns=["strike", "dose", "days"])
    df = df.astype({"strike": int, "dose": str, "days": int})
    return df


def get_plan(params):
    return [params[f"s{i}"] for i in [1,2,3,4]]


def get_toxicities(params):
    return [params[f"tx{i}"] for i in [1,2,3,4]]