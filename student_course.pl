% ---------- Student–Course Enrollment Facts ----------

enrolled(mary, science).
enrolled(mary, math).

enrolled(john, math).
enrolled(john, physics).

enrolled(linda, physics).
enrolled(linda, english).

enrolled(peter, english).
enrolled(peter, science).

% ---------- Rules ----------

% Which courses does a student take?
courses_of_student(Student, Course) :-
    enrolled(Student, Course).

% Which students are enrolled in a course?
students_in_course(Course, Student) :-
    enrolled(Student, Course).
