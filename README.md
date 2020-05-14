# Zombie Simulation Project

In this project I'm going to develop a Python simulation of zombie apocalypse. There are characters of two classes - humans and zombies - who fight each other in order to win the battle. When a human wins a fight he kills a zombie. Otherwise, the human gets infected and turns into a zombie. 

## 1. Rules of the simulation

The simulation is held on a map which consists of an island and water around.

![image-20200426214221980](/data/img/screen.png)

Each of the zombies follows a simple strategy based on resultant proximity of humans around, combined with their individual ability to attract zombies. Humans use more sophisticated strategy which consists of two main components: they want to get closer to their strong companions and stay away from the weak ones, and they want to avoid strong zombies and follow the weak ones.

Each of those components is associated with a weight which determines how important the given component is. The weights can be optimized using reinforcement learning algorithms like Genetic Algorithm based on humans' strategy success.

Both strategies are described in details in files located in the rules/ folder.

### 2. Repository content

#### Folders

| Name       | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| classes/   | contains files with Python classes - separate for Human and Zombie class |
| data/      | contains input data for the simulation such as maps and characters' features |
| functions/ | contains external functions which are to be called from scripts |
| scripts/   | contains utility scripts for tasks like generating characters' data to the file |
| rules/     | contains detailed description of simulation rules            |



#### Files

| Name    | Description                   |
| ------- | ----------------------------- |
| main.py | main script of the simulation |

