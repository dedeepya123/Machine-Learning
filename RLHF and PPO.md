## RLHF and PPO Summary

1. Train an Instruction-Tuned Model

This model already has language understanding, reasoning abilities, and instruction-following behavior.

2. Collect Human Preference Data

Humans compare model responses and choose preferred outputs.

Dataset:

Prompt
Chosen Response
Rejected Response

3. Train a Reward Model

Input:
Prompt + Response

Output:
Reward Score

Objective:

Reward(chosen) > Reward(rejected)

The reward model learns an approximation of human preferences.

4. Freeze the Reward Model

During RLHF, the reward model is not updated.

It serves as a fixed evaluator.

5. Initialize the Assistant

The instruction-tuned model becomes the initial assistant (policy).

6. Generate Responses

Assistant generates candidate responses.

Reward model assigns scores.

7. Optimize Assistant Using PPO

Language generation is viewed as:

State:
Current prompt + generated text

Action:
Next token

Policy:
P(next token | context)

Reward:
Reward model score

Goal:

Increase probability of responses with higher rewards.

8. Why PPO Is Needed

Direct reward maximization can cause reward hacking and unstable updates.

PPO constrains updates by limiting how much the new policy can differ from the previous policy.

Core idea:

Improve performance, but only through small, stable steps.

9. KL Penalty

A KL penalty keeps the assistant close to the original instruction-tuned model.

Final objective:

Reward Model Score
−
KL Divergence Penalty

This prevents the assistant from drifting too far from the capabilities learned during pretraining and instruction tuning.

Mental Model:

Pretraining
→ Learn capabilities

Instruction Tuning
→ Learn task following

Reward Model
→ Learn human preferences

PPO + KL
→ Make preferred behaviors more likely while remaining stable

Only the assistant model is updated during RLHF.

Reward model and reference model remain frozen.

## Entire RLHF Optimization Story

Step 1

Instruction Tuned Model

Good language
Good reasoning
Good capabilities

Step 2

Generate responses.

Step 3

Reward model scores them.

Step 4

Compute:

Reward
-
KL penalty

Step 5

Use PPO.

PPO updates:

Assistant only

Reward model remains frozen.

Reference model remains frozen.

Over time:

Assistant
↓
More helpful
More conversational
More aligned
Why PPO Was Chosen

At the time:

PPO was:

Stable
Simple
Widely used

for RL.
## Mental Model Of PPO

Think:

Reward Model:
"Humans like this"

Policy Gradient:

"Do more of this"

PPO:

"Do more of this,
but slowly."

KL Penalty:

"And don't forget
everything you already knew."
