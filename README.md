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