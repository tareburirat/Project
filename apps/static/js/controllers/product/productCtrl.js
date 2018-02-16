app.controller("productCtrl", function($scope, $http, $window, $rootScope) {
    $scope.products = [];
    $scope.mama = $rootScope.url;
    $scope.displayImage = "";
    $scope.altText = "1234";
    var userInfo = {};

    $scope.getOwnerId = function (ownerId) {
        $scope.ownerId = ownerId;
        getUserInfo(ownerId);
    };

    var getUserInfo = function (ownerId) {
        $http.get($scope.mama + '/api/accounts/' + ownerId + '/').then(
            function (response) {
                userInfo = response.data;
                console.log(userInfo);
            }
        )
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


    $scope.addToCart = function (productId, sellerId) {
        if (userInfo.id === sellerId || userInfo.cart_products.indexOf(productId) > -1){
            alert('ไม่สามารถซื้อสินค้าชิ้นนี้ลงตะกร้าได้');
            return;
        }
        console.log($scope.ownerId);
        if ($scope.ownerId === "" || $scope.ownerId === undefined) {
            alert("กรุณาเข้าสู่ระบบก่อน");
            return;
        }

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
    };

    $scope.make_offer = function (price) {
        var data = {
            offer_price: price,
            buyer: $scope.ownerId,
            product: $scope.productId
        };
        $http.post($scope.mama + '/api/offers/', data).then(
            function (response) {
                alert('offer made')
            },
            function (response) {
                data = response.data;
                alert('cannot make offer: ')
            }
        )
    };

});

