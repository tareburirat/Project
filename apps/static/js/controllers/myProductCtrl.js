app.controller('myProductCtrl', function ($scope, $http, $window, $rootScope) {
    $scope.products = [];
    $scope.mama = $rootScope.url;
    $scope.sellerId = $window.sellerId;
    $scope.productId = $window.productId;

    $scope.getId = function (id) {
        $scope.sellerId = id;
        getProduct();
    };


    var getProduct = function() {
        // debugger;
        $http.get($scope.mama + '/api/products/?seller_id=' + $scope.sellerId).then(
            function (response) {
                $scope.products = response.data;
            },
            function (response) {
                console.log(response)
            })
    }

    $scope.delProduct = function (productId) {
        $http.delete($scope.mama + '/api/products/' + productId).then(
            function (response) {
                $scope.products = response;
                alert('delete success!!')
                getProduct();
            }
        )
    }


});