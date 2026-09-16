# System Design

## 1. Overview

Serbian AI Tutor is a Telegram-based learning application for
Russian-speaking learners of Serbian.

The system combines:

- a versioned Serbian curriculum;
- persistent learner progress;
- a learning engine;
- an AI tutor powered by an LLM;
- dynamically generated learning activities.

The curriculum defines what should be learned.

The learning engine determines where the learner currently is.

The AI tutor determines how to teach the current topic.

---

## 2. High-level architecture

    Telegram User
          |
          v
    Telegram Bot
          |
          v
    Application
          |
          +---- Learning Engine
          |
          +---- Curriculum
          |
          +---- AI Tutor
          |        |
          |        v
          |    LLM Provider
          |
          +---- Persistence
                   |
                   v
               PostgreSQL

The first version is implemented as a modular monolith.

Components are separated logically inside one application rather
than deployed as independent microservices.

---

## 3. Telegram interface

Telegram is the first user interface.

The bot is responsible for:

- receiving commands and messages;
- displaying lessons and exercises;
- receiving learner answers;
- displaying feedback;
- navigation between learning activities.

Telegram-specific logic should remain separate from learning logic.

The learning engine should not depend directly on Telegram.

This allows additional interfaces to be added later.

---

## 4. Curriculum

The curriculum is stored as version-controlled application data.

Initial curriculum:

    curriculum/a1/curriculum.yaml

The curriculum defines:

- CEFR level;
- modules;
- topics;
- topic order.

It intentionally does not contain complete predefined lessons.

The curriculum acts as a learning map.

The AI tutor uses the current topic and learner context to dynamically
create appropriate teaching activities.

The LLM must not independently redefine curriculum order.

---

## 5. Learning Engine

The Learning Engine coordinates the learner's progression through
the curriculum.

Responsibilities include:

- identifying the current topic;
- retrieving previous progress;
- starting and finishing learning sessions;
- requesting activities from the AI Tutor;
- processing assessment results;
- deciding when to continue or move forward.

The first MVP will use simple and deterministic progression rules.

More advanced adaptive behavior can be added later without changing
the curriculum model.

---

## 6. AI Tutor

The AI Tutor converts curriculum topics into actual learning
interactions.

It may dynamically generate:

- explanations;
- examples;
- exercises;
- translations;
- dictation tasks;
- short tests;
- dialogues;
- revision activities;
- feedback.

The AI Tutor receives structured context from the application.

Example:

    learner_language: ru
    target_language: sr
    level: A1
    current_topic: accusative_direction
    completed_topics:
      - places
      - movement_verbs
      - accusative_intro

The AI Tutor should teach within these constraints.

---

## 7. LLM Provider

LLM integration is accessed through an application-level provider
interface.

Application and learning logic should not depend directly on one
specific LLM vendor.

Conceptually:

    AI Tutor
       |
       v
    LLM Provider
       |
       +---- OpenRouter
       |
       +---- OpenAI (future)
       |
       +---- other providers (future)

The MVP may initially implement only one provider.

---

## 8. Persistence

PostgreSQL is the primary application database.

The database stores persistent user and learning state.

Initial entities are expected to include:

    users
    learning_progress
    learning_sessions
    attempts

Curriculum definitions remain in version-controlled files rather than
being duplicated as editable database content in the MVP.

---

## 9. Learning session

A learning session represents one continuous study interaction.

Example lifecycle:

    user starts learning
          |
          v
    load learner progress
          |
          v
    resolve current curriculum topic
          |
          v
    create learning session
          |
          v
    AI Tutor generates activity
          |
          v
    learner responds
          |
          v
    evaluate response
          |
          +---- continue topic
          |
          +---- finish topic
          |
          v
    save progress

A session may contain multiple generated activities.

---

## 10. Application boundaries

The application should maintain clear module boundaries.

Suggested structure:

    src/
    ├── bot/
    ├── curriculum/
    ├── learning/
    ├── tutor/
    ├── llm/
    ├── users/
    ├── db/
    ├── core/
    └── main.py

Responsibilities:

    bot
        Telegram-specific handlers and presentation.

    curriculum
        Curriculum loading and navigation.

    learning
        Learning sessions, progress and orchestration.

    tutor
        AI teaching behavior and prompt construction.

    llm
        LLM provider abstraction and implementations.

    users
        User-related domain logic.

    db
        Database models, repositories and migrations integration.

    core
        Configuration, logging and shared infrastructure.

---

## 11. Configuration

Secrets and environment-specific configuration must not be committed
to Git.

Configuration should be provided through environment variables.

Examples:

    TELEGRAM_BOT_TOKEN
    DATABASE_URL
    OPENROUTER_API_KEY
    LLM_MODEL

Local development may use a `.env` file.

A `.env.example` file should document required configuration without
containing real secrets.

---

## 12. Reliability

The MVP should include basic production reliability mechanisms:

- validated configuration;
- database migrations;
- transaction boundaries;
- LLM request timeouts;
- controlled retries;
- structured LLM responses where required;
- duplicate Telegram update protection where necessary;
- exception handling;
- structured logging;
- health checks.

External service failures should not corrupt learner progress.

---

## 13. Observability

The application should produce structured logs.

Important operations should include enough context to trace a request
through the system.

Examples:

    telegram_update_id
    user_id
    learning_session_id
    topic_id
    llm_provider
    llm_model
    latency
    result

Sensitive learner content should not be logged unnecessarily.

---

## 14. Testing

The project should contain several testing layers.

Unit tests:

- curriculum loading;
- curriculum navigation;
- progression rules;
- deterministic assessment logic.

Integration tests:

- database repositories;
- learning session persistence.

AI evaluations:

- generated exercise validity;
- correction quality;
- instruction following;
- Russian-speaker adaptation.

External APIs should not be required for normal unit test execution.

---

## 15. Deployment

The application should be containerized with Docker.

The initial deployment consists of:

    application container
            |
            v
        PostgreSQL

Additional infrastructure should only be introduced when required by
an actual product need.

---

## 16. MVP boundaries

The first MVP intentionally excludes:

- microservices;
- Kubernetes;
- Kafka;
- complex distributed workflows;
- ML-based mastery prediction;
- voice recognition;
- pronunciation scoring;
- multi-agent orchestration.

These features may be introduced later if product requirements justify
their complexity.

The MVP priority is a reliable end-to-end learning experience.