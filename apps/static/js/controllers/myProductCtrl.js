app.controller('myProductCtrl', function ($scope, $http, $window) {
    $scope.products = [];
    $scope.mama = 123;
    $scope.sellerId = $window.sellerId;
    $scope.productId = $window.productId;

    $scope.getId = function (id) {
        $scope.sellerId = id;
        getProduct();
    };


    var getProduct = function() {
        // debugger;
        $http.get('http://localhost:8000/api/products/?seller_id=' + $scope.sellerId).then(
            function (response) {
                $scope.products = response.data;
            },
            function (response) {
                console.log(response)
            })
    }

    $scope.delProduct = function (productId) {
        $http.delete('http://localhost:8000/api/products/' + productId).then(
            function (response) {
                $scope.products = response;
                alert('delete success!!')
                getProduct();
            }
        )
    }


});