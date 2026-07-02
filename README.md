## الهدف النهائي

المستخدم يكتب:

Build a REST API for Todo App

الـ AI يعمل:

                 User
                   │
                   ▼
           Supervisor Agent
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
Direct Answer          Planner Agent
                             │
                             ▼
                     Developer Agent
                             │
                             ▼
                      Reviewer Agent
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
             Accept                    Reject
                │                         │
                ▼                         │
          Final Response                 │
                                          │
                                          └──────► Developer

-> Agent is :
Agent

=

Prompt

+

LLM

+

Logic

+

Tools (اختياري)

+

Output Schema

-> Every agent needs:
كل agent هو مشروع صغير لوحده
1- Prompt

2- LLM

3- State

4- Output Schema

5- Node Function


## Sprint 1 - Shared Models

### Goal
Design reusable domain models shared between all agents instead of passing raw strings.

### Why?

In a Multi-Agent system, agents exchange structured information (tasks, plans, code, reviews), not arbitrary text.

Using Pydantic models provides:

- Type safety
- Validation
- Better readability
- Easier maintenance
- Seamless integration with LangChain and FastAPI

### Models Created

- Task
- Plan
- CodeArtifact
- Review

#### Why introduce a Step model?

Each execution step is represented as an object rather than a plain string.

This allows the system to:

- Track execution progress
- Retry failed steps
- Support Reflection Loops
- Enable Parallel Execution


# Sprint 2 - Shared State

## Goal

Create a shared state that allows all agents to exchange structured information.

## Why?

Instead of each agent maintaining its own data, all agents communicate through a single shared state.

This makes the workflow:

- Predictable
- Traceable
- Easy to debug
- Easy to extend

## State Fields

- Task
- Plan
- CodeArtifact
- Review
- Current Agent
- Next Agent
- Messages

## Key Concept

The State is **not** the business logic.

It is only the shared memory exchanged between agents.

# Sprint 3 - AgentType Enum

## Goal

Replace raw string values with a strongly typed enumeration.

## Why?

Using Enum avoids:

- Typographical mistakes
- Invalid agent names
- Magic strings

It also improves:

- IDE auto-completion
- Code readability
- Type safety

## Enum Values

- SUPERVISOR
- PLANNER
- DEVELOPER
- REVIEWER
- DIRECT_ANSWER

# Sprint 4 - Base Agent

## Goal

Create a common contract for every agent in the system.

## Why?

Instead of implementing each agent differently, every agent follows the same interface.

This improves:

- Consistency
- Readability
- Reusability
- Testing

## Key Concept

Every agent receives an `AgentState` and returns an updated `AgentState`.