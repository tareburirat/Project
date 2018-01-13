var app = angular.module("app", []);
app.controller("cartCtrl", function($scope, $http, $window) {
    $scope.products = [];
    $scope.cartId = $window.cartId;

    $scope.getId = function (id) {
        $scope.cartId = id;
        getProduct()
    };

    console.log($scope.cartId);
    var getProduct = function() {
        $http.get('http://localhost:8000/api/carts/?owner_id=' + $scope.cartId).then(function (response) {
            $scope.products = response.data;
        })
    }
}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

