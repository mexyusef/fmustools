const R = require('ramda')
const { log } = console

class Functor {

  static of (value) {
    return new Functor(value)
  }
  
  constructor (value) {
    this.value = value
  }

  fmap (fn) {
    return new Functor(fn(this.value))
  }

}

Functor[ 'fantasy-land/of' ] = Functor.of
Functor.prototype[ 'fantasy-land/map' ] = Functor.prototype.fmap

const { map, compose, equals } = R

const id = x => x
const f = price => (price * 1.07) + 10
const g = total => 100 - total
const fg = compose(g, f)

const fa = Functor.of(90)
// Identity
log(equals(fa.fmap(id), Functor.of(id(90)))) // true
log(equals(fa.fmap(id), fa)) // true

// Composition
log(fa.fmap(f).fmap(g)) // Functor { value: -6.300000000000011 }
log(fa.fmap(fg)) // Functor { value: -6.300000000000011 }
log(map(compose(g, f), fa)) // Functor { value: -6.300000000000011 }
