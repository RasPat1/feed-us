"use strict";angular.module("utilFilters",[]).filter("checkmark",function(){return function(a){return a?"✓":"✘"}}).filter("toArray",function(){return function(a){return a instanceof Object?_.map(a,function(a,b){return Object.defineProperty(a,"$key",{__proto__:null,value:b})}):a}}),angular.module("feedUsApp",["ngCookies","ngResource","ngSanitize","utilFilters"]).config(["$routeProvider",function(a){a.when("/",{templateUrl:"views/main.html",controller:"MainCtrl"}).otherwise({redirectTo:"/"})}]),angular.module("feedUsApp").controller("MainCtrl",["$scope",function(a){a.id=function(){var b=0;a.nextId=function(){return b+=1}}(),a.initialize=function(){a.foods={},a.newFood("cheese"),a.newFood("vegetable cream cheese"),a.newFood("rat poison")},a.newFood=function(b){var c={id:a.nextId(),name:b,rating:0};a.foods[c.id]=c},a.addFood=function(){a.newFood(a.food.name),a.food.name=""},a.removeTodo=function(b){delete a.foods[b]},a.vote=function(b,c){a.foods[b].rating=a.foods[b].rating+c},a.clearSearch=function(){a.searchText=""},a.initialize()}]);