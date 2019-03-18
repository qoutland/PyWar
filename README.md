# PyWar
War simulator in Python

## Run Instructions
war.py

```
python war.py *times*
```

warOne.py (All simulations done in a single, multidimensional array.)

```
python warOne.py *times*
```

warThread.py (Simulations are distributed across processes):

```
python warThread.py *times*
```

## Test results
**Intel Xeon(R) CPU E5-1607 v2 @3.00GHz 4 Cores, 4 Logical Processors**

### 100 Runs:
* War: **1.42** 
* WarOne: **1.39**
* WarThread: **0.84**

### 1000 Runs:
* War: **14.20**
* WarOne: **15.91**
* WarThread: **5.66**

### 5000 Runs:
* War: **73.54**
* WarOne: **75.07**
* WarThread: **23.82**

### 10000 Runs:
* War: **146.60**
* WarOne: **153.93**
* WarThread: **49.62**