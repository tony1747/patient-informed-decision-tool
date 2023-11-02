# patient-informed-decision-tool
MOFFITT IMO 2023 Workshop

##  Interfaces

### Treatment plan:

A treatment plan is a sequence of doses for the pre-specified drug sequence (i.e. *strikes*). A does is a number in range 0-1. E.g.

````
plan = (1, 0.75, 0.75, 0.5)
````

### Treatment schedule:

A schedule is a list of individual cycles. Each cycle specifies a drug, a does, start (in days), and an end.

````
schedule = [
    ["d1", 0.5, 1., 2.],
    ["d1", 0.3, 5., 9.],
    ["d2", 0.9, 2., 20.],
    ["d2", 0.9, 10., 20.],
    ["d3", 0.8, 30., 40.],
    ["d4", 0.8, 70., 80.]
]
````