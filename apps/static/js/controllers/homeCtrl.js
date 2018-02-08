app.controller("homeCtrl", function ($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    var accountId = "";
    var userInfo = {};
    $scope.products = [];

    $http.get($scope.mama + '/api/products/?product_status=1').then(function (response) {
        $scope.products = response.data;
    });

    $scope.getAccountId = function(accId) {
        accountId = accId;
        getUserInfo(accId);
    };

    var getUserInfo = function (accId) {
        $http.get($scope.mama + '/api/accounts/' + accId + '/').then(
            function (response) {
                userInfo = response.data;
                console.log(userInfo);
            }
        )
    };

    $scope.addToCart = function (productId, sellerId) {
        if (userInfo.id === sellerId || userInfo.cart_products.indexOf(productId) > -1) {
            alert('ไม่สามารถซื้อสินค้าชิ้นนี้ลงตะกร้าได้');
            return;
        }
        console.log(accountId);
        if (accountId === "" || accountId === undefined) {
            alert("กรุณาเข้าสู่ระบบก่อน");
            return;
        }

        var data ={
            owner: accountId,
            product: productId
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

    $scope.viewProductDetail = function (productId) {
        $window.location.href = '/single/' + productId;
    };


});