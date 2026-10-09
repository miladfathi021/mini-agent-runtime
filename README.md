# mini-agent-runtime

## Project Overview

A Python runtime for an AI agent, built from scratch to study how an agent actually runs. The work focuses on the core mechanisms: an execution loop, tool calls, conversation state, and persistence. A real model client is not connected yet.

## Core Concepts

- **Execution loop.** The loop asks a model interface for the next step, runs a tool when one is requested, records the exchange, and stops on a final answer or after a fixed iteration limit.
- **Tool registration and execution.** Tools are registered by name. The runtime looks up the handler, calls it, and returns a structured success or error result, including when the tool is missing or the handler fails.
- **Argument validation.** A call is checked for missing required parameters, unknown parameters, and incorrect types before the handler runs.
- **State management.** Messages and the current iteration live in an agent state that can be updated and serialized.
- **JSON checkpoints.** The loop writes that state to a JSON file as it runs. The same state can be loaded back from the file. A missing or invalid file returns no state.
- **Modular design.** The loop, runtime, registry, validator, state, and checkpoint are separate modules.
- **Automated testing.** Pytest covers the loop, tool execution, validation failures, state serialization, and checkpoint save and load.

## Development Status

**In Progress.** The pieces above are implemented and tested. This is a learning project, not a production runtime.

## Project Philosophy

The aim is to learn agent engineering by building the underlying mechanisms directly, rather than relying entirely on an existing agent framework.
