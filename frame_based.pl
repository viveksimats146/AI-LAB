% frames.pl
% Simple frame-style knowledge representation with inheritance

% ---------- direct frame slot facts ----------
% frame(FrameName, SlotName, Value).
frame(car,        wheels,        4).
frame(car,        fuel,          petrol).
frame(car,        max_speed_kmh, 200).

frame(electric_car, battery,      lithium_ion).
frame(electric_car, fuel,         battery).        % override: electric uses battery
frame(electric_car, emissions,    none).

frame(hybrid_car,  engine,        petrol).
frame(hybrid_car,  battery,       small).
% hybrid does not declare wheels/fuel/max_speed -> should inherit from car

% ---------- ISA relationships (class-subclass) ----------
isa(electric_car, car).
isa(hybrid_car,   car).

% ---------- Slot lookup with inheritance ----------
% slot(+Frame, +Slot, -Value) is true when Frame has Slot = Value
% either directly or inherited through isa/2 chain.
slot(Frame, Slot, Value) :-
    frame(Frame, Slot, Value).             % direct slot

slot(Frame, Slot, Value) :-
    isa(Frame, Parent),                    % inherit from Parent
    slot(Parent, Slot, Value).
