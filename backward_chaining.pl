% Define the facts and rules
bird(penguin) :- cannot_fly.
bird(eagle) :- can_fly.
cannot_fly.
can_fly :- has_wings.
has_wings.
% Define the backward chaining rules
infer(X) :- bird(X).
infer(X) :- can_fly, X = eagle.
infer(X) :- cannot_fly, X = penguin.
