app.controller("purchaseOrderCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.orderNumber = '';
    $scope.getOrderNumber = function(orderNumber){
        $scope.orderNumber = orderNumber;
    }






});