app.controller("cartCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.carts = [];
    $scope.cartId = $window.cartId;
    $scope.mama = $rootScope.url;

    $scope.getId = function (id) {
        $scope.cartId = id;
        getProduct()
    };

    var getProduct = function () {
        $http.get($scope.mama + '/api/carts/?in_cart=true&owner_id=' + $scope.cartId).then(function (response) {
            $scope.carts = response.data;
        })
    };

    $scope.getTotal = function () {
        var total = 0;
        $scope.carts.forEach(function (cart) {
            total += $scope.subTotal(cart);
        });
        return total;
    };

    $scope.subTotal = function (cart) {
        return parseInt(cart.sale_price) + parseInt(cart.product_data.freight_fee);
    };

    $scope.delProduct = function (cartId) {
        $http.delete($scope.mama + '/api/carts/' + cartId).then(
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
});