% -----------------------------
%  FACTS: Dish Type (veg / nonveg)
% -----------------------------
type(paneer_tikka, veg).
type(veg_biryani, veg).
type(masala_dosa, veg).
type(chole_bhature, veg).
type(chicken_biryani, nonveg).
type(fish_fry, nonveg).
type(chicken_curry, nonveg).
type(mutton_kebab, nonveg).

% -----------------------------
%  FACTS: Taste (spicy / mild)
% -----------------------------
taste(paneer_tikka, spicy).
taste(veg_biryani, mild).
taste(masala_dosa, mild).
taste(chole_bhature, spicy).
taste(chicken_biryani, spicy).
taste(fish_fry, spicy).
taste(chicken_curry, mild).
taste(mutton_kebab, spicy).

likes(ram, veg, spicy).
likes(sita, veg, mild).
likes(rahim, nonveg, spicy).
likes(john, nonveg, mild).
likes(peter, veg, spicy).
likes(anu, nonveg, spicy).


% -----------------------------
%  RULES: Recommend based on preference
% -----------------------------
recommend(Customer, Dish) :-
    likes(Customer, Type, Taste),
     type(Dish, Type),
    taste(Dish, Taste).
veg_dish(Dish) :-
    type(Dish, veg).
spicy_dish(Dish) :-
    taste(Dish, spicy).
veg_spicy(Dish) :-
    type(Dish, veg),
    taste(Dish, spicy).
nonveg_spicy(Dish) :-
    type(Dish, nonveg),
    taste(Dish, spicy).
