# caribbean-game-team-calculator
For the game Caribbean! by Snowbird, this tool computes the teams of companions that get along.  Additional constraints can be put on the team.  Note that:
<ul>
<li>This tool is based on data gathered from Caribbean! 1.051.</li>
<li>This tool requires Python 3.</li>
</ul>

Run this tool with no arguments to see usage instructions and compute all teams that get along:
    
    > python3 party_finder.py

A single string argument can be used to constrain the results.  For example, if you require that your party have an engineer and an herbalist, you would use:
    
    > python3 party_finder.py EH

The legal arguments are as follows:

Where the skills are represented as follows:
<ul>
<li>L Looting</li>
<li>B buccaneering</li>
<li>T Tracking</li>
<li>P Path-finding</li>
<li>N Navigation</li>
<li>H Herbalism</li>
<li>S Surgery</li>
<li>E Engineer</li>
<li>C captain (Fleetmaster, Naval Combat, Seafaring)</li>
<li>A tactics</li>
<li>R trade</li>
</ul>

(Upper case represents a starting skill level of 3 or greater, lower case represents starting skill level of 1 or 2)
