# Project Summary: Sin90's Chatbot Learning Journey

## Who this is for
Handoff context for another AI agent/assistant continuing to help this user. User goes by "Sin90" — B.Tech AIML student (3rd semester), aspiring AI/VR game developer. End goal: build a 1v1 shooting-game AI opponent in Unity. A mentor recommended building a rule-based chatbot first as a foundational exercise before tackling game AI.

## Project structure (local repo: `ai_chatbot`, on GitHub as `chauhansatyam024-debug/ai-chatbot`)
- `intents.json` — user-generated (via an AI tool called "emergent") dataset of `tag`/`patterns`/`responses` triples (greeting, goodbye, languages, fallback, etc.)
- `chatbot_v1.py`, `chatbot_v2.py`, `chatbot_v3.py`, `chatbot_v4.py` — iterative versions, each fixing bugs from the last
- `main.py`, `store.py`, `pdf_demo.py` — other files in the repo, not yet discussed in depth
- `unmatched.log` — logs user inputs that fail to match any intent (for reviewing gaps in training data)

## Technical approach built so far (rule-based, no external LLM API)
1. **Tokenization**: lowercase → strip punctuation via regex (`re.sub(r"[^\w\s]", " ", text)`) → `.split()`
2. **Simple suffix-based stemming**: manually strips `"ing"/"s"/"ed"/"es"` suffixes (with a length guard to avoid mangling short words) so word variants match
3. **Scoring**: moved from raw word-overlap count to **Jaccard similarity** (`intersection / union` of token sets) so pattern length doesn't unfairly bias matches
4. **Intent matching**: loops through every pattern in every intent, keeps the highest-scoring match
5. **Confidence threshold** (0.3): scores below this are rejected and treated as no-match, forcing fallback instead of a low-quality guess
6. **Fallback handling**: dedicated `"fallback"` tag in `intents.json` returns "I don't understand" style responses when nothing scores above threshold
7. **Matched-tracking + logging**: `getToken()` returns `(response, matched)` tuple; `main()` logs unmatched/low-confidence inputs to `unmatched.log` for later review

## Bugs already fixed (recurring theme: user is still building debugging intuition)
- Wrong regex escapes (`/w`/`/s` instead of `\w`/`\s`) silently wiped out most words
- Return statement mis-indented inside a loop, causing premature return after checking only the first pattern
- Wrong/typo'd JSON key names (`"response"` vs `"responses"`)
- Looping over a string (`for tag in intent["tag"]`) instead of comparing it directly — iterates characters, not the whole tag
- Using a triple-quoted string as an inline "comment" mid-function — this is real code, not a comment, and broke indentation/control flow
- `matched` flag not initialized before the loop, and not reset to `False` when confidence threshold rejects a match
- `file.write(a, b)` — `.write()` takes exactly one argument; needed string concatenation (`a + b`) instead of a comma

## Current stage: Stage 1 of a planned "gradual step-up" roadmap toward transformer-level understanding
User explicitly chose the **gradual step-up path** (not fine-tuning an existing LLM, not jumping straight to a tiny GPT-from-scratch) after being asked what "build a bot like Claude" actually meant to them. Agreed roadmap:

1. **Word embeddings** (current stage) — using `gensim` + pre-trained GloVe (`glove-wiki-gigaword-50`) to build intuition: words as vectors, similarity, the king–man+woman≈queen analogy. Just got a real vector output and inspected the raw GloVe text file format (`word` + 50 space-separated floats per line) to demystify what a "model" file actually contains.
2. **Neural network classifier on embeddings** — replace Jaccard scoring with averaged sentence embeddings fed into a small NN for intent classification
3. **RNN/LSTM** — introduce word-order/context sensitivity (bag-of-embeddings is still order-blind)
4. **Attention mechanism** — the pre-transformer key innovation
5. **Tiny Transformer** — toy-scale version of what actually powers models like Claude/GPT

## User's working style / preferences (useful for continuing to help them)
- Codes in Python via PyCharm on Fedora Linux, uses a `.venv`
- Learns best through: concrete code examples, line-by-line tracing/dry-runs, and analogies (e.g., 2D plot analogy for embeddings, "competition judge" analogy for scoring functions)
- Frequently pastes screenshots of PyCharm (code + terminal output/tracebacks) for debugging help — wants precise diagnosis of the exact bug and a targeted fix, not a rewrite of everything
- Prefers casual/informal phrasing, doesn't always use correct capitalization/grammar — respond in plain, direct language, no jargon without explanation
- Appreciates being told the "why" behind a fix, not just the "what"
- Wants concise, actionable explanations over abstract theory (per stated preferences)
- Has been introduced to and correctly used: git/GitHub basics (init, remote, push/pull, PAT tokens), Python scoping rules, `is` vs `==` for None checks, list comprehensions, regex basics

## Where to pick up
Next immediate step: run `most_similar()` and the king/queen analogy example with the loaded GloVe model, then move to Stage 2 (neural network classifier replacing Jaccard scoring) once embeddings intuition is solid.
