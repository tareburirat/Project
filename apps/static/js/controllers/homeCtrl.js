app.controller("homeCtrl", function ($scope, $http, $window) {
    $scope.mama = 123;
    $scope.products = [];

    $scope.getBuyerId = function (buyerId) {
        $scope.buyerId = buyerId;
    };


    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.products = response.data;
        console.log($scope.products);
    });

    $scope.addToCart = function () {
        var data ={
            owner: $scope.buyerId,
            product: $scope.products,
        };

        $http.post('http://localhost:8000/api/carts/', data).then(
            function (response) {
                alert(response.data);
                $window.location.href = '/cart/'
            },
            function (response) {
                alert("failed: " + response.data)
            }
        )
    }


});