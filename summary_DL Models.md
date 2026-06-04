# Deep Learning Learning Journey

## Core Philosophy

The goal is not to memorize architectures or equations, but to understand:

* What problem researchers faced.
* Why existing approaches were insufficient.
* What new idea was introduced.
* How representations evolved through the network.
* How the field progressed toward modern AI systems.

---

# 1. Feed Forward Neural Networks (MLPs)

### Problem

Learn patterns from fixed-size inputs.

### Key Idea

Each layer learns increasingly useful feature representations through learned transformations.

### Learning

* Linear transformations
* Activations
* Backpropagation
* Representation learning

---

# 2. Convolutional Neural Networks (CNNs)

### Problem

Images contain spatial structure that MLPs fail to exploit efficiently.

### Key Idea

Local receptive fields and weight sharing.

### Learning

* Edges
* Textures
* Parts
* Objects

Hierarchical spatial feature learning.

---

# 3. Regularization & Generalization

### Problem

Networks memorize training data.

### Solutions

* Data augmentation
* Weight decay
* Dropout
* Larger datasets

### Learning

Models should learn underlying patterns rather than memorizing samples.

---

# 4. Transfer Learning

### Problem

Training large models from scratch is expensive.

### Key Idea

Reuse learned representations.

### Learning

* Feature extraction
* Fine-tuning
* Domain adaptation

---

# 5. Sequence Learning

### Problem

Language and many real-world problems are sequential.

Input size is variable and order matters.

### Question

How can a model remember previous information?

---

# 6. Recurrent Neural Networks (RNNs)

### Key Idea

Introduce hidden state.

### Learning

Convert semantic representations into contextual representations.

At each timestep:

* Current word information
* Previous context

are combined to produce richer sequence understanding.

### Limitation

Vanishing gradients and weak long-term memory.

---

# 7. Backpropagation Through Time (BPTT)

### Problem

How do RNNs learn?

### Key Idea

Unroll the network across time and propagate gradients backward through every timestep.

### Learning

The model learns:

* Input transformations
* Context transformations
* Sequence dependencies

---

# 8. LSTMs

### Problem

RNNs struggle with long-term dependencies.

### Key Idea

Explicit memory cell and gating mechanisms.

### Gates

* Forget Gate
* Input Gate
* Output Gate

### Learning

Preserve important information and discard irrelevant information.

---

# 9. GRUs

### Problem

LSTMs are powerful but complex.

### Key Idea

Simpler gated memory mechanism.

### Learning

Efficient long-term dependency modeling with fewer parameters.

---

# 10. Seq2Seq Encoder-Decoder

### Problem

Need variable-length input and output.

Example:

English → French translation

### Key Idea

Encoder creates contextual representations.

Decoder generates target sequence.

### Limitation

Entire source sequence compressed into a single context vector.

Information bottleneck.

---

# 11. Bahdanau Attention

### Problem

Single context vector loses information.

### Key Idea

Allow decoder to dynamically retrieve relevant encoder representations.

### Learning

Instead of relying on one fixed summary:

* Encoder states become memory.
* Decoder state becomes query.
* Attention retrieves relevant information.

### Major Insight

Memory + Retrieval is more powerful than memory alone.

This idea becomes the foundation of modern AI systems.

