app.controller("productSearchCtrl", function($scope, $http, $window, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.queryString = '?';
    var accountId = "";
    var userInfo = {};
    $scope.products = [];
    $scope.next = "";
    $scope.categoryProducts = [];
    $scope.promotes = [];

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

        $scope.searchProduct($scope.mama + '/api/category_products/' + $scope.queryString );
        $scope.getPromote($scope.mama + '/api/category_products/' + $scope.queryString + '&promoted=2');
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


    $scope.searchProduct = function (url) {
        $http.get(url)
            .then(
                function (response) {
                    $scope.categoryProducts = $scope.categoryProducts.concat(response.data.results);
                    $scope.next = response.data.next;
                },
                function () {
                    alert('load data fail');
                    $window.location('/')
                })

    };

    $scope.getPromote = function(url) {
        $http.get(url).then(
            function (response) {
                 $scope.promote = $scope.promotes.concat(response.data.results);
                $scope.next = response.data.next;
                // $scope.previous = response.data.previous;
            });
    };
    // $scope.getPromote($scope.mama + '/api/category_products/?product_name=&category=' + $scope.queryString + '&promoted=2');


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

