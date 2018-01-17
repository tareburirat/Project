var app = angular.module("app", []);
app.controller("cartCtrl", function ($scope, $http, $window) {
    $scope.carts = [];
    $scope.cartId = $window.cartId;

    $scope.getId = function (id) {
        $scope.cartId = id;
        getProduct()
    };

    console.log($scope.cartId);
    var getProduct = function () {
        $http.get('http://localhost:8000/api/carts/?owner_id=' + $scope.cartId).then(function (response) {
            $scope.carts = response.data;
        })
    };

    $scope.getTotal = function () {
        var total = 0;
        $scope.carts.forEach(function (cart) {
            total += parseInt(cart.product_data.sub_total);
        });
        return total;
    };


    $scope.delProduct = function (cartId) {
        $http.delete('http://localhost:8000/api/carts/' + cartId).then(
            function (response) {
                $scope.products = response;
                alert('delete success!!')
                getProduct();
            },
            function (response) {
                console.log(response.data)
                alert('fail!')
            }
        )
    }
}).config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
