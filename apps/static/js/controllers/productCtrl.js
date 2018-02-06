app.controller("productCtrl", function($scope, $http, $window, $rootScope) {
    $scope.products = [];
    $scope.mama = $rootScope.url;
    $scope.displayImage = "";
    $scope.altText = "1234";

    $scope.getOwnerId = function (ownerId) {
        $scope.ownerId = ownerId;
    };

    $scope.getId = function (id) {
        $scope.productId = id;
        getProduct()
    };

    console.log($scope.productId);
    var getProduct = function() {
        $http.get($scope.mama + '/api/products/' + $scope.productId).then(function (response) {
            $scope.product = response.data;
            $scope.properties = Object.keys($scope.product.property);
            $scope.setImage(response.data.first_image_url);
        })
    };


    $scope.addToCart = function () {
        var data ={
            owner: $scope.ownerId,
            product: $scope.productId
        };

        $http.post($scope.mama + '/api/carts/', data).then(
            function (response) {
                // alert(response.data);
                $window.location.href = '/cart/'
            },
            function (response) {
                alert("failed: " + response.data)
            }
        )
    };

    $scope.setImage = function (imageUrl) {
        $scope.displayImage = imageUrl;
        $scope.altText += "!"
    }
});

