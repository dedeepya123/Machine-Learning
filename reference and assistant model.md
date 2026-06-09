## For same  prompt we are comparing the output prob dist of reference and assistant models ?

The comparison is not simply "for the same prompt compare the entire output distribution."

It's more like:

Prompt
↓
Assistant generates a response
↓
Measure how likely that exact response
is under both models

Let's see an example.

Prompt:

How do I learn Python?

Assistant generates:

Start with fundamentals and build projects.

Now we compute:
<img width="890" height="273" alt="image" src="https://github.com/user-attachments/assets/d80914ae-a01a-4528-b775-f91277f7adfa" />

Notice something subtle:

We are evaluating the same generated response under both models.

Not generating two separate responses and comparing them.

Token Level View

Suppose response is:

Start
with
fundamentals
and
build
projects

Assistant assigns:


<img width="1008" height="290" alt="image" src="https://github.com/user-attachments/assets/c5bd10fb-a876-4a82-90fc-7ad250fee4b6" />
<img width="990" height="287" alt="image" src="https://github.com/user-attachments/assets/88029373-0856-453f-bd63-7cc493be08a8" />

Then we compare these probabilities.

Intuition

Suppose:

Assistant says:

Start with fundamentals and build projects.

Reference thinks:

Yeah, that's pretty reasonable.

Probability not too different.

KL small.

Now imagine assistant starts saying:

PYTHON PYTHON PYTHON PYTHON PYTHON!!!

because it found some reward-model loophole.

Reference thinks:

Whoa, that's extremely unlikely.

Probability difference becomes huge.

KL penalty becomes large.

Even More Precise

Mathematically, PPO-RLHF is trying to keep:

π
assistant
	​

(token∣context)

close to

π
reference
	​

(token∣context)

at every generation step.

So conceptually:

Same prompt
+
Same generated trajectory
↓
Compare token probabilities
under assistant and reference
Mental Model

Don't think:

Reference Output
vs
Assistant Output

Think:

Reference's belief about the response
vs
Assistant's belief about the response

The reference model is acting like an anchor saying:

"Would the original instruction-tuned GPT also consider this response reasonably likely?"

If yes:

Small penalty

If no:

Large penalty
