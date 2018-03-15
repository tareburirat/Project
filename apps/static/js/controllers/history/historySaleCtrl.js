app.controller('historySaleCtrl', function ($scope, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    var accId = '';
    $scope.orderNumber = '';
    $scope.yoyo = '';
    $scope.orderItemId = 0;

    $scope.getAccountId = function (accountId) {
        accId = accountId;
        getOrderItem();
    };

    var getOrderItem = function () {
        $http.get($scope.mama + '/api/order_items/?seller_id=' + accId).then(
            function success(response) {
                $scope.order_items = response.data;
            },
            function failure() {
                alert('fail');
            }
        )
    };

    $scope.setOrderItemId = function (id) {
        $scope.orderItemId = id;
    };

    $scope.updateTrackOrder = function (orderItemId) {
        var data = {
            order_status: 1,
            order_track: $scope.tracking
        };
        $http.patch($scope.mama + '/api/order_items/' + orderItemId + '/', data).then(
            function (response) {
                console.log(response);
                alert('success');
                var found = $scope.accept_order_0.find(function (element) {
                    return element.id === orderItemId;
                });

                var index = $scope.accept_order_0.indexOf(found);
                $scope.accept_order_0.splice(index, 1);
                $scope.accept_order_1.push(found);

            },
            function (response) {
                console.log(response);
                alert('failed');
            }
        );
    };

    $scope.getAcceptOrder0 = function () {
        $http.get($scope.mama + '/api/order_items/?seller_id=' + accId + '&order_status=0').then(
            function (response) {
                $scope.accept_order_0 = response.data;
                console.log(response.data[0]);
            }
        );
    };

    $scope.getAcceptOrder1 = function () {
        $http.get($scope.mama + '/api/order_items/?seller_id=' + accId + '&order_status=1').then(
            function (response) {
                $scope.accept_order_1 = response.data;
            }
        );
    };

    $scope.getAcceptOrder2 = function () {
        $http.get($scope.mama + '/api/order_items/?seller_id=' + accId + '&order_status=2').then(
            function (response) {
                $scope.accept_order_2 = response.data;
            }
        );
    }

});