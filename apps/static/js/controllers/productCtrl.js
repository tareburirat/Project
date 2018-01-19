app.controller("productCtrl", function($scope, $http, $window) {
    $scope.products = [];
    $scope.mama = 123;

    $scope.getOwnerId = function (ownerId) {
        $scope.ownerId = ownerId;
    };

    $scope.getId = function (id) {
        $scope.productId = id;
        getProduct()
    };

    console.log($scope.productId);
    var getProduct = function() {
        $http.get('http://localhost:8000/api/products/' + $scope.productId).then(function (response) {
            $scope.product = response.data;
            $scope.properties = Object.keys($scope.product.property)
        })
    };

    $scope.addToCart = function () {
        var data ={
            owner: $scope.ownerId,
            product: $scope.productId,
        };

        $http.post('http://localhost:8000/api/carts/', data).then(
            function (response) {
                // alert(response.data);
                $window.location.href = '/cart/'
            },
            function (response) {
                alert("failed: " + response.data)
            }
        )
    };
});

