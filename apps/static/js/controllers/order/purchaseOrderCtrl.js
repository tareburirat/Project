app.controller("purchaseOrderCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.order = {};

    var getOrder = function (orderId) {
        $http.get($scope.mama + '/api/orders/' + orderId).then(
            function (response) {
                $scope.order = response.data;
            }
        )
    };

    $scope.getOrderId = function (orderId) {
        console.log(orderId);
        getOrder(orderId);
    };


});