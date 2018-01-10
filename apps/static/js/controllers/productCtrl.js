<<<<<<< HEAD
(function () {
    'use strict';
=======
var app = angular.module("app", []);
app.controller("productCtrl", function($scope, $http, $window) {
    $scope.products = [];
    $scope.mama = 123;
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> 42543b110b5dd43f89275bc5aef35a95d8688beb
>>>>>>> tare

<<<<<<< HEAD
    var app = angular.module("app", []);
    app.controller("productCtrl", function($scope, MyService) {
        $scope.product = [];
=======

    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.products = response.data;
        console.log($scope.products)
    })
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> 09e8c01a597ffb557101ba99f17ffd18ddd76c00
>>>>>>> tare
=======
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
>>>>>>> origin/products

        MyService.getProduct().then(function (data) {
            $scope.product = data;
        });

}).factory('MyService', function ($http, $q) {
        'use strict';
        return {
            getProduct : function () {
                var deferred = $q.defer();

                $http.get('http://localhost:8000/api/products/').success(function (data) {
                        deferred.resolve(data);
                });
                return deferred.promise;
            }
        };
}).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
})();
