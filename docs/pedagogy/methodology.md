# Learning Methodology

## 1. Purpose

Serbian AI Tutor uses a structured and adaptive approach to language learning.

The methodology combines:

- CEFR-aligned communicative objectives;
- explicit language instruction;
- guided and independent practice;
- retrieval practice;
- systematic error tracking;
- mastery-based progression;
- spaced review;
- AI-generated explanations and practice.

The system is designed specifically for Russian-speaking adults learning Serbian.

The LLM acts as a tutor inside the learning system. It does not define the curriculum or independently decide whether a learner has mastered a concept.

---

## 2. Learning objectives

Every lesson is built around a communicative objective.

Example:

    I can say where I am going.

Supporting language concepts may include:

    vocabulary:
      apoteka
      prodavnica
      škola
      restoran

    grammar:
      present tense of ići
      u + accusative for direction

The learner studies grammar because it enables communication, not as an isolated objective.

---

## 3. Lesson lifecycle

A lesson follows a controlled learning cycle.

### Stage 1: Context

Introduce a realistic situation.

Example:

    You are leaving home and your friend asks:
    "Gde ideš?"

The learner first understands why the language is useful.

### Stage 2: Input

Present examples of the target language.

Example:

    Idem u apoteku.
    Idem u prodavnicu.
    Idem u restoran.

The learner observes the pattern before being expected to produce it independently.

### Stage 3: Explanation

Explain the relevant vocabulary, grammar or language pattern.

For Russian-speaking learners, explanations may use Russian when it improves understanding.

Cross-language comparisons should be used carefully.

Similarity between Russian and Serbian can accelerate learning but can also produce systematic transfer errors.

### Stage 4: Recognition practice

The learner identifies correct forms or meanings.

Exercise types may include:

- multiple choice;
- matching;
- selecting the correct form;
- identifying an error.

### Stage 5: Controlled production

The learner produces language with significant constraints.

Examples:

    Idem u ______. (apoteka)

    Choose the correct form:
    apoteka / apoteku / apoteci

### Stage 6: Independent production

Constraints are gradually removed.

Examples:

    Translate:
    "Я иду в аптеку."

    Answer:
    "Gde ideš?"

### Stage 7: Communicative task

The learner uses the concept in a realistic interaction.

Example:

    Tutor: Gde ideš?
    Learner: Idem u apoteku.
    Tutor: Šta želiš da kupiš?

The objective is successful communication, not only grammatical transformation.

### Stage 8: Assessment

The learner completes several tasks without immediate instructional help.

Assessment should contain more than one exercise and preferably more than one exercise type.

### Stage 9: Mastery update

The learning engine updates the learner's mastery of the concepts involved in the lesson.

Progress is based on demonstrated performance rather than lesson completion alone.

---

## 4. Exercise progression

Exercises generally progress from lower to higher production difficulty:

    recognition
        ↓
    selection
        ↓
    completion
        ↓
    constrained production
        ↓
    translation
        ↓
    free production
        ↓
    dialogue / real-life task

Not every lesson must contain every exercise type.

The learning engine may shorten or extend practice based on learner performance.

---

## 5. Retrieval practice

Previously learned information should regularly be recalled without simply showing the answer first.

Example:

Instead of repeatedly showing:

    kuća = дом

the system may later ask:

    Kako se kaže "дом" na srpskom?

or use the word inside another task.

Retrieval opportunities should be mixed into later lessons.

---

## 6. Spaced review

A concept should not be considered permanently learned after one successful lesson.

Previously learned concepts are scheduled for later review.

The review schedule should consider:

- current mastery;
- previous mistakes;
- number of successful attempts;
- time since last practice;
- difficulty of previous retrieval;
- recent failures.

The first implementation may use deterministic scheduling rules.

A more sophisticated adaptive scheduling model can be introduced later if product data justifies it.

---

## 7. Error-driven learning

Mistakes are stored as structured learning data.

Example learner answer:

    Idem u apoteci.

Possible structured error:

    category: grammar
    error_type: case
    concept: accusative_direction
    observed: apoteci
    expected: apoteku

An error should influence future practice.

Repeated errors may:

- trigger additional exercises;
- reduce concept mastery;
- schedule an earlier review;
- change the type of exercise;
- request a different explanation.

The system should distinguish between a single mistake and a recurring misconception.

---

## 8. Mastery

Mastery represents the system's estimate of how reliably a learner can use a concept.

Examples of concepts:

    biti_present
    imati_present
    accusative_direction
    locative_location
    past_tense
    future_tense
    food_vocabulary
    numbers_1_100

Mastery should not be directly assigned by an LLM.

It should be calculated from observable learning events such as:

- correct and incorrect answers;
- exercise difficulty;
- amount of assistance;
- number of attempts;
- recency;
- successful delayed retrieval;
- performance in communicative tasks.

The initial mastery algorithm should be simple and explainable.

It can later be replaced or supplemented by a statistical or ML model if sufficient learning data becomes available.

---

## 9. Feedback

Feedback should be useful but proportional to the error.

For a small error, the tutor should avoid producing an unnecessarily long grammar lecture.

Example:

Learner:

    Idem u apoteci.

Tutor:

    Почти правильно: Idem u apoteku.

    Когда говорим о направлении "куда?", после "u" здесь нужен
    винительный падеж:

    apoteka → apoteku

    Попробуй ещё раз:
    "Я иду в аптеку."

For repeated errors, feedback may become more explicit and include contrastive examples.

---

## 10. Hints

The system should prefer progressive hints over immediately revealing the answer.

Possible hint levels:

    Level 0: no hint
    Level 1: conceptual hint
    Level 2: stronger structural hint
    Level 3: partial answer
    Level 4: full explanation

Using stronger hints should affect mastery calculations differently from solving a task independently.

---

## 11. Russian-speaking learner adaptation

The curriculum is designed specifically for Russian-speaking learners.

Russian can be used for:

- explanations;
- translation exercises;
- contrastive examples;
- clarification of difficult grammar.

However, Serbian exposure should increase progressively.

The system should explicitly track errors caused by cross-language transfer where useful.

Examples may include:

- similar words with different meanings;
- incorrect case transfer;
- Serbian clitic placement;
- verb forms that appear familiar but behave differently;
- pronunciation and stress differences.

These error categories must be validated against Serbian language teaching sources before becoming part of the production curriculum.

---

## 12. Role of the AI tutor

The AI tutor is responsible for flexible language tasks.

Appropriate uses include:

- explaining a learner's mistake;
- generating examples;
- generating exercises under curriculum constraints;
- evaluating free-form answers;
- generating hints;
- conducting dialogues;
- adapting explanation style;
- producing additional practice for known weaknesses.

The AI tutor receives relevant learner state and curriculum constraints from the application.

---

## 13. Responsibilities outside the LLM

The following should remain application-controlled:

- curriculum structure;
- lesson prerequisites;
- learner progress;
- concept definitions;
- attempt history;
- mastery calculation;
- review scheduling;
- assessment rules;
- persistence;
- authorization;
- usage limits.

This separation prevents the LLM from becoming the application's database and business logic.

---

## 14. AI reliability

LLM output cannot automatically be treated as correct educational content.

AI-generated educational content should be constrained by:

- lesson objectives;
- known concepts;
- expected proficiency level;
- approved curriculum content;
- structured output schemas where appropriate.

Important language rules and canonical examples should come from validated curriculum data rather than being regenerated on every request.

---

## 15. AI evaluation

Traditional software tests are not sufficient for AI tutor behavior.

The project will maintain an evaluation dataset containing representative learning situations.

Example:

    learner_input: "Idem u apoteci."
    expected_error_type: "case"
    expected_concept: "accusative_direction"
    expected_correction: "Idem u apoteku."

Evaluation dimensions may include:

- correction accuracy;
- error classification;
- explanation accuracy;
- CEFR-level appropriateness;
- instruction following;
- unnecessary verbosity;
- hallucinated grammar rules;
- exercise validity.

Prompt or model changes should be evaluated against this dataset before production deployment.

---

## 16. Assessment model

Assessment operates at multiple levels.

### Exercise assessment

Was the individual answer acceptable?

### Concept assessment

Can the learner reliably use a particular concept?

### Lesson assessment

Were the lesson objectives achieved?

### Module assessment

Can the learner combine concepts from several lessons?

### Level assessment

Can the learner perform the communication activities expected at the target CEFR level?

Level assessment should cover multiple language activities rather than being a single grammar test.

---

## 17. Curriculum, teaching and assessment alignment

For every important learning objective, the system should maintain alignment between:

    objective
        ↓
    instruction
        ↓
    practice
        ↓
    assessment

The system should not assess language that has never been taught without explicitly marking it as diagnostic assessment.

Likewise, completing exercises should not count as evidence of mastery if those exercises do not measure the stated learning objective.

---

## 18. Methodology evolution

The methodology is versioned with the product.

Changes should be based on:

- Serbian language teaching research;
- CEFR guidance;
- evaluation results;
- learner performance data;
- observed error patterns;
- product experiments.

Major methodology decisions should be documented rather than silently encoded in prompts.