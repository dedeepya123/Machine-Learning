## What Does XL Mean?

Transformer-XL stands for:

Transformer eXtra Long

The goal was:

Extend context beyond a fixed-length segment.

Now let's get into the important part:

How Does Attention Actually Work?
<img width="922" height="376" alt="image" src="https://github.com/user-attachments/assets/d7f629ae-8b14-4988-8d12-b24447a15514" />



Suppose we're looking at layer: l

<img width="747" height="472" alt="image" src="https://github.com/user-attachments/assets/a9bef523-a067-4866-871b-4f0963433410" />

This becomes memory for layer l.

Now Chunk 2 Arrives

<img width="962" height="446" alt="image" src="https://github.com/user-attachments/assets/51eecbd0-6ad8-412a-a50b-94efea581006" />


Do we concatenate memory with current chunk and then compute Q,K,V?

Almost.

But there is one important distinction.

Queries
<img width="882" height="417" alt="image" src="https://github.com/user-attachments/assets/969eb3c4-4380-4c17-a04a-25f9ef13b33f" />


Keys

<img width="982" height="622" alt="image" src="https://github.com/user-attachments/assets/5a656145-1a35-4000-b8b5-e857b242cf72" />

<img width="801" height="347" alt="image" src="https://github.com/user-attachments/assets/d3245783-2235-4549-9a88-dd2efa4da6dd" />

<img width="1062" height="467" alt="image" src="https://github.com/user-attachments/assets/a7b7b74d-047b-45c3-b1e6-1d981f3c40f7" />

Result:

512×1024

Meaning:

Every token in chunk 2 can attend to:

Current chunk

+

Previous memory

## Why Queries Only From Current Chunk?

Think about what we're trying to compute.

We're updating representations for:

Chunk 2 tokens

Not chunk 1.

Chunk 1 is already finished.

Memory acts like:

Read-only context

Current chunk acts like:

Things being updated

So:

Memory provides K,V

Current chunk provides Q,K,V
Visual Picture

Layer l

Memory M(l)
      │
      ▼
     K,V

Current Chunk H(l-1)
      │
      ├──► Q
      ├──► K
      └──► V

Attention:
Q attends to [Memory + Current Chunk]
Why Store Memory Per Layer?

Another subtle point.

You might ask:

Why not store only the final layer?

Because each layer learns different things.

Early layers:

Local syntax

Middle layers:

Entities
Relationships

Higher layers:

Semantics
Reasoning

Researchers wanted each layer to access its own historical representation.

Therefore:

M(1)
M(2)
M(3)

...

all stored separately.

Is This Similar To KV Cache?

Notice something interesting.

Transformer-XL memory:

Store hidden states

Then later:

Convert to K,V again

KV Cache:

Store K,V directly

You can almost think of Transformer-XL as an ancestor of memory-based ideas that eventually influenced later architectures.
