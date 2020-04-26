# Zombie Simulation Project

In this project I'm going to develop a Python simulation of zombie apocalypse. The simulation contains characters of two classes - humans and zombies - who fight each other in order to win the battle. When a human wins a fight he kills a zombie. In the other case human gets infected and becomes a zombie. 

## 1. Rules of the simulation

The simulation is held on a map which consists of an island and water around.

![image-20200426214221980](C:\Users\Patryk\Dropbox\Dev\ProjektZombie\data\img\screen.png)

Each of the zombies follows a simple strategy based on resultant proximity of humans around combined with their individual ability to attract zombies. Humans use more sophisticated strategy which consists of three components: they want to get closer to their companions (especially the strongest ones), they want to avoid zombies (especially the strongest ones) and they want to keep far from the borders of the island where they can be trapped.

Each of those three components is associated with a weight which determines how important is the given component comparing to the others. The weights can be optimized using reinforcement learning algorithms like Genetic Algorithm based on humans' strategy success.



### 2. Repository content

#### Folders

| Name       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| classes/   | contains files with Python classes - separate for Human and Zombie class |
| data/      | contains input data for the simulation such as maps and characters' features |
| functions/ | contains external functions which are to be called from scripts |
| scripts/   | contains utility scripts for tasks like generating characters' data to the file |



#### Files

| Name    | Description                   |
| ------- | ----------------------------- |
| main.py | main script of the simulation |

