'use strict';

angular.module('feedUsApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'utilFilters'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

