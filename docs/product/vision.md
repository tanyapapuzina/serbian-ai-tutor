# Serbian AI Tutor

## Product vision

Serbian AI Tutor is a personalized Serbian language learning system
for Russian-speaking adults.

The product combines a structured CEFR-aligned curriculum with an
adaptive learning engine and an AI tutor.

The goal is not to create a generic chatbot that can speak Serbian.
The goal is to build a learning system that knows:

- what the learner should study;
- what the learner has already studied;
- which concepts the learner understands;
- which mistakes the learner repeatedly makes;
- what should be reviewed;
- what the learner is ready to study next.

The AI tutor provides explanations, feedback, exercises and dialogue
practice, while curriculum progression and student state are managed
by the learning system.

## Target user

Primary audience:

Russian-speaking adults learning Serbian from beginner level.

Typical use cases include:

- everyday communication in Serbia;
- shops, cafes and restaurants;
- transport;
- apartment and utilities;
- appointments;
- pharmacy and healthcare communication;
- documents and administrative situations;
- social communication;
- work and everyday life.

The first supported learning path will cover CEFR A1.

## Product principles

### 1. Communication before isolated grammar

Lessons are organized around communicative goals.

Grammar is introduced when it helps the learner accomplish a real
language task.

Example:

Instead of:

> Learn the accusative case.

The learning objective is:

> I can say where I am going and understand simple questions about
> direction.

The accusative case is one of the language tools required to achieve
that objective.

### 2. Structured curriculum

The LLM does not decide the entire learning program.

The curriculum defines:

- levels;
- modules;
- lessons;
- learning objectives;
- prerequisites;
- vocabulary;
- grammar concepts;
- assessments.

### 3. Personalized learning

Learners do not progress only by completing lessons.

The system tracks performance and uses it to determine what should be
practiced or reviewed.

### 4. Mistakes are learning data

Errors are classified and stored.

For example:

    Idem u apoteci.

may produce:

    error_type: case
    concept: accusative_direction
    expected: apoteku

Repeated errors influence future exercises and reviews.

### 5. AI where flexibility is useful

LLMs can be used for:

- explaining mistakes;
- generating constrained exercises;
- checking free-form answers;
- producing hints;
- conversation practice;
- adapting explanations;
- generating examples.

Deterministic application logic should handle:

- curriculum structure;
- progress;
- lesson prerequisites;
- attempts;
- scoring;
- mastery calculation;
- review scheduling.

### 6. Measurable learning

The system should be able to answer:

- What has the learner mastered?
- What is currently weak?
- What mistakes repeat?
- What should be reviewed?
- Is the learner ready for the next lesson?
- Is the learner ready to pass the level assessment?

## Initial scope

Version 1 focuses on:

- Russian-speaking learners;
- Serbian;
- CEFR A1;
- text-based learning;
- Telegram as the first user interface.

Future versions may add:

- A2 and higher levels;
- listening exercises;
- pronunciation evaluation;
- speech interaction;
- richer vocabulary training;
- additional interfaces.

## References

The initial methodology and curriculum research is based on:

- Common European Framework of Reference for Languages (CEFR)
- CEFR Companion Volume
- Naučimo srpski / Let's Learn Serbian, University of Novi Sad
- Učimo srpski, Azbukum Centre
- research on Serbian as a foreign language
- selected modern Serbian digital learning programs

Detailed methodological decisions are documented in:

    docs/pedagogy/methodology.md