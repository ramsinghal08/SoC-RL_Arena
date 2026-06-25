# Seasons of Code: RL Arena

This repo tracks my progress through the RL Arena project. 

### Week 1: Python Basics
I built a simple 2D grid simulation where a player character navigates around obstacles using standard WASD inputs. Learned about object oriented programming in this week.

### Week 2: Pygame
This week i made a proper graphical interface using Pygame. I made a 2 player game where each player leaves a continuous trail. I built the collision system: detecting wall crashes, trail hits, and head on collisions.

### Week 3: Paper.io
This week the goal was to extend the Week 2 game into a Paper.io clone with territory capture. 
* Flood Fill Algorithm: When a player goes out of their territory, leaves a trail, and reconnects, the game needs to calculate the enclosed area. Implemented the BFS and DFS flood fill to capture this territory.
* Rendering Optimization: Drawing 6400 individual cell rectangles per frame is terribly slow. I optimized the rendering by mapping the grid states directly to a color array using NumPy and blitting it all at once, which kept the frame rate smooth.

### Week 4: Intro to Reinforcement Learning
This was focused on theoritical learning and i have added its summary in a separate readme in week4 folder.
