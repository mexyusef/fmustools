const R = require('ramda');
// const { prop, compose, add } = R;
const { log } = console;

const compose = (f, g) => (x) => f(g(x));

const compose3 = (f, g, h) => (x) => f(g(h(x)));

const f = x => 'f(' + x
const g = x => 'g(' + x
const h = x => 'h(' + x
const x = 'x)))'

const a = compose(f, g, h) === f(g(h(x)))
const b = compose3(f, g, h) === f(g(h(x)))
log('compose(f, g, h) === f(g(h(x))) => true or false?', a)
log('compose3(f, g, h) === f(g(h(x))) => true or false?', b)
