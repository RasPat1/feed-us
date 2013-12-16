'use strict';

angular.module('feedUsApp')
  .controller('MainCtrl', function ($scope) {

    $scope.id = function() {
      var id = 0;
      $scope.nextId = function() {
          id = id + 1;
          return id;
        };
    } ();

    $scope.initialize = function() {
      $scope.foods = {};
      $scope.newFood('cheese');
      $scope.newFood('vegetable cream cheese');
      $scope.newFood('rat poison');
    };
    
    $scope.newFood = function(name) {  //This is actually a constructor treat it that way
      var foodObj =  {
        'id' : $scope.nextId(),
        'name' : name,
        'rating' : 0
      };
      $scope.foods[foodObj.id] = foodObj;
    };
    // $scope.foods = [
    //   {"name": 'HTML5 Boilerplate', "rating": 0},
    //   {"name": 'AngularJS',"rating": 0},
    //   {"name": 'Karma',"rating": 0}
    // ];
 
    $scope.addFood = function() {
      $scope.newFood($scope.food.name);
      $scope.food.name = '';
    };

    $scope.removeTodo = function(id) {
      delete $scope.foods[id];
    };
    
    $scope.vote = function(id, d){
      $scope.foods[id].rating = $scope.foods[id].rating + d;
    };

    $scope.clearSearch =  function() {
      $scope.searchText = '';
    };

    $scope.initialize();
  });
