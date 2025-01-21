embedded_pattern_languages_header = """  
  | pattern_anti_corruption
  | pattern_bloc
  | pattern_circuit_breaker
  | pattern_concurrency
  | pattern_cqrs
  | pattern_dry
  | pattern_event_sourcing
  | pattern_fluent
  | pattern_listener
  | pattern_observable
  | pattern_pubsub
  | pattern_reference
  | pattern_saga
  | pattern_sharding
  | pattern_solid
  | pattern_strangler
  | pattern_static_content
  | pattern_taskqueue
  | pattern_throttling  
  | pattern_visitor

  | pattern_behavioral
  | pattern_creational
  | pattern_structural
"""

embedded_pattern_languages_body = """

// anti corruption layer 
pattern_anti_corruption                   : "^kpk"

pattern_bloc                              : "^bloc"

// circuit breaker
pattern_circuit_breaker                   : "^sekring"

pattern_concurrency                       : "^con"
// command query responsibility segregation
pattern_cqrs                              : "^cqrs"

pattern_dry                               : "^dry"

// event sourcing
pattern_event_sourcing                    : "^event"

pattern_fluent                            : "^flu"

pattern_listener                          : "^listen"
pattern_observable                        : "^observe"

// pubsub
pattern_pubsub                            : "^pubsub"

pattern_reference                         : "^ref"

// sharding
pattern_sharding                          : "^shard"
// sharding: range-based, vertical, hash-based

pattern_solid                             : "^solid"

// strangler
pattern_strangler                         : "^strangler"
// saga
pattern_saga                              : "^saga"
// throttling
pattern_throttling                        : "^throttle"
// static content hosting
pattern_static_content                    : "^static"

pattern_taskqueue                         : "^TQ"

pattern_visitor                           : "^visit"

pattern_behavioral                        : "^behav"
pattern_creational                        : "^create"
pattern_structural                        : "^struc"
"""
