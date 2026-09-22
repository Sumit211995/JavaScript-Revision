/**
 * Lesson 1 exercises — run: node js-interview/exercises/01-values-types-declarations.js
 * Fill in ANSWERS and implementations. Do not peek at 01-solutions.js until you try.
 */

// --- Part A: Predict output (write your answer as a string or number) ---

// Clear these and predict before running; compare with 01-solutions.js
const partA = {
  q1_typeofNull: "object",
  q2_typeofArray: "object",
  q3_constReassign: "error",
  q4_varLoop: [3],
  q5_truthyEmptyArray: true,
};

// --- Part B: Implement (used by self-check below) ---

/** Return primitive type name using typeof (for null return "null"). */
function typeOfValue(value) {
  if (value === null) return "null";
  return typeof value;
}

/** Swap two variables without a third variable (numbers or strings). */
function swap(a, b) {
  return [b, a];
}

/** Return a new array; do not mutate `items`. */
function appendItem(items, item) {
  return [...items, item];
}

/** `mode`: "var" | "let" — simulate loop variable after loop ends (return final i). */
function loopFinalIndex(mode) {
  if (mode === "var") {
    for (var i = 0; i < 3; i++) {
      // empty
    }
    return i;
  }
  if (mode === "let") {
    for (let j = 0; j < 3; j++) {
      // empty
    }
    return typeof j === "undefined" ? "undefined" : j;
  }
  throw new Error("unknown mode");
}

// --- Self-check (do not edit below unless fixing the checker) ---

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function runChecks() {
  // Part A — fill these in yourself; checker uses solutions for Part B only
  assert(partA.q1_typeofNull === "object", "Part A q1: typeof null is 'object' (JS quirk)");
  assert(partA.q2_typeofArray === "object", "Part A q2: typeof [] is 'object'");
  assert(partA.q3_constReassign === "error", "Part A q3: reassigning const throws");
  assert(
    JSON.stringify(partA.q4_varLoop) === JSON.stringify([3]),
    "Part A q4: var i leaks — final i is 3"
  );
  assert(partA.q5_truthyEmptyArray === true, "Part A q5: [] is truthy");

  assert(typeOfValue(null) === "null", "typeOfValue(null)");
  assert(typeOfValue([]) === "object", "typeOfValue([])");
  assert(typeOfValue(undefined) === "undefined", "typeOfValue(undefined)");

  assert(JSON.stringify(swap(1, 2)) === JSON.stringify([2, 1]), "swap");
  const base = [1, 2];
  const next = appendItem(base, 3);
  assert(JSON.stringify(base) === JSON.stringify([1, 2]), "appendItem must not mutate");
  assert(JSON.stringify(next) === JSON.stringify([1, 2, 3]), "appendItem result");

  assert(loopFinalIndex("var") === 3, "var loop final index");
  assert(loopFinalIndex("let") === "undefined", "let loop — j not in outer scope");

  console.log("Lesson 1 exercises: all checks passed.");
}

runChecks();
