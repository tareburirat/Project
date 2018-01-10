var app = angular.module("app", []);
app.controller("homeCtrl", function ($scope, $http) {
    $scope.products = [];
    $scope.mama = 123;

    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.product = response.data;
        console.log($scope.product);
    })

}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});