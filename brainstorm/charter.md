# Brainstorming Department — charter

Owner
- Meteorologist :: Brainstorming - Brainstorming

Purpose
- Capture early idea fragments, loose riffs, and experiment notes
  before refinement by Narrative, Systems, or other departments.

Inputs
- Free-form notes, sketches, audio dumps, mail prompts.

Outputs
- idea_pad_*.md
- brain_dump_*.md
- sketch_refs.md

Gates
- None strict; tag by theme and route to the correct department.

Directory
- /brainstorm/

Templates
- /ops/templates/brainstorm/idea_pad_template.md
- /ops/templates/brainstorm/brain_dump_template.md

Mail handoff
- Queue file: /ops/handoffs/brainstorm_queue.md
- Escalation tags: [narrative], [systems], [adversary], [qa],
  [publishing], [auth_research].

Procedure
1) Create a new idea or dump from the templates.
2) Add tags and a one-line summary.
3) Append to /ops/handoffs/brainstorm_queue.md for routing by Mail.
