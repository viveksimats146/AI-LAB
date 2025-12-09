% Define the facts and rules
bird(penguin) :- cannot_fly.
bird(eagle) :- can_fly.
cannot_fly.
can_fly :- has_wings.
has_wings.
% Define the forward chaining rule
infer(X) :- bird(X).
