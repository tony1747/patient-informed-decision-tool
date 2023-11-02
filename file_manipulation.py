import pandas as pd


def cycles_to_df(cycles):
    return pd.DataFrame(cycles, columns=['drug', 'dose', 'start', 'end'])


def cycles_df_to_report(df):
    plan = {}
    for _, row in df.iterrows():
        drug = row['drug']
        dose = row['dose']
        start = row['start']
        end = row['end']
        if drug not in plan:
            plan[drug] = [{'dose': dose, 'start': start, 'end': end}]
        else:
            last_cycle = plan[drug][-1]
            if start > last_cycle['end']:
                plan[drug].append({'dose': 'break', 'start': last_cycle['end'], 'end': start})
            plan[drug].append({'dose': dose, 'start': start, 'end': end})
    return plan


def report_to_df(plan):
    schedule = []
    for drug, cycles in plan.items():
        for cycle in cycles:
            schedule.append([drug, cycle['dose'], cycle['start'], cycle['end']])
    df = pd.DataFrame(schedule, columns=['drug', 'dose', 'start', 'end'])
    df.set_index('drug', inplace=True)
    return df