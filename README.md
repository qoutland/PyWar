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
## **Intel Xeon(R) CPU E5-1607 v2 @3.00GHz 4 Cores, 4 Logical Processors**

| Type | 100 sims | 1000 sims | 5000 sims | 10000 sims |
| ------ | ------ | ------ | ------ | ------ |
| War |**1.42 s** | **14.20 s** | **73.54 s** | **146.60 s** |
| WarOne | **1.39 s** | **15.91 s** | **75.07 s** | **153.93 s** |
| WarThread | **0.84 s** | **5.66 s** | **23.82 s** | **49.62 s** |

## **Intel i7-6700K CPU @ 4.00 GHz 4 Cores, 8 Logical Processors**
| Type | 100 sims | 1000 sims | 5000 sims | 10000 sims |
| ------ | ------ | ------ | ------ | ------ |
| War |**0.58s** | **5.18 s** | **25.17 s** | **49.63 s** |
| WarOne | **0.47 s** | **5.44 s** | **25.54 s** | **53.45 s** |
| WarThread | **0.42 s** | **1.53 s** | **6.76 s** | **14.33 s** |

### Bonus
* 50000: **70.41 s**
* 100000: **138.25 s**

## **Intel Xeon(R) CPU X7460 @2.66GHz 8 Sockets, 1 Core per Socket (VMWare)**

| Type | 100 sims | 1000 sims | 5000 sims | 10000 sims |
| ------ | ------ | ------ | ------ | ------ |
| War |**0.98 s** | **10.64 s** | **51.97 s** | **104.03 s** |
| WarOne | **1.06 s** | **11.28 s** | **56.20 s** | **106.88 s** |
| WarThread | **0.27 s** | **1.51 s** | **6.69 s** | **13.61 s** |

### Bonus
* 50000: **66.38s**
* 100000: **131.56s**
