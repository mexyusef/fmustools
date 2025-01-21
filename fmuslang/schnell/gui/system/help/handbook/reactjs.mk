--% getting started
https://reactjs.org/docs/getting-started.html
--#

--% main concepts: hello
--#

--% main concepts: jsx
--#

--% main concepts: rendering elements
--#

--% main concepts: components and props
--#

--% main concepts: state and lifecycle
https://reactjs.org/docs/state-and-lifecycle.html
--#

--% main concepts: handling events
--#

--% main concepts: conditional rendering
--#

--% main concepts: lists and keys
--#

--% main concepts: forms
--#

--% main concepts: lifting state up
--#

--% main concepts: composition vs inheritance
--#

--% main concepts: thinking in react
--#

--% advanced: accessibility
--#

--% advanced: code-splitting
https://reactjs.org/docs/code-splitting.html

## bundling

### versi original
App:

// app.js
import { add } from './math.js';

console.log(add(16, 26)); // 42
// math.js
export function add(a, b) {
  return a + b;
}

### versi bundle
Bundle:

function add(a, b) {
  return a + b;
}

console.log(add(16, 26)); // 42

To avoid winding up with a large bundle, it’s good to get ahead of the problem and start “splitting” your bundle. Code-Splitting is a feature supported by bundlers like Webpack, Rollup and Browserify (via factor-bundle) which can create multiple bundles that can be dynamically loaded at runtime.

Code-splitting your app can help you “lazy-load” just the things that are currently needed by the user, which can dramatically improve the performance of your app. While you haven’t reduced the overall amount of code in your app, you’ve avoided loading code that the user may never need, and reduced the amount of code needed during the initial load.

## import()

The best way to introduce code-splitting into your app is through the dynamic import() syntax.

### Before:
import { add } from './math';

console.log(add(16, 26));

### After:
import("./math").then(math => {
  console.log(math.add(16, 26));
});

--#

--% advanced: context
--#

--% advanced: error boundaries
--#

--% advanced: forwarding refs
--#

--% advanced: fragments
--#

--% advanced: hoc
--#

--% advanced: 3rd party libraries integration
--#

--% advanced: jsx in depth
--#

--% advanced: optimizing performance
--#

--% advanced: portals
--#

--% advanced: profilers
--#

--% advanced: react without es6
--#

--% advanced: react wihout jsx
--#

--% advanced: reconciliation
--#

--% advanced: refs and the dom
--#

--% advanced: render props
--#

--% advanced: static type checking
--#

--% advanced: strict mode
--#

--% advanced: typechecking with proptypes
--#

--% advanced: uncontrolled components
--#

--% advanced: web components
https://reactjs.org/docs/web-components.html
--#

--% hooks
https://reactjs.org/docs/hooks-intro.html
--#

--% testing
https://reactjs.org/docs/testing.html
--#

--% faq
https://reactjs.org/docs/faq-ajax.html
--#

--% contributing
https://reactjs.org/docs/how-to-contribute.html
--#

--% api reference
https://reactjs.org/docs/react-api.html
--#
