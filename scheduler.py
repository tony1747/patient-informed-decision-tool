"""
generates dosing schedule from a set of drug values
d1: Taxo+Cyto
d2: trast
d3: Xeloda
d4: Fulv+Ribo
"""
def plan_to_schedule(d1, d2, d3, d4, start_strike, start_cycle):
    # throw if start_strike or start_cycle == 0
    if start_cycle == 0 or start_strike == 0:
        raise Exception("Schedules and cycles are 1-indexed")

    days=0
    out=[]
    #1st strike
    if start_strike<=1:
        for i in range(0,4):
            if start_strike!=1 or (start_strike == 1 and i >= start_cycle - 1):
                out.append(["d1",d1,days,days+21])
            days+=21
    #2nd strike
    if start_strike<=2:
        for i in range(0,4):
            if start_strike!=2 or (start_strike <= 2 and i >= start_cycle - 1):
                out.append(["d2",d2,days,days+21])
            days+=21
    #3rd strike
    if start_strike<=3:
        for i in range(0,5):
            if start_strike!=3 or (start_strike <= 3 and i >= start_cycle - 1):
                out.append(["d3",d3,days,days+21])
            days+=21
    #4th strike
    if start_strike<=4:
        for i in range(0,5):
            if start_strike!=4 or (start_strike <= 4 and i >= start_cycle - 1):
                out.append(["d4",d4,days,days+28])
            days+=28
    return out


def duration(schedule):
    return schedule[-1][3]
    