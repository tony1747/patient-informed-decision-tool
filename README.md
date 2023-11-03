# patient-informed-decision-tool
MOFFITT IMO 2023 Workshop

## Requirements

* Conda
* Python 3.9 or greater

The required packages are listed in `conda_moffitt.yml`. To install them, run:

```
conda env create -f conda_moffitt.yml
```

##  Interfaces

### Patient:

Patient configuration is specified in the `patient_config.json` file. The file contains the following fields:

* `burden`: the initial tumor burden
* `toxicity`: the initial toxicity
* `start_strike`: the 1-index of the first drug in the sequence
* `start_cycle`: the 1-index of the first cycle in the strike

### Treatment plan:

A treatment plan is a sequence of doses for the pre-specified drug sequence (i.e. *strikes*). A does is a number in range 0-1. E.g.

````
plan = (1, 0.75, 0.75, 0.5)
````

### Treatment schedule:

A schedule is a list of individual cycles. Each cycle specifies a drug, a does, start (in days), and an end.

````
schedule = 
[
    [1, 0.5, 1, 2],
    [1, 0.3, 5, 9],
    [2, 0.9, 2, 20],
    [2, 0.9, 10, 20],
    [3, 0.8, 30, 40],
    [4, 0.8, 70, 80]
]
````