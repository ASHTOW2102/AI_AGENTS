# Adopt a shared event schema

Status: accepted

## Context
Several services publish incompatible representations of the same business event.

## Decision
Adopt a versioned JSON event envelope with documented compatibility rules.

## Alternatives
We considered per-team schemas and a binary schema registry before deciding.

## Consequences
Publishers must validate envelopes, and consumers must tolerate additive fields.
