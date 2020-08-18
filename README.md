# YugiohPriceChecker

![Alpha status](https://img.shields.io/badge/Project%20status-Alpha-red.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://camo.githubusercontent.com/fd8c489427511a31795637b3168c0d06532f4483/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f77696b6970656469612d6170692e7376673f7374796c653d666c6174)](https://pypi.python.org/pypi/ansicolortags/)

Utilizes yugiohprices and YugiohWikiApi in order to analyze market data and additional card information. 

# Output Result Examples

Go to the decklist_table directory and select any text file, those are the output that contain the full data table of decklists.

YuGiOhPricesAPI queries provide the following data:
* Price (Avg)
* Price (High)
* Price (Low)
* Shift 3M
* Shift 6M
* Shift 1Y

Fandom and WikiMedia API provide the following data:
* Rarity
* Set
* Language

Example:

Table contains self-explanatory headers.
```
+-----+-----------------------------------------------+---------------+-----+------------+-------+-------------+--------------+-------------+----------+----------+----------+
| Qty |                      Name                     |     Rarity    | Ed. |    Set     | Lang. | Price (Avg) | Price (High) | Price (Low) | Shift 3M | Shift 6M | Shift 1Y |
+-----+-----------------------------------------------+---------------+-----+------------+-------+-------------+--------------+-------------+----------+----------+----------+
|  1  | Black Luster Soldier - Envoy of the Beginning |     Ultra     | Unl |  IOC-025   |  ENG  |     54.0    |    800.0     |    17.95    |  96.94   |  248.61  |  141.29  |
|  2  |            Caius the Shadow Monarch           |    Ultimate   | Unl | TU03-EN000 |  ENG  |    83.69    |    100.98    |     70.0    |  53.08   |  86.77   |  53.93   |
|  1  |                   Tragoedia                   |    Ultimate   | Unl | TU04-EN000 |  SPA  |    94.97    |    199.99    |    85.99    |  162.2   |  176.4   |  89.07   |
|  2  |                 Effect Veiler                 |    Ultimate   | 1st | DREV-EN002 |  ENG  |    20.32    |    317.82    |     9.6     |  184.59  |  201.93  |  -74.76  |
|  2  |                    Maxx "C"                   |    Ultimate   | Unl | AP04-EN002 |  SPA  |    577.81   |   1000.99    |    249.99   |  49.57   |  100.88  |  246.13  |
+-----+-----------------------------------------------+---------------+-----+------------+-------+-------------+--------------+-------------+----------+----------+----------+
Date Updated: 2020-08-09
```

Full summation estimates of the average price, high prices (high to max rarity), and low prices (low rarity)
```
+---------+-------+------+
| Average |  High | Low  |
+---------+-------+------+
|   3231  | 10831 | 1905 |
+---------+-------+------+
```

Quantity breakdown of particular printing rarities:
```
+--------+------------+------------+-------------+---------------+-----------------------------------+
| Common | Super Rare | Ultra Rare | Secret Rare | Ultimate Rare | Duel Terminal Ultra Parallel Rare |
+--------+------------+------------+-------------+---------------+-----------------------------------+
|   2    |     9      |     11     |      2      |       28      |                 2                 |
+--------+------------+------------+-------------+---------------+-----------------------------------+
```

Quantity breakdown of particular languages:
```
+-----+-----+-----+-----+
| ENG | DEU | ITA | SPA |
+-----+-----+-----+-----+
|  28 |  8  |  14 |  4  |
+-----+-----+-----+-----+
```

Card name language converted:

```
+------------+--------------------------------+----------------------------------------+-------------+
|    Set     |              Name              |              Foreign Name              | Foreign Set |
+------------+--------------------------------+----------------------------------------+-------------+
| TU04-EN000 |           Tragoedia            |               Tragoedia                |  TU04-SP000 |
| AP04-EN002 |            Maxx "C"            |                "C" Maxx                |  AP04-SP002 |
| AP06-EN001 | Tour Guide From the Underworld |    Guida Tour del Mondo Sotterraneo    |  AP06-IT001 |
| STBL-EN018 |          Glow-Up Bulb          |             Bulbo Luminoso             |  STBL-IT018 |
| EXVC-ENSP1 |          Reborn Tengu          |           Tengu Resuscitato            |  EXVC-ITSP1 |
| CP01-EN005 |        Night Assailant         |          Assalitore Notturno           |  CP01-IT005 |
+------------+--------------------------------+----------------------------------------+-------------+
```