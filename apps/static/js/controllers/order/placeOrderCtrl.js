app.controller("placeOrderCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    var accountId = '';
    $scope.address = "";
    $scope.carts = [];
    $scope.data = {};
    $scope.getAccountId = function (userAccountId) {
        accountId = userAccountId;
        getUserInfo();
    };

    var getUserInfo = function () {
        $http.get($scope.mama + '/api/accounts/' + accountId + '/').then(
            function success(response) {
                $scope.userInfo = response.data;
                $scope.address = response.data.primary_address;
                getProduct();
            },
            function failure() {
                alert('Cannot Retrieve User Information.');
                $window.path.href = $scope.mama
            }
        )
    };

    var getProduct = function () {
        $http.get($scope.mama + '/api/carts/?in_cart=true&owner_id=' + $scope.userInfo.id).then(
            function success(response) {
                $scope.carts = response.data;

            },
            function failure() {
                alert('Cannot retrieve cart information.');
            }
        )
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

    $scope.placeOrder = function () {
        var generateOrderItem = function (carts) {
            var orderItems = [];
            carts.forEach(function (cartItem) {
                var orderItem = {
                    price: cartItem.sale_price,
                    product: cartItem.product_data.id,
                    seller: cartItem.product_data.seller
                };
                orderItems.push(orderItem);
            });
            return orderItems;
        };

        var data = {
            price: $scope.getTotal(),
            buyer: $scope.userInfo.id,
            order_items: generateOrderItem($scope.carts),
            order_address: $scope.address
        };
        $http.post($scope.mama + '/api/orders/', data).then(
            function success(response) {
                alert('success');
                // $window.location.href = $scope.mama + '/order/purchase_order/' + response.data.id;
                $window.location.href = $scope.mama + '/bank_accounts/pick_or_create/';
            },
            function () {
                alert('fail')
            }
        )
    };

});