var app = angular.module("app", []);
app.controller("productCtrl", function($scope, $http) {
    $scope.products = [];

    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.products = response.data;
        console.log($scope.products)
    })

}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
