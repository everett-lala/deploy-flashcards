from django.urls import path
from . import views


urlpatterns = [
    #localhost:8000/flashcards/
    path('', views.home, name='home'),
    #localhost:8000/flashcards/addition
    path('addition', views.addition, name='addition'),
    #localhost:8000/flashcards/addition_lvl_two
    path('addition_lvl_two', views.addition_lvl_two, name='addition-lvl-two'),
    #localhost:8000/flashcards/addition_lvl_three
    path('addition_lvl_three', views.addition_lvl_three, name='addition-lvl-three'),
    #localhost:8000/flashcards/addition_lvl_four
    path('addition_lvl_four', views.addition_lvl_four, name='addition-lvl-four'),

    #localhost:8000/flashcards/substraction
    path('subtraction', views.subtraction, name='subtraction'),
    #localhost:8000/flashcards/subtraction_lvl_two
    path('subtraction_lvl_two', views.subtraction_lvl_two, name='subtraction-lvl-two'),
    #localhost:8000/flashcards/subtraction_lvl_three
    path('subtraction_lvl_three', views.subtraction_lvl_three, name='subtraction-lvl-three'),
    #localhost:8000/flashcards/subtraction_lvl_four
    path('subtraction_lvl_four', views.subtraction_lvl_four, name='subtraction-lvl-four'),

    #localhost:8000/flashcards/multiplication
    path('multiplication', views.multiplication, name='multiplication'),
    #localhost:8000/flashcards/multiplication_lvl_two
    path('multiplication_lvl_two', views.multiplication_lvl_two, name='multiplication-lvl-two'),
    #localhost:8000/flashcards/multiplication_lvl_three
    path('multiplication_lvl_three', views.multiplication_lvl_three, name='multiplication-lvl-three'),
    #localhost:8000/flashcards/multiplication_lvl_four
    path('multiplication_lvl_four', views.multiplication_lvl_four, name='multiplication-lvl-four'),

    #localhost:8000/flashcards/division
    path('division', views.division, name='division'),
    #localhost:8000/flashcards/division_lvl_two
    path('division_lvl_two', views.division_lvl_two, name='division-lvl-two'),
    #localhost:8000/flashcards/division_lvl_three
    path('division_lvl_three', views.division_lvl_three, name='division-lvl-three'),
    #localhost:8000/flashcards/division_lvl_four
    path('division_lvl_four', views.division_lvl_four, name='division-lvl-four'),

    #localhost:8000/flashcards/logout
    path('logout', views.logout, name='logout'),

    #localhost:8000/flashcards/statecapitals
    path('statecapitals', views.statecapitals, name='statecapitals'),
    #localhost:8000/flashcards/statecapitals (ordered by statehood)
    path('statestudy', views.statestudy, name='statestudy'),
    #localhost:8000/flashcards/statecapitals (ordered by name)
    path('statestudy_byname', views.statestudy_byname, name='statestudy-byname'),
    #localhost:8000/flashcards/statecapitals (ordered by name)
    path('statestudy_random', views.statestudy_random, name='statestudy-random'),

    #localhost:8000/flashcards/stateshape
    path('stateshape', views.stateshape, name='stateshape'),
    #localhost:8000/flashcards/stateflag
    path('stateflag', views.stateflag, name='stateflag'),


    #localhost:8000/flashcards/to_do
    path('to_do', views.to_do, name='to-do'),
    path('done/<list_id>', views.done, name='done'),
    path('not_completed/<list_id>', views.not_completed, name='not-completed'),
    path('todo_delete/<list_id>', views.todo_delete, name='todo-delete'),


    #localhost:8000/flashcards/word_scramble
    path('word_scramble', views.word_scramble, name='word-scramble'),
    path('word_scramble_five', views.word_scramble_five, name='word-scramble-five'),
    path('word_scramble_six', views.word_scramble_six, name='word-scramble-six'),
    path('word_scramble_seven', views.word_scramble_seven, name='word-scramble-seven'),
    path('word_scramble_eight', views.word_scramble_eight, name='word-scramble-eight'),


    path('word_scramble_incorrect', views.word_scramble_incorrect, name='word-scramble-incorrect'),
    path('word_scramble_incorrect_five', views.word_scramble_incorrect_five, name='word-scramble-incorrect-five'),
    path('word_scramble_incorrect_six', views.word_scramble_incorrect_six, name='word-scramble-incorrect-six'),
    path('word_scramble_incorrect_seven', views.word_scramble_incorrect_seven, name='word-scramble-incorrect-seven'),
    path('word_scramble_incorrect_eight', views.word_scramble_incorrect_eight, name='word-scramble-incorrect-eight'),

    path('word_scramble_mercy', views.word_scramble_mercy, name='word-scramble-mercy'),
    path('word_scramble_mercyfive', views.word_scramble_mercyfive, name='word-scramble-mercyfive'),
    path('word_scramble_mercysix', views.word_scramble_mercysix, name='word-scramble-mercysix'),
    path('word_scramble_mercyseven', views.word_scramble_mercyseven, name='word-scramble-mercyseven'),
    path('word_scramble_mercyeight', views.word_scramble_mercyeight, name='word-scramble-mercyeight'),

]
