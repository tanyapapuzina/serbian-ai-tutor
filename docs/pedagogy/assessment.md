# Assessment Model

## 1. Purpose

Assessment is responsible for converting learner interactions into
structured evidence about learning progress.

The system should not treat lesson completion as proof of knowledge.

Instead, it records observable learner performance and uses that
evidence to update concept mastery and determine future learning actions.

---

## 2. Assessment hierarchy

Assessment operates at several levels:

    Attempt
       ↓
    Exercise
       ↓
    Concept
       ↓
    Lesson
       ↓
    Module
       ↓
    CEFR Level

Each level answers a different question.

### Attempt

What happened when the learner tried to answer?

### Exercise

Was the task completed successfully?

### Concept

What does the attempt tell us about a specific language skill?

### Lesson

Were the learning objectives of the lesson demonstrated?

### Module

Can the learner combine concepts across several lessons?

### CEFR Level

Can the learner perform the communication activities expected
at the target level?

---

## 3. Attempt as the atomic learning event

Every meaningful learner answer should produce an attempt record.

An attempt should contain enough information to reconstruct what happened.

Conceptual example:

    attempt_id
    learner_id
    exercise_id
    lesson_id
    submitted_answer
    normalized_answer
    correctness
    score
    hint_level
    attempt_number
    response_time
    evaluated_by
    evaluation_version
    created_at

An attempt is historical evidence.

Existing attempts should not be overwritten when the learner tries
the exercise again.

A new attempt should be recorded instead.

---

## 4. Evaluation types

Not every exercise should be evaluated by an LLM.

The system should use the simplest reliable evaluator for each task.

### Deterministic evaluation

Use application code when the expected answer can be defined reliably.

Examples:

- multiple choice;
- matching;
- vocabulary selection;
- exact grammatical forms;
- structured fill-in-the-blank tasks.

### Rule-based evaluation

Use language-specific normalization or validation when several known
forms should be accepted.

Examples may include:

- capitalization differences;
- optional punctuation;
- known equivalent answers;
- Latin and Cyrillic variants where allowed.

### LLM-assisted evaluation

Use an LLM when correctness depends on meaning or language quality
that cannot be represented by a simple answer key.

Examples:

- free-form sentences;
- short written responses;
- dialogue responses;
- open translation tasks.

The LLM should return structured evaluation data rather than only
natural-language feedback.

---

## 5. Structured evaluation result

Evaluation should produce a machine-readable result.

Conceptual example:

    {
      "is_acceptable": false,
      "score": 0.4,
      "errors": [
        {
          "category": "grammar",
          "error_type": "case",
          "concept_id": "accusative_direction",
          "observed": "apoteci",
          "expected": "apoteku"
        }
      ],
      "feedback": "..."
    }

The exact schema will be defined in application code and versioned.

Free-form LLM text must not be the only source of assessment state.

---

## 6. Partial correctness

Language answers are not always simply correct or incorrect.

Example:

    Prompt:
    "Я завтра иду в аптеку."

    Learner:
    "Sutra idem u apoteci."

The learner may correctly demonstrate:

- vocabulary;
- word order;
- present tense usage;

while failing:

- accusative for direction.

Assessment should preserve this distinction where useful.

One answer may therefore provide evidence for several concepts.

---

## 7. Concept evidence

An attempt can produce positive or negative evidence for one or more
concepts.

Example:

    concept: ici_present
    evidence: positive

    concept: accusative_direction
    evidence: negative

This allows the learning engine to update concepts independently.

The system should avoid reducing an entire sentence to a single
binary score when more useful evidence can be extracted reliably.

---

## 8. Assistance-aware assessment

A correct answer after significant assistance should not provide the
same mastery evidence as an independent correct answer.

Relevant signals include:

- hint level;
- number of attempts;
- whether the correct answer was previously revealed;
- exercise difficulty;
- whether the task was immediate practice or delayed retrieval.

Example:

    correct without hint
        stronger positive evidence

    correct after conceptual hint
        positive evidence

    correct after partial answer
        weak positive evidence

    correct after full answer was shown
        little or no mastery evidence

The exact weights are an implementation decision and should be tested
rather than assumed.

---

## 9. Error taxonomy

Errors should use stable categories where possible.

Initial top-level categories may include:

    grammar
    vocabulary
    spelling
    word_order
    comprehension
    task_completion

More specific error types should reference curriculum concepts.

Example:

    category: grammar
    error_type: wrong_case
    concept_id: accusative_direction

Error categories should evolve from validated curriculum rules and
observed learner data.

They should not be invented dynamically by the LLM on every request.

---

## 10. Assessment modes

The system distinguishes between different assessment contexts.

### Practice

The learner may receive immediate feedback and hints.

### Checkpoint

The learner completes a short assessment covering several recent
concepts with reduced assistance.

### Diagnostic

The system estimates existing knowledge before or outside normal
curriculum progression.

### Level assessment

The learner demonstrates integrated language ability across the
target CEFR level.

Assessment mode affects how evidence is interpreted.

A successful independent checkpoint should generally provide stronger
evidence than a heavily assisted practice exercise.

---

## 11. Lesson completion

A lesson is not completed simply because all screens or exercises
were viewed.

Completion should require sufficient evidence for the lesson's
learning objectives.

Possible outcomes include:

    advance
    continue_practice
    remediate
    schedule_review

The exact decision policy belongs to the learning engine.

---

## 12. Evaluation provenance

Every automated evaluation should record how it was produced.

Relevant metadata may include:

    evaluator_type
    evaluator_version
    model_provider
    model_name
    prompt_version
    rubric_version

This is especially important for LLM-assisted evaluation.

If evaluation behavior changes after a model or prompt update, the
system must be able to identify which version produced historical
results.

---

## 13. Reliability

LLM-assisted assessment should be treated as a fallible component.

Reliability mechanisms may include:

- structured output validation;
- explicit rubrics;
- retries for invalid responses;
- confidence or ambiguity handling;
- deterministic checks where possible;
- regression evaluation datasets;
- manual review during development.

The system should fail safely when an evaluation cannot be trusted.

An invalid LLM response must not silently update learner mastery.

---

## 14. Idempotency

Processing the same learner submission more than once should not
accidentally create duplicate learning evidence.

Submission processing should use a stable identifier that allows the
backend to recognize duplicate requests.

This becomes important when:

- Telegram retries a request;
- a network timeout occurs;
- a background worker retries a job;
- the client sends the same request twice.

Idempotency requirements will be defined in the backend architecture.

---

## 15. Observability

Assessment behavior should be measurable in production.

Useful metrics may include:

- evaluation latency;
- evaluation failures;
- LLM structured-output failures;
- retry rate;
- deterministic vs LLM evaluation ratio;
- average evaluation cost;
- disagreement rates in evaluation tests;
- error category frequency.

Logs should allow an individual assessment request to be traced
without exposing unnecessary learner data.

---

## 16. Separation of responsibilities

The assessment system determines what evidence an interaction produced.

The mastery system determines how that evidence changes the estimated
knowledge state.

The curriculum determines what concepts and objectives exist.

The learning engine determines what the learner should do next.

These responsibilities should remain separate even if the first
implementation runs inside one backend application.