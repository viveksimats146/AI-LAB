% define some facts about teachers and their subject codes
teaches(john, math).
teaches(jane, english).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).
% define some facts about students and the subjects they are taking
takes(alice, math).
takes(alice, science).
takes(bob, english).
takes(bob, science).
takes(carol, history).
takes(carol, art).
takes(dave, math).
takes(dave, english).
takes(dave, art).
% define a predicate to look up the subject codes taught by a teacher
teaching_subjects(Teacher, Subject) :-
teaches(Teacher, Subject).
% define a predicate to look up the students taking a given subject
taking_students(Subject, Student) :-
takes(Student, Subject).
