## Why was Continuous Batching introduced?

Problem With Static Batching:

Requests finish at different times.

Finished slots remain idle until the entire batch completes.

GPU utilization decreases over time.

Researcher Insight:

A batch should not be treated as a fixed group.

Instead, treat it as a continuously changing pool of active requests.

Idea:

When a request finishes:

* Remove it immediately
* Insert a new waiting request immediately

Generation continues without waiting for the entire batch to finish.

This is called:

Continuous Batching

Key Component:

Scheduler

Responsibilities:

* Track active requests
* Remove finished requests
* Add waiting requests
* Launch decoding steps

Benefits:

* Higher GPU utilization
* Better throughput
* Lower serving cost
* Reduced idle GPU time

Deep Insight:

Inference serving became a scheduling problem, not just a model computation problem.

New Problem Discovered:

Each request owns a KV cache.

As requests continuously enter and leave:

* KV caches are allocated and freed repeatedly
* GPU memory becomes fragmented

This memory fragmentation became the next major bottleneck.

Next Research Question:

How can KV cache memory be managed efficiently when requests continuously join and leave?

## Summary

Continuous batching is an inference scheduling strategy where requests can dynamically enter and leave the active batch during generation. Finished requests are immediately replaced with new requests, allowing GPUs to remain highly utilized and significantly improving throughput compared to static batching.
