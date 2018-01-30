app.controller("placeOrderCtrl", function ($scope, $http, $window) {
    $scope.mama = 123;
    var accountId = '';
    $scope.address = "";
    $scope.carts = [];
    $scope.data = {};
    $scope.getAccountId = function (userAccountId) {
        accountId = userAccountId;
        getUserInfo();
    };

    var getUserInfo = function () {
        $http.get('http://localhost:8000/api/accounts/' + accountId + '/').then(
            function success(response) {
                $scope.userInfo = response.data;
                $scope.address = response.data.primary_address;
                getProduct();
            },
            function failure() {
                alert('Cannot Retrieve User Information.');
                $window.path.href = 'http://localhost:8000/'
            }
        )
    };

    var getProduct = function () {
        $http.get('http://localhost:8000/api/carts/?in_cart=true&owner_id=' + $scope.userInfo.id).then(
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
            total += parseInt(cart.product_data.sub_total);
        });
        return total;
    };

    $scope.placeOrder = function () {
        var generateOrderItem = function (carts) {
            var orderItems = [];
            carts.forEach(function (cartItem) {
                var orderItem = {
                    price: cartItem.product_data.price,
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
            order_items: generateOrderItem($scope.carts)
        };
        $http.post('http://localhost:8000/api/orders/', data).then(
            function success(response) {
                alert('success')
            },
            function () {
                alert('fail')
            }
        )
    };

});