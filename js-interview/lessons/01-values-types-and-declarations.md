# Lesson 1 — Values, types, `let` / `const` / `var`

**Goal:** Answer output-based and “what’s the difference?” questions in 30–60 second sound bites.  
**Time:** One evening (~45 min read + exercises).  
**Your repo notes:** `closure.js` (top) and `function.js` (hoisting section).

---

## 1. Two kinds of values

| Kind | Examples | Stored as |
|------|----------|-----------|
| **Primitive** | `number`, `string`, `boolean`, `null`, `undefined`, `bigint`, `symbol` | Value directly |
| **Reference** | `object`, `array`, `function` | Reference to heap memory |

```js
let a = { x: 1 };
let b = a;
b.x = 99;
console.log(a.x); // 99 — same object
```

Primitives are copied by value:

```js
let x = 10;
let y = x;
y = 20;
console.log(x); // 10
```

**Interview line:** “Objects and arrays are compared and passed by reference; primitives by value.”

---

## 2. `typeof` (know the traps)

```js
typeof 42;           // "number"
typeof "hi";         // "string"
typeof true;         // "boolean"
typeof undefined;    // "undefined"
typeof null;         // "object"  ← classic trap
typeof {};           // "object"
typeof [];           // "object"
typeof function(){}; // "function"
```

**Interview line:** “`typeof null` is `'object'` — a long-standing JS bug; use `value === null` instead.”

---

## 3. `var` vs `let` vs `const`

| | `var` | `let` | `const` |
|---|--------|--------|---------|
| Scope | Function (or global) | Block | Block |
| Hoisted | Yes (initialized `undefined`) | Yes (TDZ until line runs) | Yes (TDZ) |
| Re-declare same scope | Allowed | Error | Error |
| Reassign | Yes | Yes | No (binding); object contents can change |

**Temporal Dead Zone (TDZ):** Accessing `let`/`const` before their line runs → `ReferenceError` (not `undefined` like `var`).

```js
console.log(v); // undefined (hoisted)
var v = 1;

console.log(l); // ReferenceError
let l = 2;
```

**Block scope + loops** (you already saw this in `closure.js`):

```js
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i), 0);
// 3, 3, 3

for (let j = 0; j < 3; j++) setTimeout(() => console.log(j), 0);
// 0, 1, 2
```

**Interview line:** “In interviews I default to `const`, use `let` when I reassign, and avoid `var` in new code because of function scope and loop closure bugs.”

---

## 4. Coercion preview (Lesson 2 goes deeper)

```js
"5" + 1;   // "51"  (string wins)
"5" - 1;   // 4     (number)
Boolean(0);          // false
Boolean("");         // false
Boolean("hello");    // true
Boolean([]);         // true  ← empty array is truthy!
```

---

## 5. Quick interview Q&A

1. **Difference between `null` and `undefined`?**  
   `undefined` = missing / not assigned; `null` = intentional empty value. `typeof` differs (`undefined` vs `object` for null).

2. **Can you change a `const` object?**  
   Yes — you cannot reassign the binding, but `obj.prop = 1` is fine.

3. **What is hoisting?**  
   Declarations are processed before execution. `var` functions are fully hoisted; `let`/`const` are hoisted but in TDZ until initialized.

4. **Is JavaScript pass-by-reference?**  
   Pass-by-value of the reference — reassigning a parameter does not change the outer variable; mutating the object does.

5. **Truthy / falsy?**  
   Falsy: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`. Everything else is truthy (including `[]` and `{}`).

---

## 6. Before Lesson 2

- [ ] Run: `node js-interview/exercises/01-values-types-declarations.js` — all checks pass.
- [ ] Without looking, explain the `var` vs `let` loop + `setTimeout` output.
- [ ] Say out loud: one project bug you fixed that involved scope or `const` (Warranty auth / Zustand is a good story).

**Next:** [Lesson 2 — Operators, coercion, `==` vs `===`](02-operators-and-coercion.md) (file added when you finish Lesson 1).
