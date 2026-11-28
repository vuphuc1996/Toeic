# Part 2 Distractor-Resistance Evidence Review — TOEIC Dictionary v2.95.82

**Scope:** 16 existing Listening Part 2 items mapped to one existing criterion. No new questions or answer options were authored.

## Inclusion rule

An item is included only when (1) its canonical spoken prompt contains a whole-word lexical cue, (2) one non-answer option repeats that cue, (3) that option is a real canonical choice and is not the answer-key index, (4) the option fails the communicative task asked by the prompt, and (5) the resource is not marked reserve-pending-independent-review.

## Evidence inventory

| Resource ID | Prompt | Repeated cue | Incorrect choice | Why the choice does not answer the prompt |
|---|---|---|---|---|
| `part2-access-code` | I haven't received the access code yet. | `code` | The code has eight characters. | Describes code length rather than resolving the missing-code problem. |
| `part2-airport-taxi` | Should I book a taxi to the airport? | `taxi` | The taxi company is nearby. | States that a taxi company is nearby instead of answering whether to book one. |
| `part2-business-trip` | Do you know whether Mr. Chen has returned from his business trip? | `business` | The business trip was approved. | States that the trip was approved rather than whether Mr. Chen has returned. |
| `part2-contract-review` | Have you finished reviewing the contract? | `contract` | The contract covers three years. | Describes the contract term rather than confirming whether the review is complete. |
| `part2-database-owner` | Who is responsible for updating the client database? | `database` | The database was updated last week. | States when the database was updated rather than identifying who is responsible. |
| `part2-first-shuttle` | What time does the first shuttle leave for the airport? | `shuttle` | The shuttle is fully booked. | States availability rather than giving the first departure time. |
| `part2-inspection-duration` | How long does the equipment inspection usually take? | `equipment` | The equipment is in storage. | States where equipment is stored rather than how long the inspection takes. |
| `part2-meeting-room` | Has the meeting been moved to Conference Room C? | `meeting` | The meeting lasted about an hour. | States the meeting's duration rather than confirming whether it moved. |
| `part2-printer-arrival` | When will the replacement printer arrive? | `printer` | The printer is out of paper. | States the printer's paper status rather than its arrival time. |
| `part2-product-demo` | Where was the product demonstration held? | `demonstration` | The demonstration lasted an hour. | States the event's duration rather than where it was held. |
| `part2-registration-extension` | Would it be possible to extend the registration deadline? | `deadline` | The deadline was printed in blue. | Describes the printed deadline rather than answering whether it can be extended. |
| `part2-seat-preference` | Would you prefer the window seat or an aisle seat? | `window` | The window is being cleaned. | Uses window in a cleaning context rather than selecting a window or aisle seat. |
| `part2-wrong-branch` | Why was the shipment sent to the wrong branch? | `branch` | The branch closes at six. | States branch opening hours rather than explaining why the shipment was misrouted. |
| `part2-website-update` | Why is the website being updated tonight? | `website` | The website address has changed. | Describes an address change rather than the reason for tonight's update. |
| `part2-supplier-samples` | Didn't the supplier promise to deliver the samples today? | `samples` | The samples are stored in the laboratory. | Describes storage location rather than responding to the supplier's promised delivery. |
| `part2-visitor-badge` | Where can I pick up the visitor badge? | `visitor` | The visitor arrived yesterday. | States when the visitor arrived rather than where the badge can be collected. |

## Audit controls

- 16 distinct stable question keys are mapped; unique overall bank question IDs remain 638 because these items already existed under the Part 2 natural-response criterion.
- All 16 resources are non-reserve. No Listening reserve item is included or promoted.
- The canonical answer index is read from the source bank; the selected distractorChoiceIndex must differ from it.
- The audit compares promptQuote to the spoken segments, distractorQuote to the selected canonical choice, and requires the same lexicalCue in both texts plus a non-empty responseMismatch.
- The criterion threshold remains **10 unique mapped items at 80% latest accuracy**. Sixteen is available mapping inventory, not a learner result and not a psychometric calibration claim.

## Known limitations

- This is a criterion-specific source audit, not independent ETS review or psychometric item calibration.
- A repeated word alone is not enough; the mismatch rationale is required and is checked for presence, but not semantically auto-graded.
- Four other TOEIC criteria remain uninstrumented. Part 1, Part 4, Part 6 and Part 7 candidates were not auto-mapped because the inspected inventory did not provide enough independent evidence to justify adding them in this batch.
