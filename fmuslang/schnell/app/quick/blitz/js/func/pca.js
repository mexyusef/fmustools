const R = require('ramda');
const { prop, compose, add } = R;
const { log } = console;

const user1 = { name: 'Michael', email: 'm@m.com' };

const greeting = compose(R.concat('Hello '), prop('name'));

log(greeting({ name: 'World' }));
