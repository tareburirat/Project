app.controller('historySellerCtrl', function ($scope, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    var accId = '';
    $scope.orderNumber = '';
    $scope.yoyo = 0;

    $scope.getAccountId = function (accountId) {
        accId = accountId;
        getOrderItem();
        $scope.getOrderNumber();
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

    $scope.getOrderNumber = function(orderNumber){
        $scope.orderNumber = orderNumber;
    }
});