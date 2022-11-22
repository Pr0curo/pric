# pric

small server for dice rolls

you can create a new room as a dice-master and set the rules (number of dice, order of rolling etc.) then you get two links. The first one for your dice-master session and the second one for the padawan-sessions, where every one with the link can jin the same room. There is a list of players and a hint who's turn it is. Also the leader will be marked (color?). On the same page there is a log of the rolls and you can export the session, basically a text-file. After everyone left you can login in the same session for ~24h - after that the room or session will be wiped.

the full programm will be featured by the following premisses

- learner project
- tdd first
- flask backend
  - redis?
  - document based db for 24h storage?
- easy to use front end
- easy installation on a droplet/raspberry pi
