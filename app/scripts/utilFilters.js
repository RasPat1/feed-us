'use strict'

angular.module('utilFilters', []).
  filter('checkmark', function() {
    return function(input) {
      return input ? '\u2713' : '\u2718';
    };
  })
  .
  filter('toArray', function() { return function(obj) {
    if (!(obj instanceof Object)) return obj;
      return _.map(obj, function(val, key) {
        return Object.defineProperty(val, '$key', {__proto__: null, value: key});
      });
  }});