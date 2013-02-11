doge42
======

Tool for players of Crusader Kings II: The Republic. Named after Enrico
Dandolo, the 42nd Doge of Venice.

Calculates whether bribing a top liege before building tradeposts is
cost-effective. To use this look up the following things from within the game:

* distance of the tradepost (in the tooltip when hovering over the empty build
  icon)
* relations with the top liege of the province (not the lower liege that owns
  the province itself)
* cost to bribe the top liege
* effect on relations of that bribe

For instructions on usage, run the following on a command line with Python:

    python ck2tpcost.py -h

It was developed and tested on Python 2.7.3, but will probably work on Python
3.x as well. Windows users consult http://www.python.org/download/windows/
