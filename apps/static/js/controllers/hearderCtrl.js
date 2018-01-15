var app = angular.module("app", []);
app.controller("headerCtrl", function($scope, $http, $window, $location) {
    $scope.mama = 123;
    $scope.searchKeyWord = '1234';

    $http.get('http://localhost:8000/api/categories/?category_type=0')
        .then(
            function (response) {
                $scope.categories = response.data;
            },
            function (response) {
                $scope.categories = [];
            }
        );

    $scope.search = function () {
        $location.path('/product_search/?product_name=' + $scope.searchKeyWord)
    }
}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

