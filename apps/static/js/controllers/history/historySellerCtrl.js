app.controller('historySellerCtrl', function ($scope, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    var accId = '';
    $scope.orderNumber = '';
    $scope.yoyo = '';
    $scope.orderItemId = '';

    $scope.getAccountId = function (accountId) {
        accId = accountId;
        getOrderItem();
    };

    var getOrderItem = function () {
        $http.get($scope.mama + '/api/order_items/?order__buyer_id=' + accId).then(
            function success(response) {
                $scope.order_items = response.data;

            },
            function failure() {
                alert('fail');
            }
        )
    };

    $scope.setYoyo = function (orderNumber) {
        console.log(orderNumber);
        $scope.yoyo = orderNumber;
    }

    $scope.updateStatusOrder = function (orderItemId) {
        var data = {
            order_status: 1
        };
        $http.patch($scope.mama + '/api/order_items/' + orderItemId + '/', data).then(
            function (response) {
                console.log(response);
                alert('success');
                $window.location.href =  $scope.mama + 'account/purchase_history/';
            },
            function (response) {
                console.log(response);
                alert('failed');
            }
        );
    }
});