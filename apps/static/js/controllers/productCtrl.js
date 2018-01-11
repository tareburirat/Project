var app = angular.module("app", []);
app.controller("productCtrl", function($scope, $http, $window) {
    $scope.products = [];
    $scope.mama = 123;
    $scope.productId = $window.productId;

    $scope.getId = function (id) {
        $scope.productId = id;
        getProduct()
    };

    console.log($scope.productId);
    var getProduct = function() {
        $http.get('http://localhost:8000/api/products/' + $scope.productId).then(function (response) {
            $scope.product = response.data;
            $scope.properties = Object.keys($scope.product.property)
        })
    }

}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

