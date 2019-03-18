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
* War: **1.42s** 
* WarOne: **1.39s**
* WarThread: **0.84s**

### 1000 Runs:
* War: **14.20s**
* WarOne: **15.91s**
* WarThread: **5.66s**

### 5000 Runs:
* War: **73.54s**
* WarOne: **75.07s**
* WarThread: **23.82s**

### 10000 Runs:
* War: **146.60s**
* WarOne: **153.93s**
* WarThread: **49.62s**

**Intel Xeon(R) CPU X7460 @2.66GHz 8 Sockets, 1 Core per Socket (VMWare)**

### 1000 Runs:
* War: **10.64s**
* WarOne: **11.28s**
* WarThread: **1.51s**

### 10000 Runs:
* War: **104.03s**
* WarOne: **106.88s**
* WarThread: **13.61s**

### Just for fun warThread
* 50000: **66.38s**
* 100000: **131.56s**
