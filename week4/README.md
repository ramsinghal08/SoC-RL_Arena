# Week 4

This week, we paused the coding to learn the theory of intro to Reinforcement Learning, read the first chapter of Sutton and Barto.

Here is the summary of my key takeaways and the concepts i studied.

The starting was how RL differs from the other parts of machine learning. RL operates in the real world of interaction. There is no explicit dataset telling the agent what to do. Instead, the agent discovers the best actions purely by trying them out and observing the reward. 

### Exploration vs Exploitation
This is a fundamental problem in RL. To maximize the reward, an agent wants to exploit the actions it already knows will yield a good outcome. However, to actually find those optimal actions, it must explore unexplored actions and try things it has never selected before. You cannot exclusively do one or the other without failing at the task.

### Values and Rewards
I liked understanding the difference between a "reward" and a "value".
Reward is the immediate feedback from the environment. It is short term, comparable to a biological response of pleasure or pain.
Value is the long term game. The value of a state represents the total amount of reward an agent can expect to get, starting from there.

We want our agents to make decisions based on value, not just immediate rewards, so that we can get the highest return over time.

### Tic-Tac-Toe Example
The example of playing Tic-Tac-Toe was amazing. I have also recently built this game in pyagme as a part of my dic project so it felt more better to me.

Instead of using a classical minimax algorithm which assumes perfect play from the opponent, or an evolutionary method that only evaluates a policy after end of some games, the RL approach evaluates individual states "during" the time of play. It evaluates the winning probabilities for every board configuration and update those values based on the states, and learns an optimal policy. It learns to set traps for opponent without needing a predefined model of how that opponent behaves.

Overall, this reading really helped me understand how RL agents actually learn. I am really looking forward to implement these concepts into Python and train an agent in our environment.