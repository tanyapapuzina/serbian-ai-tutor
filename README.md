# Serbian AI Tutor

AI-powered Serbian language tutor designed for Russian-speaking learners.

The application combines a structured CEFR-aligned curriculum with an
LLM-powered tutor that dynamically generates explanations, exercises,
tests, dialogues and other learning activities.

## Core idea

The system separates three responsibilities:

- **Curriculum** — defines what should be learned and in what order.
- **Learning Engine** — tracks where the learner is in the curriculum.
- **AI Tutor** — dynamically decides how to teach the current topic.

The LLM does not define the curriculum itself.

## MVP

The first version provides:

- Telegram interface;
- Serbian A1 curriculum;
- dynamic AI-generated learning activities;
- answer evaluation and feedback;
- persistent learner progress;
- PostgreSQL storage.

## Architecture

The MVP is implemented as a modular monolith.

```text
Telegram
    |
    v
Application
    |
    +-- Learning Engine
    +-- Curriculum
    +-- AI Tutor
    |      |
    |      v
    |   LLM Provider
    |
    +-- PostgreSQL