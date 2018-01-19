app.controller("homeCtrl", function ($scope, $http, $window) {
    $scope.mama = 123;
    $scope.products = [];

    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.products = response.data;
        console.log($scope.products);
    });

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