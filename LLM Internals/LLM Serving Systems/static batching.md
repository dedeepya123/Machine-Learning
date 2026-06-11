## Why was Static Batching introduced and why did it fail?

Researcher Goal:

Improve GPU utilization by processing multiple requests together.

Idea:

Wait for requests to accumulate.

Create a fixed batch.

Run inference on the entire batch.

Benefits:

* Better GPU utilization
* Higher throughput
* Lower cost per request

Problem 1: Latency

Users arriving early must wait until the batch fills.

Large batch size:

* Better throughput
* Worse latency

Small batch size:

* Better latency
* Worse utilization

Problem 2: Different Completion Times

Requests generate different numbers of tokens.

Some finish early.

Some continue much longer.

Static batching keeps all requests together.

Finished slots become idle and cannot be reused.

Result:

GPU resources are wasted.

Deep Insight:

Static batching assumes:

Everyone starts together.
Everyone finishes together.

This works for training.

It does not work for inference.

Researcher Question:

Can finished requests be immediately replaced with new requests?

This idea led to Dynamic / Continuous Batching.

## Summary

Static batching groups requests into fixed batches before execution. While it improves GPU utilization compared to single-request inference, it increases latency because requests must wait for a batch to form. It also wastes GPU resources during decoding because requests finish at different times, leaving idle batch slots that cannot be reused until the entire batch completes.
