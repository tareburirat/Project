var app = angular.module("app", []);
app.controller("registerBuyerCtrl", function($scope, $http) {



}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});