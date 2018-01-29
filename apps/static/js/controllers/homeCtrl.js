app.controller("homeCtrl", function ($scope, $http, $window) {
    $scope.mama = 123;
    var accountId = "";
    var userInfo = {};
    $scope.products = [];

    $http.get('http://localhost:8000/api/products/').then(function (response) {
        $scope.products = response.data;
    });

    $scope.getAccountId = function(accId) {
        accountId = accId;
        getUserInfo(accId);
    };

    var getUserInfo = function (accId) {
        $http.get('http://localhost:8000/api/accounts/' + accId + '/').then(
            function (response) {
                userInfo = response.data;
                console.log(userInfo);
            }
        )
    };

    $scope.addToCart = function (productId) {
        console.log(accountId);
        if (accountId === "" || accountId === undefined) {
            alert("You must LOG IN first.");
            return
        }

        var data ={
            owner: accountId,
            product: productId
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

    $scope.viewProductDetail = function (productId) {
        $window.location.href = '/single/' + productId;
    };



});