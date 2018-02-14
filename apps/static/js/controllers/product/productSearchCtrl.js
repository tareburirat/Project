app.controller("productSearchCtrl", function($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.queryString = '?';
    var accountId = "";
    var userInfo = {};
    $scope.products = [];

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

    $scope.getQueryString = function (queryString) {
        if (queryString.product_name !== undefined) {
            $scope.queryString += "product_name=" + queryString.product_name;
        }

        if (queryString.category !== undefined) {
            // this if will be entered when $scope.queryString is not '?', means the first if was entered
            if ($scope.queryString !== '?') {
                $scope.queryString += '&'
            }
            $scope.queryString += "category=" + queryString.category;
        }


        searchProduct();
    };

    $http.get($scope.mama + '/api/categories/?category_type=0')
        .then(
            function (response) {
                $scope.categories = response.data;
            },
            function (response) {
                $scope.categories = [];
            }
        );


    var searchProduct = function () {
        $http.get($scope.mama + '/api/category_products/' + $scope.queryString)
            .then(
                function (response) {
                    $scope.categoryProducts = response.data;
                },
                function () {
                    alert('load data fail');
                    $window.location('/')
                })

    };

    $scope.addToCart = function (productId, sellerId) {
        console.log(accountId);
        if (accountId === "" || accountId === undefined) {
            alert("กรุณาเข้าสู่ระบบก่อน");
            return;
        }

        var data ={
            owner: accountId,
            product: productId
        };
        debugger;
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


});

