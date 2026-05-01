# Knowledge Artifact: Crab (Checkpoint-and-Restore for Agent SandBoxes)

## $\text{Architectural Overview}$
$\text{Crab}$ addresses the **Agent-OS Semantic Gap**: the discrepancy between an agent's high-level tool calls and the actual state changes (filesystems, processes) occurring within the underlying sandbox/microVM. This gap leads to inefficient checkpointing (either too coarse/incorrect or too dense/expensive). $\text{Crab}$ implements a **Semantics-Aware Checkpoint/Restore ($\text{C/R}$)** runtime that optimizes state persistence based on the actual OS-visible effects of each turn.

## $\text{Key Mechanisms}$

### 1. eBPF-Based Effect Inspection ($\text{EEI}$)
$\text{Crab}$ uses eBPF to monitor OS-level events in real-time. It classifies the "Effect Density" of a turn $\tau$:
$$\text{Density}(\tau) = \sum \text{Syscalls}(\text{Write}, \text{Exec}, \text{Network})$$
If a turn produces no recovery-relevant state (which occurs in $>75\%$ of turns), the system skips the checkpoint entirely.

### 2. Turn-Aligned Coordination ($\text{TAC}$)
The runtime aligns the asynchronous C/R process with the agent's turn boundaries, overlapping the expensive I/O of state persistence with the LLM's inference wait time:
$$\text{Latency}_{\text{total}} = \max(\text{Latency}_{\text{Inference}}, \text{Latency}_{\text{C/R}})$$

### 3. Host-Scoped Traffic Scheduling
To prevent I/O storms in dense co-location scenarios, $\text{Crab}$ schedules checkpoint traffic across multiple sandboxes, ensuring that the aggregate throughput does not saturate the host's storage bandwidth.

## $\text{Empirical Utility}$
- **Correctness**: Raises recovery correctness from $8\%$ (chat-only) to $100\%$.
- **Overhead**: Cuts checkpoint traffic by up to $87\%$ while staying within $1.9\%$ of fault-free execution time.

## $\text{Actionability}$
- **Implementation Path**: Implement an eBPF-based monitor to track filesystem and process changes per agent turn. Trigger a full C/R only when "significant" state changes are detected.
- **Metric Shift**: Track **Checkpoint Efficiency** ($\frac{\text{Recovery Correctness}}{\text{Traffic Volume}}$).

## $\text{Sources}$
- [arXiv:2604.28138](https://arxiv.org/abs/2604.28138) - Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes.
